"""Lift the dog off the page onto a clean field.

Cropping alone cannot work: the caption text and the intro paragraph sit inside
any rectangle that contains the dog, and several of them print the breed name --
which hands the student the answer. So the dog is masked out instead and
composited onto flat paper, which erases every glyph outside its silhouette.

Method: threshold ink against the paper colour, open hard enough to erase any
glyph stroke (leaving only the dog's core), then reconstruct the full animal by
propagating that core back through the ink mask so legs, ears and tail return.
A light second opening severs the hairline leader lines that touch the dog and
would otherwise drag their captions back in.
"""
import os, json
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, "crops")
OUT = os.path.join(HERE, "cut")
FIELD = (244, 240, 236)          # --field, the plate's own near-white


def lift(path, work=900, dthr=22, sthr=28):
    im = Image.open(path).convert("RGB")
    full = im.copy()
    im.thumbnail((work, work))
    a = np.asarray(im).astype(np.float32)
    h, w, _ = a.shape

    border = np.concatenate([a[:10].reshape(-1, 3), a[-10:].reshape(-1, 3),
                             a[:, :10].reshape(-1, 3), a[:, -10:].reshape(-1, 3)])
    paper = np.percentile(border, 80, axis=0)
    diff = np.abs(a - paper).max(axis=2)
    sat = a.max(axis=2) - a.min(axis=2)
    ink = (diff > dthr) | (sat > sthr)

    k = max(13, int(round(w * 0.026)) | 1)        # glyph-killing opening
    core = ndimage.binary_opening(ink, structure=np.ones((k, k)))
    core = ndimage.binary_fill_holes(core)

    lab, n = ndimage.label(core)
    if n == 0:
        return None
    best, score = None, -1.0
    for sl, idx in zip(ndimage.find_objects(lab), range(1, n + 1)):
        ys, xs = sl
        bh, bw = (ys.stop - ys.start) / h, (xs.stop - xs.start) / w
        if bh < 0.22 or bw < 0.16:                # title bands: wide, shallow
            continue
        area = float((lab[sl] == idx).sum()) / (w * h)
        if area > score:
            best, score = idx, area
    if best is None:
        return None

    seed = (lab == best)
    dog = ndimage.binary_propagation(seed, mask=ndimage.binary_fill_holes(ink))
    dog = ndimage.binary_opening(dog, structure=np.ones((5, 5)))   # cut leaders
    lab2, n2 = ndimage.label(dog)
    if n2:
        sizes = ndimage.sum(dog, lab2, range(1, n2 + 1))
        dog = lab2 == (int(np.argmax(sizes)) + 1)
    dog = ndimage.binary_fill_holes(dog)
    dog = ndimage.binary_dilation(dog, structure=np.ones((5, 5)))

    ys, xs = np.where(dog)
    if len(xs) == 0:
        return None
    box = (xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h)
    # white dogs on white paper barely clear the ink threshold and come out in
    # fragments; if the silhouette is implausibly small, go again more sensitive
    if dog.sum() / (w * h) < 0.14 and dthr > 10:
        return lift(path, work, dthr - 6, sthr - 8)

    m = Image.fromarray((dog * 255).astype(np.uint8), "L") \
             .resize(full.size, Image.BILINEAR) \
             .filter(ImageFilter.GaussianBlur(2.2))
    plate = Image.new("RGB", full.size, FIELD)
    lifted = Image.composite(full, plate, m)

    W, H = full.size
    pad = 0.02
    x0, y0 = max(0.0, box[0] - pad), max(0.0, box[1] - pad)
    x1, y1 = min(1.0, box[2] + pad), min(1.0, box[3] + pad)
    return lifted.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))), box


def run():
    os.makedirs(OUT, exist_ok=True)
    rep, miss = {}, []
    for f in sorted(os.listdir(CROPS)):
        if not f.endswith(".jpg"):
            continue
        r = lift(os.path.join(CROPS, f))
        if r is None:
            miss.append(f[:-4])
            Image.open(os.path.join(CROPS, f)).save(os.path.join(OUT, f), quality=92)
            continue
        img, box = r
        img.save(os.path.join(OUT, f), quality=92)
        rep[f[:-4]] = [round(v, 4) for v in box]
    json.dump(rep, open(os.path.join(HERE, "cutboxes.json"), "w"), indent=0)
    print(f"lifted {len(rep)}  failed: {miss}")


if __name__ == "__main__":
    run()
