# -*- coding: utf-8 -*-
"""Gundog breed data. Specs are reference facts off the page; all prose is written here."""

# src, name, group, families, page, height, weight, life, origin, otherColors,
# varieties, fieldMarks, para, tell, hook, mark, anchor(fx,fy), side
B = [
dict(src="IMG_4338", name="Cocker Spaniel", group="spaniel",
  fam=["uk-spaniel","cocker"], page=222,
  height="13-15 in (34-39 cm)", weight="15-31 lb (7-14 kg)", life="12-15 years",
  origin="USA", colors=["Any color"],
  marks=["Conspicuously rounded head","Pronounced stop","Large, round eyes",
         "Low-set ears fringed with long, silky hair","Sturdy, compact body",
         "Long, wavy coat"],
  para="The American cocker is the smallest of the gundogs and the most heavily "
       "coated — a domed skull, a very abrupt stop and a curtain of silky ear "
       "fringe that reaches well below the jaw. It keeps real speed and stamina "
       "under all that hair and still works as a gundog, though most now live as "
       "pets. The breed can tend toward shyness, so early socialising matters.",
  tell="Domed round skull with an abrupt stop, and ear fringe hanging past the jaw",
  hook="The DOME and the drapes — roundest head of any gundog.",
  mark="ROUNDED SKULL", anchor=(0.6,0.4), side="l"),

dict(src="IMG_4339", name="English Cocker Spaniel", group="spaniel",
  fam=["uk-spaniel","cocker"], page=222,
  height="15-16 in (38-41 cm)", weight="29-33 lb (13-15 kg)", life="12-15 years",
  origin="UK", colors=["Any color"],
  marks=["Square muzzle with moderate flews","Black saddle","Ears fringed with long, wavy hair",
         "Feathering on tail","Long, silky blue-roan coat"],
  para="Once the 'cocking spaniel', named for the woodcock it flushed. It is "
       "longer in the muzzle and flatter in the skull than its American cousin, "
       "and noticeably smaller than the English Springer. Show lines are heavier "
       "and sturdier than working lines; both make excellent companions.",
  tell="Square muzzle and a flat skull — no dome, unlike the American Cocker",
  hook="English = SQUARE head. American = round head.",
  mark="SQUARE MUZZLE", anchor=(0.95,0.36), side="l"),

dict(src="IMG_4337", name="German Spaniel", group="spaniel",
  fam=["euro-spaniel","roan"], page=223,
  height="17-21 in (44-53 cm)", weight="40-55 lb (18-25 kg)", life="12-14 years",
  origin="Germany", colors=["Red","Brown","Red roan"],
  marks=["Brown saddle","Short, fine, brown coat on head","Medium-brown eyes with kind expression",
         "Lightly feathered, drop ears","Dense, wavy, brown-roan coat","Spoon-shaped feet"],
  para="A powerful water retriever with masses of stamina, happiest when it is "
       "working. The coat is the giveaway: a dense wavy brown roan over the body "
       "with a solid brown saddle, and short fine hair on the head. It will live "
       "outdoors but does better indoors with a family.",
  tell="Brown roan body under a solid brown saddle, with a short-haired brown head",
  hook="Roan coat, solid saddle, PLAIN head — three coats on one dog.",
  say="DOYT-cher VAKH-tel-hoont",
  mark="BROWN SADDLE", whole=True, anchor=(0.55,0.26), side="l"),

dict(src="IMG_4341", name="Boykin Spaniel", group="spaniel",
  fam=["curly-water"], page=224,
  height="14-18 in (36-46 cm)", weight="24-40 lb (11-18 kg)", life="14-16 years",
  origin="US", colors=["Liver"],
  marks=["Shorter hair on face","Traditionally docked tail","Distinctive, oval, brown eyes",
         "Curly, dark chocolate coat","Compact, round feet"],
  para="The state dog of South Carolina — a curly chocolate spaniel bred to work "
       "out of small boats. It is easy-going, biddable and good with children and "
       "other dogs, and its curly coat needs regular grooming. White hair on the "
       "chest and toes is permitted.",
  tell="Solid dark chocolate curls on a compact spaniel, with a docked tail",
  hook="Boykin = BOAT dog in chocolate curls.",
  say="BOY-kin",
  mark="CHOCOLATE CURLS", whole=True, anchor=(0.46,0.44), side="r"),

dict(src="IMG_4340", name="Clumber Spaniel", group="spaniel",
  fam=["pale","uk-spaniel","heavy"], page=225,
  height="17-20 in (43-51 cm)", weight="55-75 lb (25-34 kg)", life="10-12 years",
  origin="France", colors=[],
  marks=["Broad head","Dark amber eyes","Broad, deep muzzle with well-defined stop",
         "Large, drop ears","Heavy-boned, firm body, low to the ground","Short legs",
         "Long, plain white coat with orange markings","Wide, deep chest","Large, round feet"],
  para="The most solidly built spaniel of them all — heavy-boned, low to the "
       "ground and much longer than it is tall, with a massive broad head. The "
       "coat is long and plain white with orange markings. Calm and steady enough "
       "that it moved easily from gundog work to family life.",
  tell="Massive white body slung low on short legs — the heaviest spaniel built",
  hook="A spaniel built like a coffee table: LOW, LONG, WHITE.",
  say="KLUM-ber",
  mark="LOW HEAVY BODY", whole=True, anchor=(0.45,0.45), side="r"),

dict(src="IMG_4336", name="Field Spaniel", group="spaniel",
  fam=["uk-spaniel"], page=227,
  height="17-18 in (44-46 cm)", weight="40-55 lb (18-25 kg)", life="10-12 years",
  origin="UK", colors=["Black","Roan"],
  marks=["Moderate stop","Long body relative to leg length","Light feathering on underside of tail",
         "Liver-colored nose","White mark on chest","Moderately long, liver coat",
         "Feathering on back of legs"],
  para="A cross of the English Cocker and the Sussex Spaniel, built for retrieving "
       "from water and heavy cover. It is longer in the body than it is tall, with "
       "a moderately long liver coat and a matching liver nose. Docile but very "
       "high-energy — it needs a job.",
  tell="Long liver body on moderate legs, with a liver nose and a white chest fleck",
  hook="Field = long LIVER body, liver nose. Sussex is the golden one.",
  mark="LIVER COAT", whole=True, anchor=(0.48,0.36), side="l"),

dict(src="IMG_4342", name="Sussex Spaniel", group="spaniel",
  fam=["uk-spaniel","heavy"], page=224,
  height="15-16 in (38-41 cm)", weight="40-51 lb (18-23 kg)", life="12-15 years",
  origin="UK", colors=[],
  marks=["Hazel eyes under wrinkled brow","Long, rich, golden-liver coat",
         "Body length exceeds leg length","Pendant ears covered with long, silky hair",
         "Shorter hair on face","Feathering on chest","Round feet with feathering between toes"],
  para="Distinctive twice over: it is the only gundog that gives tongue while "
       "working, and it moves with a rolling gait unlike anything else in the "
       "group. The coat is a rich golden liver, and the wrinkled brow over hazel "
       "eyes gives it a permanently frowning expression that belies a cheerful nature.",
  tell="Rich golden-liver coat and a frowning, wrinkled brow on a long, low body",
  hook="The one that FROWNS and the only one that barks on the job.",
  mark="GOLDEN-LIVER COAT", whole=True, anchor=(0.45,0.38), side="l"),

dict(src="IMG_4343", name="English Springer Spaniel", group="spaniel",
  fam=["uk-spaniel","springer"], page=226,
  height="18-22 in (46-56 cm)", weight="40-51 lb (18-23 kg)", life="12-14 years",
  origin="UK", colors=["Black and white"],
  marks=["Pronounced stop","Almond-shaped, dark hazel eyes","Pendant ears set at eye level",
         "Weather-resistant, thick, straight, liver and white coat",
         "Well-feathered tail, carried below level of back","Liver freckling on legs",
         "Heavily feathered chest","Well-rounded, compact feet"],
  para="The classic flushing gundog — named for its job of springing birds into "
       "the air. Bigger and leggier than the cockers, with a thick weather-resistant "
       "liver-and-white coat and heavy freckling down the legs. Bright, biddable "
       "and highly sensitive; harsh handling backfires badly.",
  tell="Liver-and-white, taller and leggier than a cocker, with freckled legs",
  hook="SPRINGER springs the birds — the tall liver-and-white one.",
  mark="LIVER & WHITE", whole=True, anchor=(0.52,0.36), side="l"),

dict(src="IMG_4345", name="Welsh Springer Spaniel", group="spaniel",
  fam=["uk-spaniel","springer"], page=228,
  height="18-19 in (46-48 cm)", weight="35-51 lb (16-23 kg)", life="12-15 years",
  origin="UK", colors=[],
  marks=["Finer head than English Springer Spaniel","Low-set, lightly feathered, vine-leaf-shaped ears",
         "Brown nose","Long, muscular neck","Naturally straight, soft, rich red and white coat",
         "Feathering on chest","Feathering above hock","Round, catlike feet"],
  para="A close cousin of the English Springer but always red and white, never "
       "liver. The head is finer, and the ears are small, low-set and shaped like "
       "vine leaves. Jolly and affectionate, though inclined to wander — early "
       "recall training is essential.",
  tell="Rich RED and white — never liver — with small vine-leaf ears",
  hook="Wales = RED dragon, red-and-white dog. England's springer is liver.",
  mark="RED & WHITE", whole=True, anchor=(0.50,0.34), side="l"),

dict(src="IMG_4344", name="American Water Spaniel", group="spaniel",
  fam=["curly-water"], page=229,
  height="15-18 in (38-45 cm)", weight="26-46 lb (12-21 kg)", life="10-12 years",
  origin="USA", colors=["Chocolate"],
  marks=["Broad head","Ears covered with curly hair","Light brown eyes",
         "Tight, liver curls, oily to touch","Smooth hair on face","Moderate feathering along tail",
         "Moderately feathered legs"],
  para="Bred around the Great Lakes as an all-round hunting and water dog, sized "
       "and built to work off a boat as easily as ashore. The tight oily liver "
       "curls come down from Irish Water Spaniel and Curly-Coated Retriever "
       "ancestry. A looser-curled version is called the Marcel coat.",
  tell="Tight oily liver curls on a mid-sized spaniel with a smooth face",
  hook="Boat-sized curls: smaller than the Irish, bigger than a Boykin.",
  mark="TIGHT LIVER CURLS", whole=True, anchor=(0.42,0.42), side="r"),

dict(src="IMG_4346", name="Irish Water Spaniel", group="spaniel",
  fam=["curly-water"], page=228,
  height="20-23 in (51-58 cm)", weight="44-66 lb (20-30 kg)", life="10-12 years",
  origin="Ireland", colors=[],
  marks=["Broad, level back","Nose matches coat color","Smoother hair on face",
         "Smooth hair on throat forms V-shaped patch","Naturally oily, dense coat",
         "Smooth tail except at base","Puce-liver coat forms dense ringlets",
         "Large, round feet well covered with hair"],
  para="The tallest of the spaniels and the clown of the family. Its puce-liver "
       "coat is virtually waterproof and forms dense ringlets everywhere except "
       "the face and the tail, which is smooth — the famous 'rat tail'. Its "
       "enthusiasm for freezing water earned it the nickname Bogdog.",
  tell="Ringlets everywhere except a smooth 'rat tail' and a smooth face",
  hook="Curls all over, RAT TAIL bare — only this dog does that.",
  mark="SMOOTH RAT TAIL", anchor=(0.06,0.55), side="r"),

dict(src="IMG_4353", name="Pont-Audemer Spaniel", group="spaniel",
  fam=["french-spaniel","curly-water"], page=235,
  height="20-23 in (51-58 cm)", weight="40-53 lb (18-24 kg)", life="12-14 years",
  origin="France", colors=["Brown"],
  marks=["Rounded skull with topknot of curly hair","Long, slightly pointed muzzle",
         "Small, dark amber eyes","Drop ears covered with long, silky hair",
         "Deep, broad chest reaches elbows","Curly, disheveled-looking brown coat with gray and brown mottlings",
         "Tail slightly curved with lighter-colored tip","Round feet with long, curly hair between toes"],
  para="A French pointer-retriever specialising in water and swampland, probably "
       "with Irish Water Spaniel somewhere behind it. It came within a hair of "
       "extinction in the 20th century and survives in small numbers. The mottled "
       "brown-and-grey curly coat sits under a distinct curly topknot.",
  tell="Curly topknot over a mottled grey-and-brown dishevelled coat",
  hook="The French water spaniel with a TOPKNOT and permanent bed-hair.",
  say="pon-tohd-MAIR",
  mark="CURLY TOPKNOT", anchor=(0.8,0.42), side="l"),

dict(src="IMG_4360", name="Nederlandse Kooikerhondje", group="spaniel",
  fam=["pale","dutch","red-white"], page=238,
  height="14-17 in (35-42 cm)", weight="20-24 lb (9-11 kg)", life="12-13 years",
  origin="The Netherlands", colors=[],
  marks=["White blaze on face","Drop ears covered in long, silky hair",
         "Alert, almond-shaped, deep brown eyes","Sleek, slightly wavy, white coat with orange-red patches",
         "Long hair on neck forms ruff","Well-feathered tail","Feathering on back of front legs",
         "Small, harelike feet"],
  para="Also called the Dutch Decoy Spaniel, and its job explains its build: it "
       "waves its white flag of a tail to lure curious waterfowl down tunnel traps "
       "to be caught alive — work it still does for researchers ringing birds. "
       "Small, white with orange-red patches, and it never barks on the job.",
  tell="Small white dog with orange-red patches and a white flag of a tail",
  hook="The DECOY dog — waves its white tail to hypnotise ducks.",
  say="KOY-ker-hont-yuh",
  mark="FLAG TAIL", anchor=(0.12,0.34), side="r"),

dict(src="IMG_4361", name="Picardy Spaniel", group="spaniel",
  fam=["french-spaniel"], page=239,
  height="22-24 in (55-60 cm)", weight="44-55 lb (20-25 kg)", life="12-14 years",
  origin="France", colors=[],
  marks=["Long, low-set, drop ears","Oval head with well-defined stop","Back slopes down toward tail",
         "Curved tail with feathering","Squarely built body","Rich tan markings","Brown patch",
         "Dense coat has slight wave and gray mottling","Large feet are round, with feathering between toes"],
  para="One of the oldest spaniel breeds, still used in France to flush birds in "
       "woodland and wetland. The coat is grey-mottled with brown patches and rich "
       "tan markings on the face and legs. An enthusiastic swimmer and a placid, "
       "reliable dog at home.",
  tell="Grey-mottled coat with brown patches and TAN markings on face and legs",
  hook="Picardy has TAN points. Blue Picardy has none.",
  say="PIK-ar-dee",
  mark="TAN MARKINGS", whole=True, anchor=(0.84,0.30), side="l"),

dict(src="IMG_4362", name="Blue Picardy Spaniel", group="spaniel",
  fam=["french-spaniel"], page=239,
  height="23-24 in (57-60 cm)", weight="44-46 lb (20-21 kg)", life="11-13 years",
  origin="France", colors=[],
  marks=["Well-defined stop","Slightly wavy coat with black patches","Pendulous flews",
         "Long, drop ears are covered with wavy hair","Lighter-colored blaze",
         "Tail about hock length","Gray-black speckling gives bluish shade to coat",
         "Tight, round feet have plenty of hair between toes"],
  para="A quiet, easygoing water dog used to point and retrieve snipe in marshland. "
       "The grey-black speckling over black patches gives the whole coat its "
       "characteristic blue cast. Friendly to a fault — which makes it useless as "
       "a guard.",
  tell="Grey-black speckling giving a distinctly BLUE cast, with no tan anywhere",
  hook="Blue = speckled black, no tan. Plain Picardy = brown with tan points.",
  say="PIK-ar-dee",
  mark="BLUE SPECKLING", whole=True, anchor=(0.50,0.42), side="l"),

dict(src="IMG_4363", name="French Spaniel", group="spaniel",
  fam=["french-spaniel"], page=240,
  height="22-24 in (55-61 cm)", weight="44-55 lb (20-25 kg)", life="12-14 years",
  origin="France", colors=[],
  marks=["Straight top to muzzle","Large, oval eyes match brown of coat",
         "Pendant ears set pretty far back on the head","Tail curves upward toward tip",
         "Silky, white and brown coat","Brown spotting on chest"],
  para="Claimed at home to be the original of all the hunting spaniels. It is tall, "
       "elegant and clean-marked — silky white with clear brown patches rather than "
       "the mottling of the Picardy breeds. Level-headed and not inclined to bark, "
       "so it copes with city life given enough exercise.",
  tell="Clean silky white with defined brown patches — clear-cut, not mottled",
  hook="French Spaniel = CLEAN patches. Picardy = muddy mottle.",
  say="ay-pan-YUL fron-SAY",
  mark="CLEAN BROWN PATCHES", whole=True, anchor=(0.52,0.32), side="l"),

# ---------------- water dogs ----------------
dict(src="IMG_4347", name="Spanish Water Dog", group="water",
  fam=["curly-water","corded"], page=230,
  height="16-20 in (40-50 cm)", weight="31-49 lb (14-22 kg)", life="10-14 years",
  origin="Spain", colors=["White","Black","Brown and white","Black and white"],
  marks=["Brown nose matches color of coat","Light chest markings",
         "Woolly, brown coat forms cords if left unclipped","Back slopes gently down toward tail",
         "Tail barely reaches hocks","Legs slightly shorter than body length",
         "Round feet covered in hair"],
  para="Known at home as the Perro de Agua, and used for herding, hunting and "
       "towing boats in port. Left unclipped, the woolly coat forms cords all over. "
       "Biddable and generally level-headed, but it can be impatient with children, "
       "and it remains rare outside southern Spain.",
  tell="Woolly coat that cords all over, on a dog slightly longer than tall",
  hook="Spain's all-rounder — herds, hunts and TOWS BOATS in dreadlocks.",
  say="PERR-oh day AH-gwah",
  mark="CORDED COAT", whole=True, anchor=(0.45,0.45), side="r"),

dict(src="IMG_4348", name="Poodle (Standard)", group="water",
  fam=["poodle"], page=231,
  height="Over 15 in (Over 38 cm)", weight="46-71 lb (21-32 kg)", life="10-13 years",
  origin="Germany", colors=["Any solid color"],
  marks=["Head carried high","Long, wide, pendant ears","Dark, almond-shaped eyes",
         "Strong, well-chiseled face and jaw","Profuse, dense, curly coat",
         "Small, oval feet, with arched toes"],
  para="Claimed by France but almost certainly German, and originally a water dog — "
       "the standard size stays closest to those roots. Robust, clever and good "
       "tempered, which is why it is used so heavily in crossbreeding. A plain "
       "all-over clip is the easiest coat to maintain.",
  tell="Profuse dense curls in one solid colour, carried on a tall square frame",
  hook="A RETRIEVER in disguise — the clip is a haircut, not a personality.",
  mark="DENSE CURLS", whole=True, anchor=(0.48,0.42), side="r"),

dict(src="IMG_4350", name="Corded Poodle", group="water",
  fam=["pale","poodle","corded"], page=233,
  height="9-24 in (24-60 cm)", weight="46-71 lb (21-32 kg)", life="10-13 years",
  origin="France", colors=["Any color"],
  marks=["Muzzle has straight bridge","Long, elegant, narrow head","Oblique, almond-shaped eyes",
         "Ears covered with many cords","Level back","Fine, dense, corded, white coat",
         "Black, corded coat"],
  para="Bred from separate poodle lines for many years but not yet recognised as a "
       "breed of its own. The look was fashionable in the 19th century and is now "
       "rare even in France. Most poodle coats will cord with a little encouragement, "
       "and once the cords have formed they are fairly easy to look after.",
  tell="Poodle proportions wrapped in long hanging cords rather than clipped curls",
  hook="Same dog as a Standard Poodle — DREADLOCKED instead of clipped.",
  mark="LONG CORDS", whole=True, anchor=(0.62,0.50), side="l"),

dict(src="IMG_4349", name="Portuguese Water Dog", group="water",
  fam=["curly-water","poodle"], page=231,
  height="17-22 in (43-57 cm)", weight="35-55 lb (16-25 kg)", life="10-14 years",
  origin="Portugal", colors=["White","Brown","Black and white","Brown and white"],
  marks=["Round eyes are set far apart","Curved tail with plume at tip",
         "Forehead has central furrow","Hindquarters clipped for work and showing",
         "Long, wavy, black coat","Round feet"],
  para="Classed as a gundog but used as often to retrieve fishermen's nets as "
       "hunters' game. There are two coat types, long and wavy or short and curly, "
       "and the traditional working clip leaves the hindquarters shorn. A lively "
       "mind that turns destructive if the dog is not kept busy.",
  tell="Clipped hindquarters with a plumed tail tip — the working lion clip",
  hook="Clipped BEHIND, plume on the TAIL TIP — a fisherman's dog.",
  mark="PLUMED TAIL TIP", anchor=(0.3,0.34), side="r"),

dict(src="IMG_4351", name="Barbet", group="water",
  fam=["curly-water","beard"], page=232,
  height="19-24 in (48-62 cm)", weight="35-65 lb (16-29 kg)", life="12-14 years",
  origin="France", colors=["Variety of colors"],
  marks=["Low-set, drop ears covered by long hair","Face profusely covered with hair",
         "Gray hairs on chin","Long, woolly, curly, solid black coat",
         "Tail has slight hook at tip","Round, broad feet"],
  para="One of Europe's oldest water dogs, with ancestors going back to the Middle "
       "Ages, and an ancestor in turn to many other breeds. The whole face is buried "
       "in hair — that coat is superb protection for a working dog but needs daily "
       "attention, which is probably why the breed fell out of fashion.",
  tell="Woolly curls covering the entire face, ears buried under long hair",
  hook="Barbet = BEARD. The face disappears completely.",
  say="bar-BAY",
  mark="HAIRY FACE", anchor=(0.86,0.32), side="l"),

dict(src="IMG_4352", name="Frisian Water Dog", group="water",
  fam=["dutch","curly-water"], page=232,
  height="22-23 in (55-59 cm)", weight="33-44 lb (15-20 kg)", life="12-13 years",
  origin="The Netherlands", colors=["Dark brown"],
  marks=["Low-set ears hang flat against head","Rounded top to head",
         "Long tail curled into a ring","Solid black coat","White chest markings",
         "Round, arched feet"],
  para="Also called the Dutch Spaniel or Wetterhoun, and originally used by "
       "fishermen to control otters. It still flushes and retrieves but doubles as "
       "a farm guard. Independent and slightly suspicious by nature, which makes it "
       "a poor fit for city living but a reliable rural dog.",
  tell="Curly coat with the long tail carried curled into a tight ring over the back",
  hook="The OTTER dog with a tail curled like a doorknocker.",
  say="VET-er-hoon",
  mark="RING TAIL", anchor=(0.2,0.36), side="r"),

dict(src="IMG_4355", name="Lagotto Romagnolo", group="water",
  fam=["curly-water","beard"], page=235,
  height="16-19 in (41-48 cm)", weight="24-35 lb (11-16 kg)", life="12-14 years",
  origin="Italy", colors=["Orange","Brown","Roan"],
  marks=["Moderately large, triangular, drop ears with rounded tips","Liver-colored nose",
         "Woolly, off-white coat forms tight ringlets","Curly, white coat with brown markings",
         "Deep chest","Round, compact feet"],
  para="Originally a marshland retriever in northern Italy, later re-employed as a "
       "truffle hound — the only breed specifically bred for the job. The woolly "
       "coat forms tight ringlets and needs weekly combing and an annual clip. "
       "Good-natured and happiest when kept busy.",
  tell="Tight woolly off-white ringlets on a compact, square, teddy-bear frame",
  hook="The TRUFFLE dog — a woolly teddy bear with a nose for money.",
  say="la-GOT-toh roh-man-YOH-loh",
  mark="TIGHT RINGLETS", whole=True, anchor=(0.46,0.40), side="r"),

# ---------------- pointers & HPR ----------------
dict(src="IMG_4354", name="Brittany", group="pointer",
  fam=["french-spaniel","orange-white"], page=234,
  height="19-20 in (47-51 cm)", weight="31-40 lb (14-18 kg)", life="12-14 years",
  origin="France", colors=["Liver and white","Black and white","Black, tan, and white"],
  marks=["Muzzle tapered but not pointed","Oval, dark eyes","Triangular, drop ears",
         "High-set tail carried just below back level","Dense, fairly fine, slightly wavy, orange and white coat",
         "Orange flecking","Feathering on forelegs","Compact, round feet"],
  para="Known as the Brittany Spaniel, and as the Epagneul Breton at home. It "
       "flushes and retrieves but is at its best simply locating game birds. An "
       "old breed that nearly vanished in the 19th century and has since regained "
       "popularity as both a sporting dog and a family companion.",
  tell="Compact orange-and-white dog with a very high-set, naturally short tail",
  hook="A pointer in a spaniel's body — SHORT TAIL, orange flecks.",
  say="ay-pan-YUL breh-TON",
  mark="HIGH-SET TAIL", anchor=(0.1,0.45), side="r"),

dict(src="IMG_4356", name="Small Munsterlander Pointer", group="pointer",
  fam=["munsterlander","dutch"], page=236,
  height="20-21 in (52-53 cm)", weight="40-60 lb (18-27 kg)", life="13-14 years",
  origin="Germany", colors=[],
  marks=["White blaze on head","Well-feathered, broad ears","Silky, brown coat",
         "Medium-length, well-feathered tail","White legs with brown mottling"],
  para="One German name for it, Heidewachtel or 'heath quail dog', describes its "
       "first job of flushing game birds. Cheerful and affectionate, but hunters "
       "snap up nearly every one of the small number bred each year. Despite the "
       "name it is not directly related to the Large Munsterlander.",
  tell="Silky brown coat with white brown-mottled legs and a white blaze",
  hook="SMALL = brown. LARGE = black. Not actually related.",
  say="MUUN-ster-lan-der",
  mark="BROWN & WHITE", whole=True, anchor=(0.50,0.32), side="l"),

dict(src="IMG_4357", name="Large Munsterlander", group="pointer",
  fam=["munsterlander"], page=236,
  height="23-26 in (58-65 cm)", weight="65-68 lb (29-31 kg)", life="12-13 years",
  origin="Germany", colors=[],
  marks=["Solid black head","White hairs at tip of snout","Black mantle",
         "White coat with black flecking","Long, dense coat provides insulation",
         "Legs are well feathered"],
  para="The Grosser Munsterlander is more closely related to the German pointers "
       "than to the Small Munsterlander. Slow to mature but calm, highly trainable "
       "and genuinely versatile. It thrives on close human company and is good with "
       "children.",
  tell="Solid black head above a white body heavily flecked with black",
  hook="Black HEAD, black MANTLE, snowstorm everywhere else.",
  say="MUUN-ster-lan-der",
  mark="SOLID BLACK HEAD", anchor=(0.9,0.3), side="l"),

dict(src="IMG_4358", name="Frisian Pointing Dog", group="pointer",
  fam=["pale","dutch","munsterlander"], page=237,
  height="20-21 in (50-53 cm)", weight="42-55 lb (19-25 kg)", life="12-14 years",
  origin="The Netherlands", colors=["Orange with white markings"],
  marks=["Long, straight, smooth, black coat with white markings","Pronounced stop",
         "Black ticking","Long, level back","Feathered, curving tail",
         "Back of front legs well feathered"],
  para="Also known as the Stabyhoun, and bred by farmers to track, point and "
       "retrieve alongside hunters. Active and even-tempered, and excellent with "
       "children. Despite steady efforts to build up its numbers it remains rare "
       "even in its native Friesland.",
  tell="Long straight black-and-white coat with black ticking on a level back",
  hook="Stabyhoun = the FARMER'S dog. Long straight coat, no curl at all.",
  say="STAH-bee-hoon",
  mark="BLACK TICKING", whole=True, anchor=(0.48,0.48), side="l"),

dict(src="IMG_4359", name="Drentsche Partridge Dog", group="pointer",
  fam=["pale","dutch","munsterlander"], page=237,
  height="22-25 in (55-63 cm)", weight="44-55 lb (20-25 kg)", life="12-13 years",
  origin="The Netherlands", colors=[],
  marks=["Oval, amber eyes","Brown markings","Drop ears covered with long, silky hair",
         "Well-feathered tail","Wavy, white coat","Brown spots on legs"],
  para="Somewhere between a pointer and a retriever, the Patrijshond is a typically "
       "versatile European hunting dog, related to the Small Munsterlander Pointer "
       "and the French Spaniel. It stays relaxed enough for city life provided it "
       "gets enough activity.",
  tell="Wavy white coat with solid brown patches and a brown, silky-eared head",
  hook="Dutch partridge dog — brown patches, WAVY white, amber eyes.",
  say="DRENT-suh PA-trice-hont",
  mark="BROWN PATCHES", whole=True, anchor=(0.50,0.34), side="l"),

dict(src="IMG_4369", name="Cesky Fousek", group="pointer",
  fam=["wirehair","beard"], page=245,
  height="23-26 in (58-66 cm)", weight="49-75 lb (22-34 kg)", life="12-13 years",
  origin="Czech Republic", colors=["Brown"],
  marks=["Distinctive, bushy eyebrows","Large, drop ears","Beard of soft hair",
         "Deep-set, amber eyes with kind expression","Brown nose",
         "Hard, protective, dark roan coat with brown patches",
         "Tail traditionally docked to two-fifths of length","Compact, spoon-shaped feet"],
  para="Claimed variously as Czech, Slovakian or Bohemian, and still a popular "
       "hunting dog in those countries though rare elsewhere. Loyal, trainable and "
       "usually gentle with people — but a natural hunter, so it can be unreliable "
       "around other pets.",
  tell="Dark roan wire coat with brown patches, bushy brows and a soft beard",
  hook="Czech wirehair: dark ROAN body, brown patches, big eyebrows.",
  say="CHESS-kee FOH-sek",
  mark="DARK ROAN COAT", whole=True, anchor=(0.48,0.40), side="l"),

dict(src="IMG_4370", name="Wirehaired Pointing Griffon", group="pointer",
  fam=["wirehair","beard"], page=245,
  height="20-24 in (50-60 cm)", weight="51-60 lb (23-27 kg)", life="12-13 years",
  origin="The Netherlands", colors=["Liver","White and orange","Roan, white, and brown"],
  marks=["Hairy eyebrows","Shorter, liver hair on ears","Long muzzle with hairy beard and mustache",
         "Body length exceeds leg length","Harsh, coarse, steel-gray coat with dense undercoat",
         "Deep chest","Round feet with tight, arched toes"],
  para="Bred by the Dutchman Edward Korthals and taken up by French hunters — "
       "related to the German Shorthaired Pointer. Not the fastest gundog, which is "
       "exactly the point: it is prized where hunters want an obedient, close-working "
       "dog. Those same qualities make it an easy companion.",
  tell="Harsh steel-grey wire coat with a full beard and moustache",
  hook="Korthals' griffon — STEEL GREY with a walrus moustache.",
  say="KOR-tahls GRIFF-on",
  mark="STEEL-GRAY WIRE", whole=True, anchor=(0.48,0.36), side="l"),

dict(src="IMG_4371", name="German Shorthaired Pointer", group="pointer",
  fam=["ticked-pointer","german-pointer"], page=244,
  height="21-25 in (53-64 cm)", weight="44-71 lb (20-32 kg)", life="10-14 years",
  origin="Germany", colors=["Liver","Brown","Black"],
  varieties=["Shorthaired","Wirehaired","Longhaired"],
  marks=["Well-defined stop","Broad, drop ears, rounded at tips","Medium-sized, brown eyes",
         "Liver patch","Liver coat with white ticking, coarse to touch","Tucked-up belly",
         "Tapering tail with white tip, carried low","Spoon-shaped, compact feet"],
  para="A superlative hunting dog that tracks, points and retrieves over any "
       "terrain from heathland to marsh. The Deutsch Kurzhaar has always been kept "
       "as a house dog as well as a hunting one, and is generally level-headed and "
       "reliable — but it turns hyperactive and destructive without real exercise. "
       "Three coat types exist; the shorthaired is by far the best known.",
  tell="Liver head and patches over a densely white-ticked body, short and coarse",
  hook="GSP = liver head, TICKED body, low tail with a white tip.",
  mark="WHITE TICKING", whole=True, anchor=(0.44,0.46), side="l"),

dict(src="IMG_4372", name="Weimaraner", group="pointer",
  fam=["german-pointer","gray"], page=246,
  height="22-27 in (56-69 cm)", weight="55-90 lb (25-41 kg)", life="12-13 years",
  origin="Germany", colors=[],
  varieties=["Longhaired","Shorthaired"],
  marks=["Striking, pale blue-gray eyes","Large, high-set ears have slight fold",
         "Gray nose","Silky, silver-gray coat","Body as long as height at the withers",
         "Moderately tucked-up belly","Tail reaches hocks","Firm, compact feet"],
  para="Created as an all-purpose hunting, pointing and retrieving gundog and "
       "nicknamed the Gray Ghost. Careful, almost stealthy in the field, and "
       "elegant enough that looks alone have driven its popularity. It can stay "
       "active for hours and needs an owner with matching stamina.",
  tell="Solid silver-grey coat with a grey nose and pale blue-grey eyes",
  hook="The GRAY GHOST — grey coat, grey nose, ghost-pale eyes.",
  say="VY-mar-ah-ner",
  mark="SILVER-GRAY COAT", whole=True, anchor=(0.46,0.44), side="l"),

dict(src="IMG_4373", name="Vizsla", group="pointer",
  fam=["hungarian","red"], page=247,
  height="21-25 in (53-64 cm)", weight="44-66 lb (20-30 kg)", life="13-14 years",
  origin="Hungary", colors=[],
  marks=["Nose color matches coat","Eyes slightly darker than coat color",
         "Smooth, arched neck is muscular","Strong, muscular back",
         "Distinctive, sleek, golden-russet coat lacks insulating undercoat",
         "Slightly curved tail tapers to pointed tip","Long forearms","Tight, arched, round, catlike feet"],
  para="Also known as the Hungarian Shorthaired Pointer, and thought to date to the "
       "16th century. Extremely affectionate and intelligent, and very responsive to "
       "training. It has almost boundless energy and will fetch sticks as happily as "
       "game — all day, if allowed.",
  tell="Sleek golden-russet coat with a nose the SAME colour as the coat",
  hook="Rust dog, rust nose — nothing black on a Vizsla anywhere.",
  say="VEEZH-lah",
  mark="RUSSET NOSE", anchor=(0.94,0.26), side="l"),

dict(src="IMG_4374", name="Wirehaired Vizsla", group="pointer",
  fam=["hungarian","red","wirehair","beard"], page=247,
  height="21-24 in (53-62 cm)", weight="44-66 lb (20-30 kg)", life="12-14 years",
  origin="Hungary", colors=[],
  marks=["Rounded, V-shaped ears","Golden sand-colored coat","Eyes slightly darker than coat",
         "Deep chest reaching down to elbows","Low-set, slightly curved tail","Straight forelegs"],
  para="The wirehaired variety of the Hungarian Vizsla, developed in the 1930s and "
       "stronger in build than the smooth one — probably because it came from a "
       "cross between a smooth Vizsla and a German Wirehaired Pointer. The dense "
       "wiry coat suits cold-weather hunting, and the shaggy beard and eyebrows "
       "give it an alert but gentle expression.",
  tell="Vizsla colouring in a dense wiry coat, with a shaggy beard and eyebrows",
  hook="Same rust dog, WIRE coat and a beard — and a heavier frame.",
  say="VEEZH-lah",
  mark="WIRY BEARD", anchor=(0.84,0.3), side="l"),

dict(src="IMG_4375", name="Portuguese Pointer", group="pointer",
  fam=["ticked-pointer","iberian"], page=248,
  height="19-24 in (48-60 cm)", weight="35-60 lb (16-27 kg)", life="12-14 years",
  origin="Portugal", colors=[],
  marks=["Triangular, drop ears","Moderately developed flews","Dark eyes with dark rims",
         "Short, red-yellow coat","Deep chest","Slightly tucked-up belly",
         "Square muzzle","Slight dewlap","White markings on feet"],
  para="The Perdigueiro Português — literally the Portuguese Partridge Dog — was "
       "used as a pointer for hunters working with falcons or nets. Still worked "
       "today, and level-headed enough to make an amenable companion, though this "
       "tenacious hunter needs serious mental and physical work every day.",
  tell="Short red-yellow coat with a square muzzle and a slight dewlap",
  hook="Portugal's pointer: RED-YELLOW, square muzzle, loose throat.",
  say="per-di-GAY-roo por-too-GESH",
  mark="RED-YELLOW COAT", whole=True, anchor=(0.50,0.42), side="l"),

dict(src="IMG_4376", name="Bracco Italiano", group="pointer",
  fam=["pale","ticked-pointer","italian"], page=248,
  height="22-26 in (55-67 cm)", weight="55-88 lb (25-40 kg)", life="12-13 years",
  origin="Italy", colors=["White","White with orange, amber, or brown markings"],
  marks=["Slightly arched muzzle","Pendant ears with rounded tips","Well-developed flews",
         "Nose matches coat color","Powerful neck has soft dewlap",
         "Smooth, roan coat with chestnut markings","Tail tapers slightly","Oval-shaped feet"],
  para="Dogs like the Italian Pointer appear in paintings from the 14th century, "
       "when they were used to drive game birds into nets. Still worked today, and "
       "level-headed and gentle at home, though it can be stubborn. The heavy flews "
       "and soft dewlap give it a distinctly houndlike head.",
  tell="Houndlike head with heavy flews and a dewlap, on a roan chestnut-marked body",
  hook="A pointer with a BLOODHOUND'S head — flews, dewlap, sad eyes.",
  say="BRAH-koh it-al-YAH-noh",
  mark="HEAVY FLEWS", whole=True, anchor=(0.94,0.22), side="l"),

dict(src="IMG_4377", name="Spinone Italiano", group="pointer",
  fam=["pale","wirehair","beard","italian"], page=249,
  height="23-28 in (58-70 cm)", weight="65-85 lb (29-39 kg)", life="12-13 years",
  origin="Italy", colors=["White","Orange roan","White and brown or brown roan"],
  marks=["Large, round, ocher eyes with kind expression","Triangular, pendant ears",
         "Light-colored nose","Long mustache blends into beard","Broad, deep chest",
         "Coarse, dense, white and orange coat","Back curves gently",
         "Thick tail carried low","Slightly tucked-up belly","Large, round feet"],
  para="A versatile tracker and retriever from northern Italy, and the region's most "
       "popular hunting breed until the 20th century. It works at a deliberately "
       "slower pace than most gundogs, which makes it a comfortable walking "
       "companion. Gentle and loyal — but the coarse coat holds smells and the "
       "breed drools.",
  tell="Big shaggy white-and-orange dog with ocher eyes and a full moustache",
  hook="The GENTLE GIANT that ambles — ocher eyes, soup-strainer moustache.",
  say="spin-OH-nay it-al-YAH-noh",
  mark="OCHER EYES", whole=True, anchor=(0.86,0.22), side="l"),

dict(src="IMG_4378", name="French Pyrenean Pointer", group="pointer",
  fam=["pale","ticked-pointer","braque"], page=250,
  height="19-23 in (47-58 cm)", weight="40-53 lb (18-24 kg)", life="12-14 years",
  origin="France", colors=["Chestnut-brown"],
  marks=["Typical, chestnut-brown head","Broad, straight back, may be very long",
         "Nose matches coat color","Very short, fine, chestnut-brown and white coat",
         "Belly moderately tucked up","Area of speckling denser than French Gascony Pointer"],
  para="The most popular of the French pointers, though still rare and mostly in "
       "hunters' hands. Created in south-west France to work mountain terrain, it is "
       "swift and tireless in the field and gentle and affectionate at home. Its "
       "speckling is noticeably denser than its Gascony cousin's.",
  tell="Chestnut head and DENSE speckling on a short fine coat",
  hook="Pyrenean = DENSE speckle. Gascony = sparse speckle. Same dog otherwise.",
  say="brahk fron-SAY pee-ray-NAY",
  mark="DENSE SPECKLING", whole=True, anchor=(0.46,0.44), side="l"),

dict(src="IMG_4384", name="French Gascony Pointer", group="pointer",
  fam=["pale","ticked-pointer","braque"], page=253,
  height="22-27 in (56-69 cm)", weight="55-71 lb (25-32 kg)", life="12-14 years",
  origin="France", colors=["Chestnut-brown"],
  marks=["Drop ears with rounded tips","Chestnut-brown eyes","Broad, straight back",
         "Very fine, short, chestnut-brown and white coat","Slightly tucked-up belly",
         "Chestnut-brown flecking less dense than on French Pyrenean Pointer",
         "Compact, almost round feet"],
  para="One of the oldest pointer breeds, from south-west France, still kept as a "
       "hunter's dog as well as a household companion. Loyal and affectionate with a "
       "sensitive nature that responds best to gentle, consistent training, and a "
       "determined tracker in the field.",
  tell="Chestnut and white with SPARSE flecking — bigger than the Pyrenean",
  hook="Gascony is the BIGGER, less-speckled brother.",
  say="brahk fron-SAY gas-KOHN-yuh",
  mark="SPARSE FLECKING", whole=True, anchor=(0.46,0.44), side="l"),

dict(src="IMG_4379", name="Saint Germain Pointer", group="pointer",
  fam=["pale","ticked-pointer","braque","orange-white"], page=250,
  height="21-24 in (53-62 cm)", weight="40-57 lb (18-26 kg)", life="12-14 years",
  origin="France", colors=[],
  marks=["Pink nose","Golden-yellow eyes","Flews cover lower jaw",
         "Tapering, hock-length tail carried horizontally",
         "Smooth, dull white coat with orange markings","Long, deep chest",
         "Long feet with light-colored nails"],
  para="The Braque Saint-Germain, a fleet-footed pointer and retriever of birds in "
       "field, woodland and marsh — though its thin coat rules it out as an "
       "all-weather dog. Affectionate but sensitive, needing firm yet gentle "
       "handling, and it adapts surprisingly well to urban family life.",
  tell="Dull white with clean orange patches, a PINK nose and golden-yellow eyes",
  hook="PINK nose and yellow eyes — no other French braque has both.",
  say="brahk san zher-MAN",
  mark="PINK NOSE", anchor=(0.94,0.24), side="l"),

dict(src="IMG_4380", name="Bourbonnais Pointing Dog", group="pointer",
  fam=["pale","ticked-pointer","braque"], page=251,
  height="19-22 in (48-57 cm)", weight="35-57 lb (16-26 kg)", life="12-14 years",
  origin="France", colors=[],
  marks=["Pear-shaped head","Brown, drop ears with rounded tips","Slightly tapered muzzle",
         "Nose color matches brown of coat","Line of belly rises steadily",
         "Fine, dense, white coat with brown ticking and markings","Round feet"],
  para="The oldest and perhaps the most level-headed of the French gundog breeds, "
       "and a versatile tracker, pointer and retriever. Robust in build and giving "
       "an impression of real power, it is full of stamina at work and relaxed and "
       "affectionate off duty.",
  tell="Pear-shaped head over a finely brown-ticked white coat",
  hook="The PEAR-headed braque — brown ticking, no chestnut patches.",
  say="brahk doo boor-bon-NAY",
  mark="PEAR-SHAPED HEAD", anchor=(0.88,0.26), side="l"),

dict(src="IMG_4382", name="Auvergne Pointer", group="pointer",
  fam=["pale","ticked-pointer","braque","black-white"], page=252,
  height="21-25 in (53-63 cm)", weight="49-62 lb (22-28 kg)", life="12-13 years",
  origin="France", colors=[],
  marks=["Black nose","Typical black markings on face and ears","Oval, dark hazel eyes",
         "Level topline","Shiny, short, white coat with black markings",
         "Black flecking over white gives coat blue appearance","Flews neatly overlap lower lip",
         "Tail reaches hock"],
  para="The Braque d'Auvergne was bred in central France by and for hunters, and "
       "remains a tenacious all-purpose dog that can work all day over long "
       "distances. Friendly, intelligent and easily trained, it loves company and "
       "will thrive in any active household.",
  tell="BLACK head and ears over a blue-flecked white body — never brown",
  hook="The only French braque in BLACK. All the others are chestnut.",
  say="brahk doh-VAIRN",
  mark="BLACK HEAD", anchor=(0.88,0.24), side="l"),

dict(src="IMG_4383", name="Ariege Pointing Dog", group="pointer",
  fam=["pale","ticked-pointer","braque"], page=252,
  height="22-26 in (56-67 cm)", weight="55-66 lb (25-30 kg)", life="12-14 years",
  origin="France", colors=[],
  marks=["Oval eyes have gentle expression","Flesh-colored nose","Fine, folded, tan ears",
         "Short, glossy, white coat with fawn ticking","Long, straight muzzle",
         "Tapering tail","Compact feet with well-arched toes"],
  para="Rare even in its homeland in south-west France, the Braque de l'Ariège is "
       "used for pointing and retrieving and has some tracking ability. Almost "
       "exclusively owned by hunters, it needs patient training to settle an "
       "enthusiastic nature that can spill over into wildness.",
  tell="Very pale — white with fawn ticking, tan ears and a flesh-coloured nose",
  hook="The PALEST braque: fawn ticks, flesh nose, almost washed out.",
  say="brahk duh lar-YEZH",
  mark="FLESH-COLORED NOSE", anchor=(0.94,0.24), side="l"),

dict(src="IMG_4381", name="Pudelpointer", group="pointer",
  fam=["wirehair","german-pointer","beard"], page=251,
  height="22-27 in (55-68 cm)", weight="44-66 lb (20-30 kg)", life="12-14 years",
  origin="Germany", colors=["Dead leaf","Black"],
  marks=["Curling forelock","Drop ears lie close to head","Large, dark, amber eyes",
         "Beard and mustache lighter in color","Saberlike tail",
         "Hard, rough, brown coat, with dense undercoat","White markings on chest",
         "Slightly tucked-up belly","Oval feet"],
  para="A deliberate cross of poodle and pointer aiming to combine the best of both: "
       "intelligent, hardy and sociable, with excellent all-round working ability. "
       "Most popular with hunters, and an amenable, cheerful rural companion. The "
       "curling forelock is inherited straight from the poodle side.",
  tell="Rough brown coat with a curling forelock and a pale beard",
  hook="POODLE + POINTER — the forelock gives away the poodle half.",
  say="POO-del-poyn-ter",
  mark="CURLING FORELOCK", anchor=(0.88,0.18), side="l"),

dict(src="IMG_4385", name="Slovakian Rough-haired Pointer", group="pointer",
  fam=["wirehair","gray","beard"], page=253,
  height="22-27 in (57-68 cm)", weight="55-77 lb (25-35 kg)", life="12-14 years",
  origin="Slovakia", colors=[],
  marks=["Long, lean head","Drop ears with short, soft hair","Almond-shaped, amber eyes",
         "Longer, softer, lighter-colored hair on muzzle","Straight, solid back slopes slightly down toward tail",
         "Harsh, flat, gray (brown-shaded sable) coat","White markings on chest",
         "Rounded feet with well-arched toes"],
  para="Found under a variety of names — Slovensky Pointer, Wirehaired Slovakian "
       "Pointer, Slovenský Hrubosrstý Stavač at home. Probably descended from German "
       "hunting dogs and showing their intelligence, good humour and energy. Not a "
       "breed to leave alone: it thrives on company and activity.",
  tell="Harsh flat GREY coat with a long lean head and a pale wiry muzzle",
  hook="A wirehaired Weimaraner, essentially — grey, but harsh-coated.",
  say="SLOH-ven-skee HROO-bo-sr-stee",
  mark="HARSH GRAY COAT", whole=True, anchor=(0.46,0.42), side="l"),

dict(src="IMG_4386", name="Pointer", group="pointer",
  fam=["pale","ticked-pointer","orange-white"], page=254,
  height="24-27 in (61-69 cm)", weight="44-75 lb (20-34 kg)", life="12-13 years",
  origin="UK", colors=["Variety of colors"],
  marks=["Very well-defined stop","Bright, hazel eyes","Drop ears","Well-developed, soft flews",
         "White blaze on head","Back slopes gently toward tail",
         "Fine, hard, short, orange and white coat","Medium-length tail carried level with back",
         "Oval feet with well-arched toes"],
  para="Also known as the English Pointer — swift and eager when tracking and "
       "pointing, the tasks it has been used for since the 17th century, though it "
       "does not retrieve particularly well. Gentle, loyal and obedient in character, "
       "and reliable with children, though it can be too boisterous for toddlers.",
  tell="Tall, clean-lined, short-coated, with a very deep stop and a level tail",
  hook="The ORIGINAL pointer — deepest stop in the group, tail dead level.",
  mark="DEEP STOP", anchor=(0.82,0.36), side="l"),

dict(src="IMG_4387", name="Spanish Pointer", group="pointer",
  fam=["pale","ticked-pointer","iberian"], page=255,
  height="23-26 in (59-67 cm)", weight="55-66 lb (25-30 kg)", life="12-14 years",
  origin="Spain", colors=[],
  marks=["White patch on head","Liver-colored patch","Dark hazel eyes have soft, sad expression",
         "Large, drop ears","Well-developed flews cover lower lip","Well-defined dewlap on neck",
         "White and liver hairs give coat marbled appearance","Point of sternum prominent",
         "Round, catlike feet","Tail traditionally docked to one-third of natural length"],
  para="The Perdiguero de Burgos was bred to track deer and is now used mostly for "
       "smaller game — halfway between a scent hound and a pointer, and a keen "
       "hunter that thrives on work. Reliable and easy-going, it fits well into "
       "family life despite the serious expression.",
  tell="Marbled white-and-liver coat with heavy flews, a dewlap and a sad expression",
  hook="Spain's pointer wears a HOUND'S face — dewlap, flews, sad eyes.",
  say="per-di-GAIR-oh day BOOR-gohs",
  mark="MARBLED COAT", whole=True, anchor=(0.48,0.42), side="l"),

dict(src="IMG_4388", name="Old Danish Pointer", group="pointer",
  fam=["pale","ticked-pointer"], page=255,
  height="20-24 in (50-60 cm)", weight="57-77 lb (26-35 kg)", life="12-13 years",
  origin="Denmark", colors=[],
  marks=["Moderate stop","Broad, drop ears with rounded tips","Liver flecking",
         "Firm, muscular back slopes slightly toward tail","Muscular, slightly 'throaty' neck",
         "Dense, white coat with liver markings","Liver patch",
         "Tapering tail almost reaches hock"],
  para="Its local name, Gammel Dansk Hønsehund, translates as Old Danish Chicken "
       "Dog or Bird Dog. Still used as a determined tracker, pointer and retriever, "
       "and even as a sniffer dog, but even-tempered enough to make a family dog "
       "for anyone willing to give it plenty to do.",
  tell="Heavy-set and low-slung for a pointer, white with liver patches and flecks",
  hook="The STOCKY one — a pointer built like a barrel.",
  say="GAM-el dansk HERN-suh-hoon",
  mark="LIVER PATCHES", whole=True, anchor=(0.48,0.36), side="l"),

# ---------------- setters ----------------
dict(src="IMG_4364", name="English Setter", group="setter",
  fam=["setter"], page=240,
  height="24-25 in (61-64 cm)", weight="55-66 lb (25-30 kg)", life="12-13 years",
  origin="UK", colors=["Orange or lemon belton","Liver belton"],
  marks=["Low-set, pendant ears","Blue belton coat","Light tan marks on face",
         "Well-feathered tail","Square muzzle with slightly pendulous flews"],
  para="Developed to track, set and retrieve birds, and still worked today, though "
       "different bloodlines now serve hunting and home. Its speckled coat patterns "
       "have their own name — belton — with blue belton the classic. Cheerful and "
       "tireless, but calm and reliable with it.",
  tell="Fine speckled 'belton' coat — flecks scattered evenly, never solid patches",
  hook="BELTON = the speckle. Blue belton is black flecks on white.",
  mark="BELTON SPECKLING", whole=True, anchor=(0.50,0.36), side="l"),

dict(src="IMG_4365", name="Irish Setter", group="setter",
  fam=["setter","red"], page=241,
  height="25-27 in (64-69 cm)", weight="60-71 lb (27-32 kg)", life="12-13 years",
  origin="Ireland", colors=[],
  marks=["Deep, square muzzle","Silky, drop ears","Level, almond-shaped eyes have kind expression",
         "Long, glossy, red coat","Very deep and narrow chest","Well-feathered tail",
         "Shorter hair on front of lower legs","Longer hair on underside of body",
         "Feathering on back of legs"],
  para="The Modder Rhu — the red dog of Ireland — started as a hunting dog and "
       "still works, though it is now more often kept as a striking and spirited "
       "companion. Slow to mature and in need of firm early training: its "
       "devil-may-care streak can try an owner's patience. Sociable to the point "
       "of actively seeking out children and other dogs to play with.",
  tell="Long glossy SOLID red coat with a very deep, narrow chest",
  hook="Solid RED, no white — the Irish Setter is one colour all over.",
  mark="SOLID RED COAT", whole=True, anchor=(0.48,0.40), side="l"),

dict(src="IMG_4367", name="Irish Red and White Setter", group="setter",
  fam=["pale","setter","red-white"], page=242,
  height="25-27 in (64-69 cm)", weight="55-75 lb (25-34 kg)", life="12-13 years",
  origin="Ireland", colors=[],
  marks=["Broad, domed head","Clear, crisp colored areas","Ears level with eyes and set far back",
         "Red mottling on face","Fine, wavy, red and white coat","Strong body with deep chest"],
  para="This setter carries the red-and-white colouring typical of many hunting "
       "dogs, but today is more often kept for company. Long overshadowed by the "
       "related Irish Setter, it is slowly gaining the recognition it deserves. "
       "Cheerful and energetic, and it thrives on attention and firm guidance.",
  tell="Clean-edged red patches on white — crisp blocks, not the English Setter's speckle",
  hook="Irish R&W = crisp PATCHES. English Setter = fine speckle.",
  mark="CRISP PATCHES", whole=True, anchor=(0.52,0.32), side="l"),

dict(src="IMG_4368", name="Gordon Setter", group="setter",
  fam=["setter","black-tan"], page=242,
  height="24-26 in (62-66 cm)", weight="57-66 lb (26-30 kg)", life="12-13 years",
  origin="UK", colors=[],
  marks=["Deep head with slightly rounded skull","Lean, long neck","Shiny, coal-black coat",
         "Fringe on belly may extend to throat","Typical chestnut-red marking on feet and lower legs",
         "Full feathering on long, muscular thighs"],
  para="Originally employed in Scotland to track game birds and then freeze once it "
       "had found them. Changes in hunting fashion have moved the breed from field "
       "to fireside, and it brings a level-headed and loyal nature with it — though "
       "it still needs daily vigorous exercise and a good deal of space.",
  tell="Coal-black coat with chestnut-red points on the face, feet and lower legs",
  hook="The BLACK AND TAN setter — the only one in the group.",
  mark="BLACK & TAN", whole=True, anchor=(0.50,0.38), side="l"),

# ---------------- retrievers ----------------
dict(src="IMG_4389", name="Labrador Retriever", group="retriever",
  fam=["retriever"], page=256,
  height="22 in (55-57 cm)", weight="55-82 lb (25-37 kg)", life="10-12 years",
  origin="Canada", colors=["Chocolate","Black"],
  marks=["Broad head","Medium-sized, hazel eyes","Drop ears set well back","Moderate stop",
         "Black nose fades to light brown with age","Powerful neck","Level topline",
         "Broad chest","Weatherproof, short, yellow coat",
         "Characteristic 'otter' tail, round and well haired","Round, compact feet"],
  para="One of the most familiar dogs in the world, and top of the popularity lists "
       "for two decades. Its ancestors came not from Labrador but from Newfoundland, "
       "where fishermen bred waterproof-coated dogs to help tow in catches and "
       "retrieve escaping fish. Loving, easy to train and reliable with children and "
       "other pets — far too amiable to guard anything. It gains weight fast and "
       "needs both mental and physical work.",
  tell="Thick round 'otter' tail and a short weatherproof coat on a broad, blocky head",
  hook="OTTER TAIL — thick at the base, round, no feathering at all.",
  mark="OTTER TAIL", anchor=(0.09,0.42), side="r"),

dict(src="IMG_4390", name="Golden Retriever", group="retriever",
  fam=["retriever","gold"], page=258,
  height="20-24 in (51-61 cm)", weight="55-75 lb (25-34 kg)", life="12-13 years",
  origin="UK", colors=["Cream"],
  marks=["Drop ears","Powerful but well-chiseled head","Dark brown eyes",
         "Long, silky, golden coat","Long tail without a curl",
         "Dense, water-resistant, lighter undercoat","Round, catlike feet"],
  para="Bred as a powerful retriever for long-distance work, and used by hunters "
       "and in field trials as well as for guide work. Responsive, even-tempered "
       "and gregarious — this dog's main aim in life is to please, which is exactly "
       "why it makes no kind of guard dog.",
  tell="Long silky golden coat with heavy feathering and a straight, uncurled tail",
  hook="Golden = long FEATHERED coat. Labrador = short and slick.",
  mark="SILKY GOLD COAT", whole=True, anchor=(0.48,0.40), side="l"),

dict(src="IMG_4391", name="Flat-Coated Retriever", group="retriever",
  fam=["retriever","black"], page=258,
  height="22-24 in (56-61 cm)", weight="55-80 lb (25-36 kg)", life="11-13 years",
  origin="UK", colors=["Liver"],
  marks=["Shallow stop","Triangular, drop ears with rounded tips","Dense, black coat",
         "Feathering on chest","Well-feathered tail","Round, close-knit feet"],
  para="One of the earliest retriever breeds and once a gamekeeper's favourite. "
       "Today it is still worked but more often found as a good-natured and handsome "
       "pet. Lively and brimming with enthusiasm, but level-headed and obedient with "
       "it — and it has a deep bark, so it can actually guard.",
  tell="Dense flat black coat with a long, shallow-stopped head — no dome at all",
  hook="FLAT coat, FLAT head — the long-headed black retriever.",
  mark="SHALLOW STOP", anchor=(0.9,0.28), side="l"),

dict(src="IMG_4392", name="Chesapeake Bay Retriever", group="retriever",
  fam=["retriever","curly-water"], page=259,
  height="21-26 in (53-66 cm)", weight="55-80 lb (25-36 kg)", life="12-13 years",
  origin="USA", colors=["Straw bracken","Red-gold"],
  marks=["Moderate stop","Color of nose matches coat","Oily, brown double coat","Wavy coat",
         "Deep chest","Medium-length, slightly curved tail","Harelike feet",
         "Leg length equal to depth of body"],
  para="A retriever from the north-eastern United States with much in common with "
       "the Curly-Coated Retriever. A superb water dog with typical retriever "
       "gentleness but an alert and determined personality of its own. For anyone "
       "who can supply enough activity, it is intelligent and biddable.",
  tell="Oily wavy brown double coat with a nose that matches the coat exactly",
  hook="The OILY one — dead-grass brown, waterproof, nose matches coat.",
  mark="OILY BROWN COAT", whole=True, anchor=(0.48,0.42), side="l"),

dict(src="IMG_4393", name="Curly-Coated Retriever", group="retriever",
  fam=["retriever","curly-water"], page=259,
  height="25-27 in (64-69 cm)", weight="60-71 lb (27-32 kg)", life="12-13 years",
  origin="UK", colors=["Liver"],
  marks=["Small, triangular, drop ears","Thick, tightly curled, black coat",
         "Oval, black eyes match coat color","Smooth, short hair on head",
         "Tail almost reaches hock","Round feet with well-arched toes"],
  para="Bred for hunting waterfowl, this rare retriever is still worked, used as an "
       "assistance dog and kept as an affectionate, level-headed companion. High "
       "energy and a real need for company make it far better suited to rural life "
       "than to a flat in town.",
  tell="Tight crisp curls over the whole body but a SMOOTH short-haired head",
  hook="Curls everywhere, bald head — the tallest retriever of the lot.",
  mark="SMOOTH HEAD", anchor=(0.88,0.18), side="l"),

dict(src="IMG_4366", name="Nova Scotia Duck Tolling Retriever", group="retriever",
  fam=["retriever","gold","red-white"], page=243,
  height="18-21 in (45-53 cm)", weight="37-51 lb (17-23 kg)", life="12-13 years",
  origin="Canada", colors=[],
  marks=["Almond-shaped eyes have alert expression","Triangular drop ears held slightly erect",
         "Tapering muzzle with slightly wedge-shaped head","Close-fitting lips","Level back",
         "Water-repellent, red coat with dense undercoat","Typical white chest markings",
         "Well-feathered tail, broad at base","Typical white markings on feet"],
  para="Named for a strange job: the dog plays on the shore in full view of ducks "
       "and geese, retrieving thrown sticks with a great show of activity but never "
       "barking, and the display lures — 'tolls' — curious birds into gun range. "
       "Playful, quiet and obedient, and tireless enough to need serious exercise.",
  tell="Smallest retriever — foxy red with white on the feet, chest and tail tip",
  hook="The TOLLER — a fox-red retriever that dances birds into range.",
  say="TOLL-ing",
  mark="FOXY RED COAT", whole=True, anchor=(0.46,0.42), side="l"),
]
