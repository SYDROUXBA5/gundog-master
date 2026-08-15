#!/usr/bin/env python3
"""Build gundog-master.html by re-skinning the Working Master engine with the
gundog chapter's 58 breeds. The engine (CSS, screens, scoring, leader lines) is
reused verbatim; only the data and the group taxonomy change."""
import base64, io, json, os, re, sys, subprocess
from datetime import datetime
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from breeds import B
from anchors import to_plate, in_photo

ENGINE = "/Users/remidroux/Desktop/HOUND/working-master.html"
OUT = "/Users/remidroux/Desktop/HOUND/gundog-master.html"
CROPS = os.path.join(HERE, "cut")

GROUPNAMES = {"pointer": "Pointer &amp; HPR", "setter": "Setter",
              "spaniel": "Spaniel", "retriever": "Retriever", "water": "Water dog"}
GROUP_KEYS = list(GROUPNAMES)
# families whose coats need the plate dropped a step or the dog vanishes into it
PALE_FAMS = {"corded", "pale"}


def slug(name):
    s = name.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def nums(text):
    """max cm / max kg out of e.g. '21-25 in (53-64 cm)'."""
    m = re.search(r"\(([\d.]+)(?:-([\d.]+))?\s*(cm|kg)\)", text)
    if not m:
        return None
    return float(m.group(2) or m.group(1))


def encode(src, maxw=1150, q=80):
    im = Image.open(os.path.join(CROPS, src + ".jpg")).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build_breeds():
    ids = {b["src"]: slug(b["name"]) for b in B}
    fam_index = {}
    for b in B:
        for f in b["fam"]:
            fam_index.setdefault(f, []).append(ids[b["src"]])

    out = []
    for b in B:
        bid = ids[b["src"]]
        im = Image.open(os.path.join(CROPS, b["src"] + ".jpg"))
        ax, ay = to_plate(im.width, im.height, *in_photo(b["src"], *b["anchor"]))
        confuse = sorted({o for f in b["fam"] for o in fam_index[f] if o != bid})
        rec = {
            "id": bid, "name": b["name"], "group": b["group"],
            "families": b["fam"], "page": b["page"],
            "height": b["height"], "weight": b["weight"],
            "life": b["life"], "origin": b["origin"],
            "maxHeightCm": nums(b["height"]), "maxWeightKg": nums(b["weight"]),
            "otherColors": b.get("colors", []), "varieties": b.get("varieties", []),
            "fieldMarks": b["marks"], "para": b["para"], "tell": b["tell"],
            "say": "", "hook": b["hook"], "confuse": confuse[:8],
            "sources": [b["src"] + ".heic"],
            "mark": b["mark"],
            "anchor": "whole" if b.get("whole") else "feature",
            "ax": ax, "ay": ay, "side": b["side"],
            "img": encode(b["src"]),
        }
        out.append(rec)
    return out


KNOWLEDGE = [
 {"q":"What defines a gundog?","options":["A dog bred to guard livestock","A dog bred to work with hunters to find and retrieve game","A dog bred to race","A dog bred to pull sleds"],"answer":1,
  "explain":"Gundogs are the breeds developed to work alongside hunters — locating, flushing and retrieving game."},
 {"q":"The gundog group splits into which three main working roles?","options":["Trackers, guards and herders","Pointers/setters, spaniels and retrievers","Terriers, hounds and toys","Sled dogs, draught dogs and drovers"],"answer":1,
  "explain":"Pointers and setters locate and indicate game, spaniels flush it, and retrievers collect it once shot."},
 {"q":"What does a pointer or setter do when it finds game?","options":["Grabs it immediately","Freezes and indicates the bird's position","Barks to drive it away","Digs it out of cover"],"answer":1,
  "explain":"They locate the bird and then hold still, indicating its position to the hunter rather than seizing it."},
 {"q":"What is the spaniel's traditional job?","options":["Guarding the bag","Flushing game out of cover","Killing vermin underground","Pointing from a distance"],"answer":1,
  "explain":"Spaniels work close in and push — flush — game out of thick cover so it can be shot."},
 {"q":"What does HPR stand for?","options":["Hound, Pointer, Retriever","Hunt, Point, Retrieve","Herd, Protect, Retrieve","Hold, Push, Release"],"answer":1,
  "explain":"HPR breeds do all three jobs in one dog — hunt, point and retrieve. The Weimaraner, GSP and Vizsla are typical."},
 {"q":"Which coat feature do the water breeds share?","options":["A dense, often oily, water-resistant coat","A single short coat with no undercoat","A hairless body","A coat that sheds completely in summer"],"answer":0,
  "explain":"Water dogs carry dense, often oily double or curly coats that shed water and insulate in cold water."},
 {"q":"Why do gundogs generally make poor guard dogs?","options":["They are too small","They were bred to be biddable and good-natured with people","They cannot bark","They sleep too much"],"answer":1,
  "explain":"Gundogs work in close company with people and were selected for an amiable, trainable temperament."},
 {"q":"Which spaniel has a noticeably domed, rounded skull?","options":["English Cocker Spaniel","Cocker Spaniel (American)","Field Spaniel","Welsh Springer Spaniel"],"answer":1,
  "explain":"The American Cocker has a conspicuously rounded skull and a very abrupt stop; the English Cocker's head is flatter with a squarer muzzle."},
 {"q":"An English Springer Spaniel is liver and white. What colour is a Welsh Springer?","options":["Black and white","Red and white","Solid liver","Blue roan"],"answer":1,
  "explain":"The Welsh Springer is always rich red and white, never liver."},
 {"q":"Which spaniel has a smooth 'rat tail' but ringlets everywhere else?","options":["American Water Spaniel","Irish Water Spaniel","Boykin Spaniel","Sussex Spaniel"],"answer":1,
  "explain":"The Irish Water Spaniel's tail is smooth apart from the base, while the rest of the dog is in dense ringlets."},
 {"q":"Which is the tallest of the spaniels?","options":["Clumber Spaniel","Irish Water Spaniel","Sussex Spaniel","Cocker Spaniel"],"answer":1,
  "explain":"At 20-23 in (51-58 cm) the Irish Water Spaniel is the tallest spaniel."},
 {"q":"Which spaniel is heavy-boned and built low to the ground with a massive broad head?","options":["Field Spaniel","Clumber Spaniel","English Springer Spaniel","German Spaniel"],"answer":1,
  "explain":"The Clumber is the heaviest and lowest-slung spaniel, weighing 55-75 lb (25-34 kg) on short legs."},
 {"q":"Which gundog is the only one that gives tongue while working?","options":["Sussex Spaniel","Gordon Setter","Brittany","Barbet"],"answer":0,
  "explain":"The Sussex Spaniel is the only gundog that barks on the job, and it moves with a distinctive rolling gait."},
 {"q":"The Nederlandse Kooikerhondje uses its tail to do what?","options":["Balance on ice","Lure ducks into a trap by waving it","Signal the handler at distance","Sweep scent from the ground"],"answer":1,
  "explain":"The Dutch Decoy Spaniel waves its white tail to draw curious waterfowl down tunnel traps — 'tolling'."},
 {"q":"Which retriever plays on the shore to lure ducks within range?","options":["Curly-Coated Retriever","Nova Scotia Duck Tolling Retriever","Chesapeake Bay Retriever","Flat-Coated Retriever"],"answer":1,
  "explain":"The Toller performs on the bank to draw — 'toll' — birds into gun range, then retrieves them."},
 {"q":"Which is the smallest of the retrievers?","options":["Labrador Retriever","Nova Scotia Duck Tolling Retriever","Golden Retriever","Curly-Coated Retriever"],"answer":1,
  "explain":"The Toller stands 18-21 in (45-53 cm), well under the other retrievers."},
 {"q":"The Labrador Retriever's ancestors actually came from where?","options":["Labrador","Newfoundland","Scotland","Nova Scotia"],"answer":1,
  "explain":"Despite the name, the breed descends from waterproof-coated dogs bred by fishermen in Newfoundland."},
 {"q":"What is the Labrador's characteristic tail called?","options":["Rat tail","Otter tail","Flag tail","Ring tail"],"answer":1,
  "explain":"The Labrador carries a thick, round, well-haired 'otter' tail with no feathering."},
 {"q":"Which retriever has tight curls over the body but a smooth, short-haired head?","options":["Curly-Coated Retriever","Chesapeake Bay Retriever","Flat-Coated Retriever","Golden Retriever"],"answer":0,
  "explain":"The Curly-Coated Retriever is tightly curled all over except the head, which carries smooth short hair."},
 {"q":"Which is the tallest retriever?","options":["Labrador Retriever","Curly-Coated Retriever","Golden Retriever","Chesapeake Bay Retriever"],"answer":1,
  "explain":"The Curly-Coated Retriever stands 25-27 in (64-69 cm)."},
 {"q":"Which setter is black with chestnut-red points?","options":["English Setter","Gordon Setter","Irish Setter","Irish Red and White Setter"],"answer":1,
  "explain":"The Gordon Setter is the black-and-tan setter — coal black with chestnut-red markings on face, feet and legs."},
 {"q":"What is the name for the English Setter's fine speckled coat pattern?","options":["Roan","Belton","Brindle","Ticking"],"answer":1,
  "explain":"The English Setter's speckling has its own name, belton — blue belton being black flecks on white."},
 {"q":"How do you tell an Irish Red and White Setter from an English Setter?","options":["The Irish is smaller","The Irish has clear-edged patches, not fine speckling","The Irish is always black","The Irish has erect ears"],"answer":1,
  "explain":"The Irish Red and White carries crisp, clearly defined colour patches; the English Setter is finely speckled."},
 {"q":"Which gundog is nicknamed the 'Gray Ghost'?","options":["Slovakian Rough-haired Pointer","Weimaraner","Bracco Italiano","Spinone Italiano"],"answer":1,
  "explain":"The Weimaraner earned the name from its silver-grey coat and its careful, almost stealthy way of working."},
 {"q":"On a Vizsla, what colour is the nose?","options":["Always black","The same colour as the coat","Always pink","Slate blue"],"answer":1,
  "explain":"The Vizsla's nose matches its golden-russet coat — there is no black anywhere on the dog."},
 {"q":"The Vizsla is also known as what?","options":["Hungarian Shorthaired Pointer","Hungarian Wirehaired Griffon","Hungarian Water Dog","Hungarian Setter"],"answer":0,
  "explain":"The Vizsla is the Hungarian Shorthaired Pointer, thought to date back to the 16th century."},
 {"q":"Which coat types does the German Shorthaired Pointer's breed group include?","options":["Only shorthaired","Shorthaired, wirehaired and longhaired","Shorthaired and corded","Wirehaired and curly"],"answer":1,
  "explain":"There are three coat types — wirehaired, longhaired and shorthaired — with the shorthaired by far the best known."},
 {"q":"What is the German Shorthaired Pointer called in its homeland?","options":["Deutsch Drahthaar","Deutsch Kurzhaar","Deutsch Langhaar","Deutscher Wachtelhund"],"answer":1,
  "explain":"Kurzhaar means shorthair; the wirehaired version is the Drahthaar."},
 {"q":"The Pudelpointer is a deliberate cross between which two types?","options":["Poodle and pointer","Poodle and setter","Pointer and spaniel","Poodle and retriever"],"answer":0,
  "explain":"It was bred to combine the poodle's intelligence and coat with the pointer's working ability — hence the curling forelock."},
 {"q":"How do you separate the French Pyrenean Pointer from the French Gascony Pointer?","options":["Colour — one is black","Size and speckle density","Ear shape","Tail length"],"answer":1,
  "explain":"The Gascony is the larger dog with sparser flecking; the Pyrenean is smaller with denser speckling."},
 {"q":"Which French braque is black-marked rather than chestnut?","options":["Auvergne Pointer","Bourbonnais Pointing Dog","Saint Germain Pointer","Ariege Pointing Dog"],"answer":0,
  "explain":"The Braque d'Auvergne has black head markings and black flecking that gives the coat a blue cast."},
 {"q":"The Saint Germain Pointer is distinguished by which pair of features?","options":["Black nose and brown eyes","Pink nose and golden-yellow eyes","Grey nose and blue eyes","Liver nose and amber eyes"],"answer":1,
  "explain":"A pink nose paired with golden-yellow eyes sets the Braque Saint-Germain apart from the other French braques."},
 {"q":"Which breed is known as the Perdiguero de Burgos?","options":["Portuguese Pointer","Spanish Pointer","Spanish Water Dog","Bracco Italiano"],"answer":1,
  "explain":"The Spanish Pointer, originally bred to track deer, is the Perdiguero de Burgos."},
 {"q":"Which Italian gundog has heavy flews and a dewlap that give it a houndlike head?","options":["Spinone Italiano","Bracco Italiano","Lagotto Romagnolo","Cesky Fousek"],"answer":1,
  "explain":"The Bracco Italiano carries well-developed flews and a soft dewlap on a powerful neck."},
 {"q":"Which breed was specifically re-purposed to hunt truffles?","options":["Barbet","Lagotto Romagnolo","Spanish Water Dog","Frisian Water Dog"],"answer":1,
  "explain":"The Lagotto Romagnolo began as a marshland retriever and is now the truffle dog."},
 {"q":"The Old Danish Pointer's local name translates as what?","options":["Old Danish Chicken Dog","Old Danish Marsh Hound","Danish Deer Dog","Danish Farm Pointer"],"answer":0,
  "explain":"Gammel Dansk Hønsehund translates as Old Danish Chicken Dog or Bird Dog."},
 {"q":"Which two breeds are NOT closely related despite their names?","options":["Small and Large Munsterlander","English and Welsh Springer","Irish Setter and Irish Red and White Setter","Cocker and English Cocker"],"answer":0,
  "explain":"The Large Munsterlander is more closely related to the German pointers than to the Small Munsterlander."},
 {"q":"The Stabyhoun is better known in English as what?","options":["Frisian Water Dog","Frisian Pointing Dog","Drentsche Partridge Dog","Dutch Decoy Spaniel"],"answer":1,
  "explain":"The Stabyhoun is the Frisian Pointing Dog, bred by Dutch farmers to track, point and retrieve."},
 {"q":"Which breed's whole face is buried in hair, and is one of Europe's oldest water dogs?","options":["Barbet","Pont-Audemer Spaniel","Spinone Italiano","Cesky Fousek"],"answer":0,
  "explain":"The Barbet's face is profusely covered with hair; it is an ancestor of many other water breeds."},
 {"q":"What is the Frisian Water Dog's most distinctive feature?","options":["A docked tail","A tail carried curled into a ring","A hairless tail","No tail at all"],"answer":1,
  "explain":"The Wetterhoun carries its long tail curled into a ring over the back."},
 {"q":"Which coat pattern belongs to the Blue Picardy Spaniel?","options":["Tan points on brown","Grey-black speckling giving a blue cast","Solid black","Orange and white patches"],"answer":1,
  "explain":"Grey-black speckling over black patches gives the Blue Picardy its blue shade — and it carries no tan."},
 {"q":"Which is the smallest gundog in the group?","options":["Nederlandse Kooikerhondje","Cocker Spaniel","Boykin Spaniel","Brittany"],"answer":1,
  "explain":"At 13-15 in (34-39 cm) the American Cocker Spaniel is the smallest of the gundogs."},
 {"q":"The Brittany is unusual among spaniels because it does what?","options":["Points rather than flushes","Swims underwater","Herds sheep","Hunts at night"],"answer":0,
  "explain":"The Brittany works as a pointer despite the spaniel name, and carries a very high-set, naturally short tail."},
 {"q":"Which breed is the state dog of South Carolina?","options":["American Water Spaniel","Boykin Spaniel","Chesapeake Bay Retriever","Curly-Coated Retriever"],"answer":1,
  "explain":"The Boykin Spaniel, a curly chocolate spaniel bred to work from small boats, is South Carolina's state dog."},
 {"q":"Which of these is the largest gundog by height?","options":["Spinone Italiano","Cocker Spaniel","Brittany","Lagotto Romagnolo"],"answer":0,
  "explain":"The Spinone Italiano stands 23-28 in (58-70 cm), the tallest range in the group."},
 {"q":"Why is the Spinone Italiano an easy walking companion?","options":["It needs almost no exercise","It naturally moves at a slower pace than most gundogs","It cannot walk far","It refuses to run"],"answer":1,
  "explain":"The Spinone is inclined to work at a slightly slower pace than other gundogs, which suits a walking pace."},
]


def main():
    src = open(ENGINE, encoding="utf-8").read()

    breeds = build_breeds()
    print(f"breeds: {len(breeds)}  images: "
          f"{sum(len(b['img']) for b in breeds)/1e6:.1f} MB of base64")

    # ---- data ----
    src = re.sub(r"const BREEDS = \[.*?\n(?=const KNOWLEDGE)",
                 "const BREEDS = " + json.dumps(breeds, ensure_ascii=False) + ";\n",
                 src, count=1, flags=re.S)
    src = re.sub(r"const KNOWLEDGE = \[.*?\n(?=const )",
                 "const KNOWLEDGE = " + json.dumps(KNOWLEDGE, ensure_ascii=False) + ";\n",
                 src, count=1, flags=re.S)

    # ---- group taxonomy ----
    chips = "\n    ".join(
        f'<button class="chip" data-filter="{k}">{v}</button>' for k, v in GROUPNAMES.items())
    src = re.sub(r'<div class="filters".*?</div>',
                 '<div class="filters" role="group" aria-label="Filter breeds">\n'
                 '    <button class="chip on" data-filter="all">All breeds</button>\n    '
                 + chips + "\n  </div>", src, count=1, flags=re.S)

    opts = "".join(f'<option value="{k}">{v}</option>' for k, v in GROUPNAMES.items())
    src = re.sub(r'<select id="browse-group".*?</select>',
                 '<select id="browse-group" aria-label="Filter by group">'
                 '<option value="all">All groups</option>' + opts + "</select>",
                 src, count=1, flags=re.S)

    src = src.replace('const GROUPNAMES={herding:"Herding",guardian:"Guardian",mastiff:"Mastiff type"};',
                      "const GROUPNAMES=" + json.dumps(GROUPNAMES).replace("&amp;", "&") + ";")
    src = src.replace('["herding","guardian","mastiff"]', json.dumps(GROUP_KEYS))
    src = src.replace("--herding:var(--ink); --guardian:var(--ink); --mastiff:var(--ink);",
                      " ".join(f"--{k}:var(--ink);" for k in GROUP_KEYS))
    src = src.replace(".photo-card.herding,.photo-card.guardian,.photo-card.mastiff",
                      ",".join(f".photo-card.{k}" for k in GROUP_KEYS))
    src = src.replace(".photo-card.herding.pale,.photo-card.guardian.pale,.photo-card.mastiff.pale",
                      ",".join(f".photo-card.{k}.pale" for k in GROUP_KEYS))
    src = src.replace(".btile .thumb.herding,.btile .thumb.guardian,.btile .thumb.mastiff",
                      ",".join(f".btile .thumb.{k}" for k in GROUP_KEYS))
    src = src.replace('const PALE=new Set(["white-lgd","corded"]);',
                      "const PALE=new Set(" + json.dumps(sorted(PALE_FAMS)) + ");")

    # ---- naming, counts, chrome ----
    # the ranks were pastoral because the dogs were; a gundog ladder is a shoot day
    src = src.replace(
        'const LEVELS=["Rookie","Kennel Hand","Stockman","Drover","Shepherd",'
        '"Yard Boss","Head Handler","Master Handler","Working Sage","Working Master"]',
        'const LEVELS=["Rookie","Kennel Hand","Beater","Picker-Up","Gun",'
        '"Field Hand","Head Keeper","Master Keeper","Field Sage","Gundog Master"]')
    # the wordmark is split by an <em>, so the plain rename cannot see it
    src = src.replace('<span class="logo-wm">Working <em>Master</em></span>',
                      '<span class="logo-wm">Gundog <em>Master</em></span>')
    src = src.replace("Working Master", "Gundog Master")
    src = src.replace("WORKING MASTER", "GUNDOG MASTER")
    src = src.replace("working-master", "gundog-master")
    src = src.replace("name every working dog on sight", "name every gundog on sight")
    src = src.replace(
        "Breed identification drill for the 98 working dogs — herders, livestock "
        "guardians and mastiff types. A study companion for the Highland Canine "
        "Master Trainer course.",
        "Breed identification drill for the 58 gundogs — pointers, setters, "
        "spaniels, retrievers and water dogs. A study companion for the Highland "
        "Canine Master Trainer course.")
    src = src.replace('id="st-grad">0/98<', f'id="st-grad">0/{len(breeds)}<')
    src = src.replace("All 98 cards", f"All {len(breeds)} cards")
    src = re.sub(r"working dogs\b", "gundogs", src)
    src = re.sub(r"working dog\b", "gundog", src)

    # body copy that names the old taxonomy
    src = src.replace(
        "98 herders, guardians and mastiff types, transcribed from your encyclopedia.",
        f"{len(breeds)} pointers, setters, spaniels, retrievers and water dogs, "
        "transcribed from your encyclopedia.")
    src = src.replace(
        "How herders, guardians and mastiff types work and are built",
        "How pointers, setters, spaniels and retrievers work and are built")
    src = src.replace(
        "/* white livestock guardians and corded coats need the field dropped a step, or the coat",
        "/* white pointers and corded coats need the field dropped a step, or the coat")

    stamp = datetime.now().strftime("%d %b %H:%M")
    src = re.sub(r'<b id="build-stamp">[^<]*</b>',
                 f'<b id="build-stamp">{stamp} · gundog</b>', src)

    open(OUT, "w", encoding="utf-8").write(src)
    print("wrote", OUT, f"{os.path.getsize(OUT)/1e6:.1f} MB")


if __name__ == "__main__":
    main()
