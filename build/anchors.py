"""Convert photo-space anchors to plate-space, and render a proof sheet.

The plate is `aspect-ratio:4/3; padding:7% 8% 9%` with the image bottom-aligned
and centred (align-items:flex-end; justify-content:center). CSS padding percentages
resolve against the element WIDTH on every side, so with plate width 100 the
content box is x in [8,92] and y in [7,66], and the plate height is 75.
`left:%` resolves against width, `top:%` against height -- hence the /75 on ay.
"""
from PIL import Image, ImageDraw
import os, sys, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from breeds import B

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, "cut")
CUT = json.load(open(os.path.join(HERE, "cutboxes.json"))) \
    if os.path.exists(os.path.join(HERE, "cutboxes.json")) else {}
PAD = 0.02   # must match cutout.py


def in_photo(src, fx, fy):
    """Leader anchors are pinned by hand in `crops/` space -- automatic subject
    detection kept swallowing the caption text, so the localized marks are
    placed manually and every whole-animal mark uses the engine's label-only
    `whole` mode, which needs no coordinates at all.

    The shipped image is the lifted cut-out, a sub-rectangle of that crop, so
    the anchor is re-expressed against the cut before it reaches the plate.
    Sources absent from cutboxes.json ship their plain crop and map 1:1."""
    box = CUT.get(src)
    if not box:
        return fx, fy
    x0, y0 = max(0.0, box[0] - PAD), max(0.0, box[1] - PAD)
    x1, y1 = min(1.0, box[2] + PAD), min(1.0, box[3] + PAD)
    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        return fx, fy
    return min(max((fx - x0) / w, 0.0), 1.0), min(max((fy - y0) / h, 0.0), 1.0)

PLATE_W, PLATE_H = 100.0, 75.0
BOX_X0, BOX_X1 = 8.0, 92.0
BOX_Y0, BOX_Y1 = 7.0, 66.0
BOX_W, BOX_H = BOX_X1 - BOX_X0, BOX_Y1 - BOX_Y0


def to_plate(iw, ih, fx, fy):
    """photo-space fraction -> (ax, ay) as the engine's left:%/top:% pair."""
    scale = min(BOX_W / iw, BOX_H / ih)
    sw, sh = iw * scale, ih * scale
    x0 = BOX_X0 + (BOX_W - sw) / 2.0
    y0 = BOX_Y1 - sh                      # bottom-aligned
    ax = x0 + fx * sw
    ay = (y0 + fy * sh) / PLATE_H * 100.0
    return round(ax, 2), round(ay, 2)


def solve_all():
    out = {}
    for b in B:
        im = Image.open(os.path.join(CROPS, b["src"] + ".jpg"))
        fx, fy = in_photo(b["src"], *b["anchor"])
        out[b["src"]] = to_plate(im.width, im.height, fx, fy)
    return out


def proof(path, cols=6, cell=300):
    """Render each plate exactly as the browser would, with the dot drawn on."""
    items = [b for b in B if not b.get('whole')]
    rows = math.ceil(len(items) / cols)
    cw, ch = cell, int(cell * 0.75) + 20
    sheet = Image.new("RGB", (cols * cw, rows * ch), "#BEC5C9")
    d = ImageDraw.Draw(sheet)
    for i, b in enumerate(items):
        im = Image.open(os.path.join(CROPS, b["src"] + ".jpg"))
        ox, oy = (i % cols) * cw, (i // cols) * ch
        pw, ph = cell, int(cell * 0.75)
        d.rectangle([ox, oy, ox + pw, oy + ph], fill="#F4F0EC")
        # replicate the content box in pixels
        bx0, bx1 = ox + pw * BOX_X0 / 100, ox + pw * BOX_X1 / 100
        by0, by1 = oy + pw * BOX_Y0 / 100, oy + pw * (100 - 9) / 100
        scale = min((bx1 - bx0) / im.width, (by1 - by0) / im.height)
        sw, sh = int(im.width * scale), int(im.height * scale)
        thumb = im.resize((sw, sh))
        px = int(bx0 + ((bx1 - bx0) - sw) / 2)
        py = int(by1 - sh)
        sheet.paste(thumb, (px, py))
        ax, ay = to_plate(im.width, im.height, *in_photo(b["src"], *b["anchor"]))
        dx = ox + pw * ax / 100.0
        dy = oy + ph * ay / 100.0
        r = 5
        d.ellipse([dx - r - 2, dy - r - 2, dx + r + 2, dy + r + 2], fill="white")
        d.ellipse([dx - r, dy - r, dx + r, dy + r], fill="#1665B2")
        d.text((ox + 5, oy + ph + 3), f'{b["src"][4:]} {b["mark"][:22]}', fill="#12222E")
    sheet.save(path, quality=88)
    return sheet.size


if __name__ == "__main__":
    print(proof(os.path.join(HERE, "proof.jpg")))
