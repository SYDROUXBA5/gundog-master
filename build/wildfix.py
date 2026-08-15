#!/usr/bin/env python3
"""Re-fetch the field photos that came back wrong or unusable.

The first pass took Commons' top search hit, which for some breeds is a costumed
pet, a head-only close-up, or a dog too distant to read. This pass gathers many
candidates per breed, scores them for "a whole dog, side on, legible", and
refuses any file already used by another breed.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from breeds import B
from wild import api, strip_html, OK_LIC, UA

OUT = os.path.join(HERE, "wild")
META = os.path.join(HERE, "wild.json")

REJECT = re.compile(
    r"(logo|map|icon|coat.of.arms|stamp|diagram|chart|skeleton|x.ray|"
    r"puppy|puppies|litter|costume|clothes|clothing|sweater|jacket|hat|"
    r"cartoon|drawing|painting|engraving|illustration|sculpture|statue|"
    r"grave|monument|sign|poster|book|cover)", re.I)
PREFER = re.compile(r"(standing|side|profile|field|outdoor|run|walk|show|full)", re.I)
# a title that names a different dog is a different dog, whatever it scores
CROSS = re.compile(r"(doodle|poo\b|cockapoo|labradoodle|goldendoodle|schnoodle|"
                   r"cross|mix|mongrel|hybrid)", re.I)
# the file must actually claim to be this breed
MUST = {
 "Cocker Spaniel": r"cocker",
 "Poodle (Standard)": r"poodle|caniche|pudel",
 "Corded Poodle": r"cord",
 "Barbet": r"barbet|barbocho",
 "Vizsla": r"vizsla",
 "Nova Scotia Duck Tolling Retriever": r"toll",
 "American Water Spaniel": r"water spaniel|\bAWS\b",
 "Ariege Pointing Dog": r"ari[eè]ge",
 "Cesky Fousek": r"fousek|bohemian",
 "French Gascony Pointer": r"gascogne|gascony",
 "Portuguese Pointer": r"portug",
 "Blue Picardy Spaniel": r"picard",
}
# and it must not be a lazy shot that teaches nothing
DEAD = re.compile(r"(asleep|sleeping|lying|laying|close.?up|head|portrait|muzzle|"
                  r"nose|eye|paw|tail)\b", re.I)

# breed -> search terms tuned to find a whole dog outdoors
RETRY = {
 "Cocker Spaniel": ["American Cocker Spaniel standing", "American Cocker Spaniel dog"],
 "Poodle (Standard)": ["Standard Poodle standing", "Caniche standard", "Standard Poodle black"],
 "Corded Poodle": ["Corded Poodle", "Poodle corded coat", "Puli-like corded poodle"],
 "Barbet": ["Barbet dog standing", "Barbet chien", "Barbet dog breed"],
 "Vizsla": ["Vizsla standing", "Magyar Vizsla dog", "Vizsla portrait dog"],
 "Nova Scotia Duck Tolling Retriever": ["Nova Scotia Duck Tolling Retriever standing",
                                        "Toller retriever dog"],
 "American Water Spaniel": ["American Water Spaniel dog", "American Water Spaniel standing"],
 "Ariege Pointing Dog": ["Braque de l'Ariege dog", "Braque de l'Ariege chien"],
 "Cesky Fousek": ["Cesky Fousek standing", "Cesky Fousek dog breed"],
 "French Gascony Pointer": ["Braque francais type Gascogne", "Braque francais grande taille"],
 "Portuguese Pointer": ["Perdigueiro Portugues standing", "Portuguese Pointer dog"],
 "Blue Picardy Spaniel": ["Epagneul bleu de Picardie chien", "Blue Picardy Spaniel dog"],
}


def score(p):
    ii = (p.get("imageinfo") or [{}])[0]
    w, h = ii.get("width", 0), ii.get("height", 0)
    if not w or not h:
        return -1
    s = 0.0
    ar = w / h
    s += 3.0 if 1.15 <= ar <= 1.9 else (-2.0 if ar < 0.85 else 0.0)  # landscape = whole dog
    s += min(w, 2600) / 1300.0
    if PREFER.search(p.get("title", "")):
        s += 1.2
    return s


def gather(term, limit=25):
    d = api({"action": "query", "generator": "search",
             "gsrsearch": f"filetype:bitmap {term}", "gsrnamespace": 6,
             "gsrlimit": limit, "prop": "imageinfo",
             "iiprop": "url|size|extmetadata", "iiurlwidth": 1000})
    return list((d.get("query", {}).get("pages", {}) or {}).values())


def main():
    meta = json.load(open(META))
    used = {v.get("title") for v in meta.values()}
    for name, terms in RETRY.items():
        b = next(x for x in B if x["name"] == name)
        used.discard(meta.get(b["src"], {}).get("title"))   # free its own old file
        best, bestscore = None, 0.0
        for t in terms:
            try:
                cands = gather(t)
            except Exception as e:
                print(f"  ! {name}: {e}")
                continue
            for p in cands:
                title = p.get("title", "")
                if REJECT.search(title) or CROSS.search(title) or title in used:
                    continue
                if DEAD.search(title):
                    continue
                must = MUST.get(name)
                if must and not re.search(must, title, re.I):
                    continue
                ii = (p.get("imageinfo") or [{}])[0]
                if not ii.get("thumburl") or ii.get("width", 0) < 800:
                    continue
                ex = ii.get("extmetadata", {})
                lic = strip_html(ex.get("LicenseShortName", {}).get("value", ""))
                if not OK_LIC.match(lic):
                    continue
                sc = score(p)
                if sc > bestscore:
                    by = strip_html(ex.get("Artist", {}).get("value", "")) or "Unknown"
                    best, bestscore = ({
                        "title": title, "thumb": ii["thumburl"],
                        "by": (by[:57] + "…") if len(by) > 60 else by, "lic": lic,
                        "licUrl": strip_html(ex.get("LicenseUrl", {}).get("value", "")),
                        "src": ii.get("descriptionurl", "")}, sc)
            time.sleep(0.4)
        if not best:
            print(f"MISS {name}")
            continue
        req = urllib.request.Request(best["thumb"], headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=45) as r:
            open(os.path.join(OUT, b["src"] + ".jpg"), "wb").write(r.read())
        meta[b["src"]] = {k: best[k] for k in ("by", "lic", "licUrl", "src", "title")}
        used.add(best["title"])
        print(f"{name:38} {bestscore:4.1f}  {best['lic']:16} {best['title'][5:60]}")
        json.dump(meta, open(META, "w"), ensure_ascii=False, indent=1)
        time.sleep(0.4)


if __name__ == "__main__":
    main()
