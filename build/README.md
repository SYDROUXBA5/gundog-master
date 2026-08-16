# Gundog Master — build pipeline

Builds `../gundog-master.html` by re-skinning the **Working Master** engine
(`../working-master.html`) with the gundog chapter. The engine is reused
untouched — CSS, screens, scoring, streaks, leader lines. Only the data and the
group taxonomy change.

Source photos: `~/Desktop/GUNDOG/` (59 HEIC pages → 58 breeds + 1 chapter intro).

## Run order

```bash
python3 crop.py       # page photo -> hero dog region      (hi/ -> crops/)
python3 cutout.py     # lift the dog off the page          (crops/ -> cut/)
python3 anchors.py    # proof sheet of the leader-line dots (proof.jpg)
python3 assemble.py   # -> ../gundog-master.html
```

`crop.py` and `cutout.py` expect `hi/` — the pages converted at 2600px:

```bash
cd ~/Desktop/GUNDOG && for f in *.heic; do sips -s format jpeg -Z 2600 "$f" --out "hi/${f%.heic}.jpg"; done
```

## Why the dog is cut out of the page

The printed captions and the intro paragraph sit inside any rectangle that
contains the dog, and several of them **name the breed** — which hands the
student the answer on a flashcard. So `cutout.py` masks the animal and
composites it onto flat paper, erasing every glyph outside its silhouette.

Six pages defeat the mask (white or black coats that barely separate from white
paper) and ship their plain crop instead; they are listed in `assemble.py`'s
fallback set, and their remaining callouts are descriptive, never naming.

## Marks: `whole` vs leader line

A leader line only earns its place on a **localized** feature — a nose, a tail,
a stop, a forelock. For whole-animal tells (coat colour, coat texture, build)
the engine's label-only `whole` mode is used, which needs no coordinates and
therefore cannot point at the wrong thing. 37 breeds use `whole`, 21 carry a
leader.

Leader anchors are pinned by hand in `crops/` space in `breeds.py`
(`anchor=(fx,fy)`); automatic subject detection kept swallowing caption text.
`anchors.py` re-expresses them against the cut-out via `cutboxes.json`, then
into plate space. **Always eyeball `proof.jpg` after touching an anchor** — the
working-master build once shipped every leader line invisible.

## Field photos (`wild`)

Each card pairs the book plate with a real photograph — the plate teaches the
standard, the field photo teaches what you actually meet. `wild.py` fetches one
per breed from Wikimedia Commons, `wildfix.py` re-fetches the bad ones, and the
author/licence/source are stored alongside the pixels and shown on the **reveal
only** (the Commons filename names the breed and would give the question away).

Only free licences are accepted: CC BY, CC BY-SA, CC0, public domain.

**Automated picking cannot be trusted.** The first pass returned a Goldendoodle
for "Standard Poodle", PSF clipart for the American Water Spaniel, and the same
costumed toy poodle for two different breeds. The guards that fixed it are in
`wildfix.py`: require the filename to actually name the breed (`MUST`), block
crossbreed tokens (`CROSS`), reject drawings and clipart (`ART`), reject
sleeping/close-up shots (`DEAD`), and refuse a file already used by another
breed. **Always render the contact sheet and look at all 58** — a wrong photo
teaches the wrong dog, which is worse than no photo.

## Cleaning the plates (`clean.py`) — read this before touching it

Three approaches were tried. Two failed, and they failed the same way, so the
working rule is worth stating plainly:

**Never mask or cut the dog out. Erase the page around it.**

Most gundogs are white-and-liver or white-and-orange, and a white chest is the
same tone as white paper. Any "keep the pixels that differ from paper" rule
therefore amputates the pale half of the animal — both cut-out attempts produced
spaniels with no legs and setters with no chest.

What works, in order:

1. **Separate type from dog by stroke width, not position.** A caption stroke is
   a few pixels thick; a leg is fifty. Erasing every thin stroke *anywhere*
   catches captions printed hard against the dog, which an "erase what is far
   from the dog" rule can never reach — the body absorbs the ground shadow the
   dog stands in, and captions inside that shadow read as part of the animal.
2. **Only erase small leftovers.** "Ink that is not the body" is too blunt on its
   own: an ear or a raised head that the opening separated from the trunk is
   exactly that, and painting it out beheads the dog. This is what happened to
   the Pont-Audemer Spaniel.
3. **Flatten the background to a locally estimated page tone,** not one flat
   colour. These are photographs of a book under a lighting gradient; a single
   fill value leaves visible ghost rectangles wherever type used to be.

Twelve plates print a neighbouring breed, a strip of puppies, a chapter header
or the table hard against the dog. No rule distinguishes those from the animal,
because they genuinely are in frame. Their frames are set by hand in `HAND_BOX` /
`HAND_TRIM`, read off a decile grid, and the cleaner is not allowed to re-crop
them.

**Always render the QC contact sheets and look at all 58.** Every failure in this
pipeline was invisible in the numbers and obvious in the picture.

## The five kinds

`GROUP_GUIDE` and `DECISION` in `assemble.py` drive a screen that teaches what
separates pointer, setter, spaniel, retriever and water dog — job, build, ears,
coat, tail, plus a five-step decision tree and three example plates per group.
`inject_groups()` splices the screen, its CSS and its render function into the
cloned engine. Eight of the knowledge questions drill the same distinctions.

## Adding the next chapter

Copy this folder, swap `breeds.py` (data + `KNOWLEDGE` lives in `assemble.py`),
and update `GROUPNAMES` / `PALE_FAMS` at the top of `assemble.py`. Everything
else carries over.
