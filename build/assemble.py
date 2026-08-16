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
    return _b64(im, q)


def _b64(im, q):
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


WILD_DIR = os.path.join(HERE, "wild")
WILD_META = json.load(open(os.path.join(HERE, "wild.json"))) \
    if os.path.exists(os.path.join(HERE, "wild.json")) else {}


def wild(src, maxw=760, q=72):
    """The field photograph, pre-cropped to the 4:3 the plate renders it at.

    The plate is the breed standard; this is the dog as it actually looks, which
    is what you have to recognise at the kennel. Credit travels with the pixels
    because these are other people's CC-licensed photographs."""
    meta = WILD_META.get(src)
    path = os.path.join(WILD_DIR, src + ".jpg")
    if not meta or not os.path.exists(path):
        return None
    im = Image.open(path).convert("RGB")
    tw, th = im.width, round(im.width * 3 / 4)
    if th > im.height:                       # too short: crop width instead
        th, tw = im.height, round(im.height * 4 / 3)
    im = im.crop(((im.width - tw) // 2, (im.height - th) // 2,
                  (im.width - tw) // 2 + tw, (im.height - th) // 2 + th))
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    return {"by": meta["by"], "lic": meta["lic"], "licUrl": meta["licUrl"],
            "src": meta["src"], "img": _b64(im, q)}


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
            "say": b.get("say", ""), "hook": b["hook"], "confuse": confuse[:8],
            "sources": [b["src"] + ".heic"],
            "mark": b["mark"],
            "anchor": "whole" if b.get("whole") else "feature",
            "ax": ax, "ay": ay, "side": b["side"],
            "img": encode(b["src"]),
        }
        w = wild(b["src"])
        if w:
            rec["wild"] = w
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
 {"q":"You meet a tall, lean, short-coated gundog with a level tail. Which group?","options":["Spaniel","Pointer or HPR","Retriever","Water dog"],"answer":1,
  "explain":"Leggy, square and short-coated is the pointer outline. A setter has the same build under a long silky coat."},
 {"q":"What separates a setter from a pointer at a glance?","options":["The setter is much smaller","The setter's long silky feathered coat","The setter has erect ears","The setter has a curled tail"],"answer":1,
  "explain":"They share the job and roughly the build; the setter carries a long flat silky coat with heavy feathering."},
 {"q":"Which feature most reliably marks a spaniel?","options":["A curled tail","Long, low-set, heavily fringed ears","Webbed feet","A black nose"],"answer":1,
  "explain":"Spaniel ears hang low and long with heavy fringe. Retriever ears are shorter and set higher."},
 {"q":"A square, solid dog with a thick straight tail and a broad kind head is most likely which group?","options":["Retriever","Setter","Water dog","Pointer"],"answer":0,
  "explain":"Heavier than a pointer, shorter-eared than a spaniel, with a thick tail — the Labrador's otter tail is the type."},
 {"q":"A gundog in tight curls or hanging cords belongs to which group?","options":["Setter","Water dog","Pointer","Retriever"],"answer":1,
  "explain":"Coat texture is the water dog's tell: curls, wool or cords, never a straight jacket."},
 {"q":"Which breed is named a spaniel but is built and coated like a water dog?","options":["Sussex Spaniel","Irish Water Spaniel","Field Spaniel","Welsh Springer Spaniel"],"answer":1,
  "explain":"The Irish Water Spaniel carries dense ringlets on a tall square frame — a water dog in all but name."},
 {"q":"A wirehaired gundog has a harsh flat coat, not curls. Which group is it likely in?","options":["Water dog","Pointer or HPR","Retriever","Spaniel"],"answer":1,
  "explain":"Harsh flat wire belongs to the HPR breeds — the Spinone, the Griffon, the Cesky Fousek. Curls and cords mean water dog."},
 {"q":"Compared with a spaniel, a retriever is generally...","options":["Smaller with longer ears","Bigger and squarer with shorter, higher-set ears","Identical in build","Lower to the ground"],"answer":1,
  "explain":"Size, a squarer outline and shorter higher ears separate retriever from spaniel."},
]


# The five groups look alike breed by breed but differ by JOB, and the job shows
# in the build. This screen teaches that shape before any breed name does.
GROUP_GUIDE = [
 {"key": "pointer", "name": "Pointer &amp; HPR", "job": "Find the bird and freeze",
  "one": "Tall, lean and short-coated. Built to quarter a field all day.",
  "marks": [["Coat", "Short and tight — you can see the muscle under it. The wirehaired ones are harsh and flat, never curly."],
            ["Build", "Leggy and square, deep chest, tucked belly. The most athletic outline in the group."],
            ["Head", "Long clean muzzle, high-set ears lying flat to the cheek."],
            ["Tail", "Carried level with the back, or docked short."]],
  "vs": "If it is tall and lean but wearing a long silky coat, it is a SETTER, not a pointer."},
 {"key": "setter", "name": "Setter", "job": "Find the bird and freeze",
  "one": "A pointer's height and job, wearing a long silky feathered coat.",
  "marks": [["Coat", "Long, flat and silky, with heavy feathering on chest, legs and tail."],
            ["Build", "Tall and elegant — as leggy as a pointer under all that hair."],
            ["Head", "Long and lean, ears set low and hanging in a fold."],
            ["Tail", "Carried level like a flag, thickly feathered underneath."]],
  "vs": "Same job as a pointer, different coat. Against a SPANIEL: a setter is far taller and longer in the leg."},
 {"key": "spaniel", "name": "Spaniel", "job": "Flush the bird out of cover",
  "one": "Compact and low, with long low-set ears framing the face.",
  "marks": [["Ears", "The giveaway — long, low-set and heavily fringed, hanging well below the jaw."],
            ["Build", "Small to medium and compact; body longer than the legs are tall."],
            ["Coat", "Medium, wavy or flat, feathered on legs and belly."],
            ["Tail", "Carried low, often docked, feathered underneath."]],
  "vs": "Ear set is the test: a spaniel's ears hang low and long; a retriever's are shorter and set higher."},
 {"key": "retriever", "name": "Retriever", "job": "Fetch the shot bird back",
  "one": "Solid, square and powerful, with a thick straight tail and a kind broad head.",
  "marks": [["Build", "Sturdy and balanced — heavier through the body than a pointer, shorter-coupled than a spaniel."],
            ["Head", "Broad skull, moderate stop, open friendly expression."],
            ["Coat", "Dense and weatherproof, with a real undercoat. Straight or wavy, never corded."],
            ["Tail", "Thick at the base and carried straight — the Labrador's 'otter' tail is the type."]],
  "vs": "Against a SPANIEL: bigger, squarer, shorter ears. Against a POINTER: heavier and less leggy."},
 {"key": "water", "name": "Water dog", "job": "Work and retrieve in water",
  "one": "Read the coat: curls, cords or wool — never a straight jacket.",
  "marks": [["Coat", "Tight curls, dense wool, or long hanging cords. Often clipped, which is a grooming choice, not the breed."],
            ["Build", "Square and agile, medium-sized, built to swim rather than to gallop."],
            ["Head", "Frequently buried in coat — topknots, beards and moustaches are common."],
            ["Tail", "Varies a lot: plumed, ringed, or shorn as part of a working clip."]],
  "vs": "Careful: the Irish Water Spaniel is named a spaniel but is built and coated like a water dog."},
]

DECISION = [
 ["Curls, cords or wool?", "Water dog", "Poodle, Lagotto, Portuguese Water Dog"],
 ["Long low ears, compact and low-slung?", "Spaniel", "Cocker, Springer, Clumber"],
 ["Tall and lean under a long silky feathered coat?", "Setter", "English, Irish, Gordon"],
 ["Tall and lean in a short tight coat?", "Pointer &amp; HPR", "GSP, Weimaraner, Vizsla"],
 ["Solid and square, thick straight tail, broad kind head?", "Retriever", "Labrador, Golden, Chesapeake"],
]


def groups_screen():
    """Markup + script for the group primer, injected into the cloned engine."""
    cards = []
    for g in GROUP_GUIDE:
        rows = "".join(
            f'<div class="gg-row"><span class="gg-k">{k}</span><span>{v}</span></div>'
            for k, v in g["marks"])
        cards.append(
            f'<article class="gg-card" data-gg="{g["key"]}">'
            f'<header class="gg-head"><h3>{g["name"]}</h3>'
            f'<span class="gg-job">{g["job"]}</span></header>'
            f'<p class="gg-one">{g["one"]}</p>'
            f'<div class="gg-rows">{rows}</div>'
            f'<p class="gg-vs"><b>Telling it apart</b> {g["vs"]}</p>'
            f'<div class="gg-eg" data-eg="{g["key"]}"></div></article>')

    steps = "".join(
        f'<li><span class="gg-q">{q}</span>'
        f'<span class="gg-a">{a}</span>'
        f'<span class="gg-ex">{ex}</span></li>' for q, a, ex in DECISION)

    html = (
      '<section id="groups" class="screen" hidden>\n'
      '  <div class="screen-head"><button class="back" data-nav="home" '
      'aria-label="Back to home">←</button><span class="qcount">The five kinds</span></div>\n'
      '  <p class="gg-intro">Every gundog does one of three jobs — find the bird, '
      'flush it, or fetch it — and the job is written into the body. Learn the five '
      'shapes first and most breeds place themselves.</p>\n'
      f'  <ol class="gg-tree">{steps}</ol>\n'
      f'  <div class="gg-grid">{"".join(cards)}</div>\n'
      '</section>\n')

    css = (
      "\n/* ===== the five kinds ===== */\n"
      ".gg-intro{max-width:64ch;color:var(--graphite);font-size:14.5px;line-height:1.6;margin:0 0 var(--s5)}\n"
      ".gg-tree{list-style:none;counter-reset:gg;margin:0 0 var(--s6);padding:0;"
      "border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:var(--surface)}\n"
      ".gg-tree li{counter-increment:gg;display:grid;grid-template-columns:auto 1fr auto;"
      "gap:var(--s2) var(--s3);align-items:baseline;padding:10px var(--s4);border-top:1px solid var(--line-soft)}\n"
      ".gg-tree li:first-child{border-top:0}\n"
      ".gg-tree li::before{content:counter(gg);font:600 11px/1 var(--f-data);color:var(--graphite)}\n"
      ".gg-q{font-size:14px}\n"
      ".gg-a{font:600 12px/1 var(--f-mark);letter-spacing:.1em;text-transform:uppercase;color:var(--azure-ink)}\n"
      ".gg-ex{grid-column:2/4;font-size:11.5px;color:var(--graphite)}\n"
      ".gg-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--s4)}\n"
      ".gg-card{border:1px solid var(--line);border-radius:var(--r);background:var(--surface);padding:var(--s4)}\n"
      ".gg-head{display:flex;align-items:baseline;justify-content:space-between;gap:var(--s2);flex-wrap:wrap}\n"
      ".gg-head h3{font-family:var(--f-title);font-size:15px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}\n"
      ".gg-job{font-size:11.5px;color:var(--graphite)}\n"
      ".gg-one{margin:var(--s2) 0 var(--s3);font-size:14px;line-height:1.5}\n"
      ".gg-rows{border-top:1px solid var(--line-soft)}\n"
      ".gg-row{display:grid;grid-template-columns:74px 1fr;gap:var(--s3);padding:7px 0;"
      "border-bottom:1px solid var(--line-soft);font-size:13px;line-height:1.45}\n"
      ".gg-k{font:600 10.5px/1.5 var(--f-mark);letter-spacing:.09em;text-transform:uppercase;color:var(--graphite)}\n"
      ".gg-vs{margin:var(--s3) 0 0;font-size:12.5px;line-height:1.5;color:var(--graphite)}\n"
      ".gg-vs b{color:var(--ink);font-weight:600}\n"
      ".gg-eg{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--s2);margin-top:var(--s3)}\n"
      ".gg-eg figure{margin:0}\n"
      ".gg-eg img{display:block;width:100%;aspect-ratio:4/3;object-fit:contain;"
      "background:var(--field);border:1px solid var(--line);border-radius:var(--r)}\n"
      ".gg-eg figcaption{font-size:10.5px;color:var(--graphite);margin-top:3px;line-height:1.3}\n")

    js = (
      "\n/* the five kinds: three example plates per group, taken from the data */\n"
      "function renderGroups(){\n"
      "  document.querySelectorAll('.gg-eg').forEach(box=>{\n"
      "    const g=box.dataset.eg;\n"
      "    const picks=BREEDS.filter(b=>b.group===g).slice(0,3);\n"
      "    box.innerHTML=picks.map(b=>`<figure><img src=\"${b.img}\" alt=\"${esc(b.name)}\" "
      "loading=\"lazy\"><figcaption>${esc(b.name)}</figcaption></figure>`).join('');\n"
      "  });\n"
      "}\n")

    return html, css, js


def inject_groups(src):
    html, css, js = groups_screen()
    src = src.replace('<section id="knowledge" class="screen" hidden>',
                      html + '<section id="knowledge" class="screen" hidden>', 1)
    src = src.replace("</style>", css + "</style>", 1)
    src = src.replace('const SCREENS=["home"',
                      'const SCREENS=["groups","home"', 1)
    src = src.replace('if(id==="home")renderHome();',
                      'if(id==="home")renderHome();if(id==="groups")renderGroups();', 1)
    src = src.replace('else if(m==="browse"){renderBrowse();show("browse")}',
                      'else if(m==="groups"){renderGroups();show("groups")}\n'
                      '  else if(m==="browse"){renderBrowse();show("browse")}', 1)
    src = src.replace('<button class="mode-card" data-mode="knowledge">',
                      '<button class="mode-card" data-mode="groups">\n'
                      '      <div class="ic gold"><svg viewBox="0 0 24 24">'
                      '<path d="M3 6h7M3 12h7M3 18h7M14 6h7M14 12h7M14 18h7"/></svg></div>\n'
                      '      <h3>The five kinds</h3><p>Pointer, setter, spaniel, retriever, '
                      'water dog — what separates them, before the names.</p>\n'
                      '    </button>\n'
                      '    <button class="mode-card" data-mode="knowledge">', 1)
    src = src.replace("/* ================= modes wiring ================= */", js +
                      "/* ================= modes wiring ================= */", 1)
    return src


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

    src = inject_groups(src)

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

    # ---- the group drill ----
    # Breed ID can only ever test the 58 dogs in the book. Naming the KIND
    # transfers to any gundog that walks in, and it is the first cut a handler
    # actually makes on sight, so it earns its own mode. It reuses the flash
    # screen wholesale; only the four buttons and the right-answer test change.
    src = src.replace(
        '    <button class="mode-card" data-mode="knowledge">',
        '''    <button class="mode-card" data-mode="group">
      <div class="ic blue"><svg viewBox="0 0 24 24"><path d="M3 6h7v5H3zM14 6h7v5h-7zM3 15h7v3H3zM14 15h7v3h-7z"/></svg></div>
      <h3>Which kind?</h3><p>Pointer, setter, spaniel, retriever or water dog — the first cut you make on sight.</p>
    </button>
    <button class="mode-card" data-mode="knowledge">''', 1)

    src = src.replace(
        'else if(m==="knowledge")startKnowledge();',
        'else if(m==="group")startGroup();\n  else if(m==="knowledge")startKnowledge();', 1)

    src = src.replace(
        "function comboMeter(el,combo){",
        '''const GROUP_OPTS=Object.keys(GROUPNAMES).map(g=>({gid:g,name:GROUPNAMES[g]}));
function startGroup(){
  const P=pool();
  if(P.length<5){toast("Need a few more breeds — widen the filter.");return}
  const n=Math.min(20,P.length);
  F={label:"which kind",grp:true,rev:false,qs:shuffle([...P]).slice(0,n),
     i:0,ok:0,missed:[],combo:0,best:0,xp:0,answered:false};
  show("flash");renderFlash();
}
function comboMeter(el,combo){''', 1)

    src = src.replace(
        '    $("flash-prompt").textContent="Who\'s this?";',
        '    $("flash-prompt").textContent=F.grp?"Which kind of gundog?":"Who\'s this?";', 1)

    src = src.replace(
        '  const box_=$("flash-opts");box_.innerHTML="";\n'
        '  F.opts.forEach((o,i)=>{const btn=document.createElement("button");btn.className="opt";',
        '  const box_=$("flash-opts");box_.innerHTML="";\n'
        '  if(F.grp)F.opts=GROUP_OPTS.slice();\n'
        '  F.opts.forEach((o,i)=>{const btn=document.createElement("button");btn.className="opt";', 1)

    src = src.replace(
        '  const b=F.qs[F.i],chosen=F.opts[i],right=chosen.id===b.id;\n'
        '  document.querySelectorAll("#flash-opts .opt").forEach((btn,j)=>{btn.disabled=true;\n'
        '    if(F.opts[j].id===b.id)btn.classList.add("correct");',
        '  const b=F.qs[F.i],chosen=F.opts[i],\n'
        '        right=F.grp?chosen.gid===b.group:chosen.id===b.id;\n'
        '  document.querySelectorAll("#flash-opts .opt").forEach((btn,j)=>{btn.disabled=true;\n'
        '    if(F.grp?F.opts[j].gid===b.group:F.opts[j].id===b.id)btn.classList.add("correct");', 1)

    # naming the kind is not naming the dog, so it must not graduate a breed
    src = src.replace('if(S.run[b.id]>=3&&!S.graduated[b.id]){',
                      'if(!F.grp&&S.run[b.id]>=3&&!S.graduated[b.id]){', 1)

    # A miss in group mode picks a GROUP, not a breed, so the confused-pair stat
    # would key on an undefined id and the side-by-side VS card would be handed
    # something with no fieldMarks, no height and no group -- which threw on
    # groupName(undefined).toLowerCase(). Both paths are breed-vs-breed by
    # nature, so group mode skips them and reveals the breed card instead:
    # what you needed to learn is which dog it was and which kind it belongs to.
    src = src.replace(
        '    const key=[b.id,chosen.id].sort().join("|");\n'
        '    S.pairs[key]=(S.pairs[key]||0)+1;',
        '    if(!F.grp){const key=[b.id,chosen.id].sort().join("|");\n'
        '      S.pairs[key]=(S.pairs[key]||0)+1;}', 1)

    src = src.replace(
        '    revealHTML=F.duel\n'
        '      ? `<div class="reveal">${duelTellsHTML(b,chosen)}</div>`+vsHTML(chosen,b)\n'
        '      : vsHTML(chosen,b);',
        '    revealHTML=F.grp\n'
        '      ? `<div class="reveal">${breedCardHTML(b,true)}</div>`\n'
        '      : F.duel\n'
        '      ? `<div class="reveal">${duelTellsHTML(b,chosen)}</div>`+vsHTML(chosen,b)\n'
        '      : vsHTML(chosen,b);', 1)

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
