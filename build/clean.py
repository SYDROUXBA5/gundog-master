"""Clean the book plate: keep the dog, erase the page.

Three rules, in this order:

1. The dog is never masked or moved. Most gundogs are white-and-liver, and a
   white chest is the same tone as white paper, so any "keep what differs from
   paper" rule amputates the pale half of the animal. Everything here works by
   deciding what to REMOVE.

2. Text is separated from dog by STRUCTURE, not position. A caption stroke is a
   few pixels thick; a dog's leg is fifty. An opening large enough to erase any
   glyph leaves only the animal, which is then grown back through the ink so
   legs, ears and tail return. Whatever ink is left over is type, leader lines,
   the curled page edge or the table, and gets painted out — including captions
   that sit right against the dog, which an earlier "erase what is far from the
   dog" rule could never reach.

3. The background is then flattened to one flat paper colour outside the dog's
   row-wise span, which removes page shading, the curl, the table and any ghost
   of the painted-out type. The span is used rather than the silhouette so pale
   markings, which are invisible to the ink test, stay inside the protected
   region and survive.
"""
import json, os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, "crops")
OUT = os.path.join(HERE, "cut")


def span_fill(mask):
    """Fill each row between the leftmost and rightmost set pixel."""
    out = np.zeros_like(mask)
    rows = np.where(mask.any(axis=1))[0]
    for y in rows:
        xs = np.where(mask[y])[0]
        out[y, xs[0]:xs[-1] + 1] = True
    return out


def clean(path, work=1000, pad=0.04, no_recrop=False):
    full = Image.open(path).convert("RGB")
    small = full.copy()
    small.thumbnail((work, work))
    a = np.asarray(small).astype(np.float32)
    h, w, _ = a.shape

    edge = np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3),
                           a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)])
    paper = np.percentile(edge, 84, axis=0)
    dist = np.abs(a - paper).max(axis=2)
    sat = a.max(axis=2) - a.min(axis=2)
    ink = (dist > 18) | (sat > 24)

    k = max(15, int(round(w * 0.028)) | 1)
    core = ndimage.binary_opening(ink, structure=np.ones((k, k)))
    core = ndimage.binary_fill_holes(core)
    lab, n = ndimage.label(core)
    if n == 0:
        return None
    best, area = None, 0.0
    for sl, idx in zip(ndimage.find_objects(lab), range(1, n + 1)):
        ys, xs = sl
        if (ys.stop - ys.start) / h < 0.18 or (xs.stop - xs.start) / w < 0.12:
            continue
        s = float((lab[sl] == idx).sum())
        if s > area:
            best, area = idx, s
    if best is None:
        return None

    body = ndimage.binary_propagation(lab == best, mask=ndimage.binary_fill_holes(ink))
    body = ndimage.binary_opening(body, structure=np.ones((7, 7)))   # sever leaders
    lab2, n2 = ndimage.label(body)
    if n2:
        sizes = ndimage.sum(body, lab2, range(1, n2 + 1))
        body = lab2 == (int(np.argmax(sizes)) + 1)
    body = ndimage.binary_fill_holes(body)

    keep = ndimage.binary_dilation(body, structure=np.ones((3, 3)))

    # The body absorbs the ground shadow the dog stands in, because the shadow is
    # ink and touches the feet. Captions printed inside that shadow are therefore
    # "part of the dog" to the rule above and survive it. So type is caught a
    # second way, by stroke width: a glyph is a few pixels thick and vanishes
    # under a small opening, while a leg or a muzzle does not. Erasing every thin
    # stroke ANYWHERE catches those captions and the leader lines with them, at
    # the cost of shaving a pixel or two off the fur silhouette.
    t = max(9, int(round(w * 0.014)) | 1)
    thin = ink & ~ndimage.binary_opening(ink, structure=np.ones((t, t)))

    # "Ink that is not the body" is too blunt on its own: a raised head or an ear
    # that the opening separated from the trunk is exactly that, and painting it
    # out beheads the dog. Type is not merely non-body, it is non-body AND small,
    # so only small leftovers are erased and any large blob is left alone. The
    # big non-dog objects — a neighbouring breed, the curled page, the table —
    # are kept out of frame by HAND_BOX instead, where a rule cannot help.
    rest = ink & ~keep
    rl, rn = ndimage.label(rest)
    small = np.zeros_like(rest)
    if rn:
        sizes = ndimage.sum(rest, rl, range(1, rn + 1))
        limit = 0.012 * w * h
        keep_ids = np.where(sizes <= limit)[0] + 1
        small = np.isin(rl, keep_ids)
    erase = small | thin
    protect = ndimage.binary_dilation(span_fill(body), structure=np.ones((5, 5)))
    flatten = ~protect

    # Trim the box to where the animal actually is. The body absorbs the ground
    # shadow, which on some pages runs off the plate and drags the table edge
    # into the crop; rows and columns holding only a trace of it are not dog.
    rows, cols = body.sum(axis=1), body.sum(axis=0)
    ry = np.where(rows > max(3.0, rows.max() * 0.04))[0]
    rx = np.where(cols > max(3.0, cols.max() * 0.04))[0]
    box = (rx[0] / w, ry[0] / h, (rx[-1] + 1) / w, (ry[-1] + 1) / h)

    W, H = full.size

    def up(m, grow):
        im = Image.fromarray((m * 255).astype(np.uint8), "L").resize((W, H), Image.BILINEAR)
        if grow:
            im = im.filter(ImageFilter.MaxFilter(grow))
        return im.filter(ImageFilter.GaussianBlur(1.6)).point(lambda v: 255 if v > 90 else 0)

    # Painting with one flat colour left ghost rectangles wherever type had been,
    # because the page is photographed under a lighting gradient and no single
    # value matches it everywhere. So the fill is a locally estimated page tone:
    # blank the ink to flat paper, blur that heavily, and the result is the
    # page's own shading with the dog and the type taken out of it.
    pap = tuple(int(round(c)) for c in paper)
    flat = Image.new("RGB", (W, H), pap)
    blanked = Image.composite(flat, full, up(ink, 7))
    local = blanked.filter(ImageFilter.GaussianBlur(max(12, W // 22)))

    out = Image.composite(local, full, up(erase, 5).filter(ImageFilter.GaussianBlur(1.2)))
    out = Image.composite(local, out, up(flatten, 0).filter(ImageFilter.GaussianBlur(2.5)))

    cov = body.sum() / (w * h)
    if no_recrop:
        return out, (0.0, 0.0, 1.0, 1.0), cov, box[2] - box[0], box[3] - box[1]
    x0, y0 = max(0.0, box[0] - pad), max(0.0, box[1] - pad)
    x1, y1 = min(1.0, box[2] + pad), min(1.0, box[3] + pad)
    return (out.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))),
            (x0, y0, x1, y1), cov, box[2] - box[0], box[3] - box[1])


# A handful of plates print the neighbouring breed, a strip of puppies or the
# table edge hard against the dog, close enough that no automatic rule can tell
# it from the animal. Those are trimmed by hand, in crops/ space, before the
# cleaner sees them: (left, top, right, bottom) as fractions to cut away.
HAND_TRIM = {
    "IMG_4339": (0.075, 0.00, 0.00, 0.00),   # neighbouring dog, left edge
    "IMG_4340": (0.00, 0.085, 0.00, 0.02),   # strip of puppy feet across the top
    "IMG_4346": (0.00, 0.00, 0.02, 0.125),   # table under the book, page curl
    "IMG_4350": (0.00, 0.00, 0.03, 0.00),    # page edge, right
    "IMG_4355": (0.00, 0.135, 0.03, 0.00),   # chapter header and caption block
    "IMG_4360": (0.045, 0.00, 0.00, 0.07),   # page edge left, table below
    "IMG_4364": (0.10, 0.275, 0.00, 0.06),   # header text, neighbour dog, table
}
# Five plates where automatic framing cannot win: the neighbouring breed, a
# strip of puppies, a chapter header or the table sit hard against the dog, and
# every automatic box either keeps the furniture or clips the animal. These
# frames were read off a decile grid by eye, in crops/ space, and are used
# verbatim — the cleaner still erases the type inside them, but does not get to
# re-crop and second-guess the framing.
HAND_BOX = {
    "IMG_4340": (0.00, 0.130, 1.00, 1.000),   # drop the strip of puppy feet
    "IMG_4353": (0.03, 0.050, 1.00, 0.930),   # second dog above, table below
    "IMG_4355": (0.14, 0.030, 1.00, 0.940),   # chapter text left, table below
    "IMG_4360": (0.045, 0.000, 1.00, 0.905),  # page edge left, table below
    "IMG_4364": (0.12, 0.040, 1.00, 0.950),   # neighbouring dog left, table right
    # thin chapter-header bands along the very top; safe to shave because the
    # dog's head sits well below them on these plates
    "IMG_4368": (0.00, 0.055, 1.00, 1.000),
    "IMG_4376": (0.00, 0.090, 1.00, 1.000),
    "IMG_4386": (0.00, 0.055, 1.00, 1.000),
    "IMG_4391": (0.00, 0.055, 1.00, 1.000),
    "IMG_4393": (0.00, 0.060, 1.00, 1.000),
}
SKIP_TIGHT = set(HAND_BOX)


def run():
    """Two passes.

    Pass one only asks "where is the dog?". Whatever else shares the source
    rectangle — a chapter header, the neighbouring breed's photograph, the
    curled page edge, the table under the book — survives cleaning because it
    is thick, page-coloured furniture rather than type, and no amount of
    cleverness in the mask removes something that is genuinely in frame.

    So pass one's answer is used to re-crop the page tightly around the animal,
    and pass two cleans that. The furniture is then simply not in the picture.
    """
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(HERE, "_tight")
    os.makedirs(tmp, exist_ok=True)
    boxes, weak = {}, []
    for f in sorted(os.listdir(CROPS)):
        if not f.endswith(".jpg"):
            continue
        key = f[:-4]
        if key in HAND_BOX:
            bx = HAND_BOX[key]
            im0 = Image.open(os.path.join(CROPS, f)).convert("RGB")
            W0, H0 = im0.size
            im0.crop((int(bx[0] * W0), int(bx[1] * H0),
                      int(bx[2] * W0), int(bx[3] * H0))).save(
                          os.path.join(tmp, "h_" + f), quality=95)
            r = clean(os.path.join(tmp, "h_" + f), no_recrop=True)
            if r is None:
                weak.append((key, "hand-box no core"))
                continue
            r[0].save(os.path.join(OUT, f), quality=92)
            boxes[key] = [round(v, 4) for v in bx]
            continue
        src = Image.open(os.path.join(CROPS, f)).convert("RGB")
        base = (0.0, 0.0, 1.0, 1.0)
        if key in HAND_TRIM:
            l, t, r_, b = HAND_TRIM[key]
            base = (l, t, 1.0 - r_, 1.0 - b)
            W0, H0 = src.size
            src = src.crop((int(base[0] * W0), int(base[1] * H0),
                            int(base[2] * W0), int(base[3] * H0)))
            trimmed = os.path.join(tmp, "t_" + f)
            src.save(trimmed, quality=95)
            first = clean(trimmed, pad=0.06)
        else:
            first = clean(os.path.join(CROPS, f), pad=0.06)
        if first is None:
            weak.append((key, "no core"))
            continue
        _, b1, _, _, _ = first
        W, H = src.size
        tight = src.crop((int(b1[0] * W), int(b1[1] * H), int(b1[2] * W), int(b1[3] * H)))
        tpath = os.path.join(tmp, f)
        tight.save(tpath, quality=95)

        second = clean(tpath, pad=0.02)
        if second is None:
            weak.append((key, "pass2 lost it"))
            tight.save(os.path.join(OUT, f), quality=92)
            boxes[key] = [round(v, 4) for v in b1]
            continue
        img, b2, cov, bw, bh = second
        img.save(os.path.join(OUT, f), quality=92)
        # compose hand trim + both passes so anchors authored in crops/ space still map
        sx, sy = b1[2] - b1[0], b1[3] - b1[1]
        c = (b1[0] + b2[0] * sx, b1[1] + b2[1] * sy,
             b1[0] + b2[2] * sx, b1[1] + b2[3] * sy)
        bx, by = base[2] - base[0], base[3] - base[1]
        boxes[key] = [round(v, 4) for v in (base[0] + c[0] * bx, base[1] + c[1] * by,
                                            base[0] + c[2] * bx, base[1] + c[3] * by)]
        if cov < 0.14:
            weak.append((key, f"cov={cov:.2f}"))
    json.dump(boxes, open(os.path.join(HERE, "cutboxes.json"), "w"), indent=0)
    print(f"cleaned {len(boxes)}")
    print(f"suspect ({len(weak)}): " + ", ".join(f"{k}[{v}]" for k, v in weak))


if __name__ == "__main__":
    run()
