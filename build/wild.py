#!/usr/bin/env python3
"""Fetch one field photograph per breed from Wikimedia Commons.

The cut-out plate teaches the standard; the field photo teaches the dog as it
actually looks in the world. Working Master carries one per breed and this is
the same field (`wild`), so the engine already knows how to render it.

Only freely-licensed files are kept, and the author, licence and file page are
stored with each image so the app can show the credit on the reveal.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from breeds import B

OUT = os.path.join(HERE, "wild")
META = os.path.join(HERE, "wild.json")
API = "https://commons.wikimedia.org/w/api.php"
UA = "GundogMaster/1.0 (personal study tool; contact@naifubushcraft.com)"

OK_LIC = re.compile(r"(^CC0|^CC BY|^Public domain|^PD|^GFDL)", re.I)
BAD_FILE = re.compile(r"(logo|map|icon|coat.of.arms|stamp|diagram|chart|"
                      r"skeleton|x.ray|puppy|puppies|litter)", re.I)

# Commons indexes many of these under their native names; the English book name
# alone finds nothing for several French and Dutch breeds.
ALIAS = {
 "Cocker Spaniel": ["American Cocker Spaniel"],
 "English Cocker Spaniel": ["English Cocker Spaniel"],
 "German Spaniel": ["Deutscher Wachtelhund", "German Spaniel"],
 "Clumber Spaniel": ["Clumber Spaniel"],
 "Field Spaniel": ["Field Spaniel"],
 "Sussex Spaniel": ["Sussex Spaniel"],
 "Boykin Spaniel": ["Boykin Spaniel"],
 "English Springer Spaniel": ["English Springer Spaniel"],
 "Welsh Springer Spaniel": ["Welsh Springer Spaniel"],
 "American Water Spaniel": ["American Water Spaniel"],
 "Irish Water Spaniel": ["Irish Water Spaniel"],
 "Pont-Audemer Spaniel": ["Epagneul de Pont-Audemer", "Pont-Audemer Spaniel"],
 "Nederlandse Kooikerhondje": ["Kooikerhondje"],
 "Picardy Spaniel": ["Epagneul picard", "Picardy Spaniel"],
 "Blue Picardy Spaniel": ["Epagneul bleu de Picardie", "Blue Picardy Spaniel"],
 "French Spaniel": ["Epagneul francais", "French Spaniel"],
 "Spanish Water Dog": ["Spanish Water Dog", "Perro de agua espanol"],
 "Poodle (Standard)": ["Standard Poodle"],
 "Corded Poodle": ["Corded Poodle", "Standard Poodle"],
 "Portuguese Water Dog": ["Portuguese Water Dog"],
 "Barbet": ["Barbet dog", "Barbet (dog)"],
 "Frisian Water Dog": ["Wetterhoun"],
 "Lagotto Romagnolo": ["Lagotto Romagnolo"],
 "Brittany": ["Brittany dog", "Epagneul Breton"],
 "Small Munsterlander Pointer": ["Small Munsterlander"],
 "Large Munsterlander": ["Large Munsterlander"],
 "Frisian Pointing Dog": ["Stabyhoun"],
 "Drentsche Partridge Dog": ["Drentse Patrijshond"],
 "Cesky Fousek": ["Cesky Fousek", "Bohemian Wire-haired Pointing Griffon"],
 "Wirehaired Pointing Griffon": ["Korthals Griffon", "Wirehaired Pointing Griffon"],
 "German Shorthaired Pointer": ["German Shorthaired Pointer"],
 "Weimaraner": ["Weimaraner"],
 "Vizsla": ["Vizsla dog", "Magyar Vizsla"],
 "Wirehaired Vizsla": ["Wirehaired Vizsla"],
 "Portuguese Pointer": ["Perdigueiro Portugues", "Portuguese Pointer"],
 "Bracco Italiano": ["Bracco Italiano"],
 "Spinone Italiano": ["Spinone Italiano"],
 "French Pyrenean Pointer": ["Braque francais Pyrenees", "French Pyrenean Pointer"],
 "French Gascony Pointer": ["Braque francais Gascogne", "French Gascony Pointer"],
 "Saint Germain Pointer": ["Braque Saint-Germain"],
 "Bourbonnais Pointing Dog": ["Braque du Bourbonnais"],
 "Auvergne Pointer": ["Braque d'Auvergne"],
 "Ariege Pointing Dog": ["Braque de l'Ariege"],
 "Pudelpointer": ["Pudelpointer"],
 "Slovakian Rough-haired Pointer": ["Slovensky hrubosrsty stavac", "Slovakian Rough-haired Pointer"],
 "Pointer": ["English Pointer"],
 "Spanish Pointer": ["Perdiguero de Burgos"],
 "Old Danish Pointer": ["Gammel Dansk Honsehund", "Old Danish Pointer"],
 "English Setter": ["English Setter"],
 "Irish Setter": ["Irish Setter"],
 "Irish Red and White Setter": ["Irish Red and White Setter"],
 "Gordon Setter": ["Gordon Setter"],
 "Labrador Retriever": ["Labrador Retriever"],
 "Golden Retriever": ["Golden Retriever"],
 "Flat-Coated Retriever": ["Flat-Coated Retriever"],
 "Chesapeake Bay Retriever": ["Chesapeake Bay Retriever"],
 "Curly-Coated Retriever": ["Curly Coated Retriever"],
 "Nova Scotia Duck Tolling Retriever": ["Nova Scotia Duck Tolling Retriever"],
}


def api(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def strip_html(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def candidates(term, limit=14):
    d = api({"action": "query", "generator": "search",
             "gsrsearch": f'filetype:bitmap {term}', "gsrnamespace": 6,
             "gsrlimit": limit, "prop": "imageinfo",
             "iiprop": "url|size|extmetadata", "iiurlwidth": 1000})
    return list((d.get("query", {}).get("pages", {}) or {}).values())


def pick(term):
    for p in sorted(candidates(term), key=lambda x: x.get("index", 99)):
        title = p.get("title", "")
        if BAD_FILE.search(title):
            continue
        ii = (p.get("imageinfo") or [{}])[0]
        if not ii.get("thumburl"):
            continue
        if ii.get("width", 0) < 640:
            continue
        ex = ii.get("extmetadata", {})
        lic = strip_html(ex.get("LicenseShortName", {}).get("value", ""))
        if not OK_LIC.match(lic):
            continue
        by = strip_html(ex.get("Artist", {}).get("value", "")) or "Unknown"
        if len(by) > 60:
            by = by[:57].rstrip() + "…"
        return {"title": title, "thumb": ii["thumburl"],
                "by": by, "lic": lic,
                "licUrl": strip_html(ex.get("LicenseUrl", {}).get("value", "")),
                "src": ii.get("descriptionurl", "")}
    return None


def main():
    os.makedirs(OUT, exist_ok=True)
    meta = json.load(open(META)) if os.path.exists(META) else {}
    todo = [b for b in B if b["src"] not in meta]
    print(f"{len(meta)} already done, {len(todo)} to fetch")
    for i, b in enumerate(todo, 1):
        terms = ALIAS.get(b["name"], [b["name"]])
        hit = None
        for t in terms:
            try:
                hit = pick(t)
            except Exception as e:
                print(f"  ! {b['name']} / {t}: {e}")
                hit = None
            if hit:
                break
            time.sleep(0.4)
        if not hit:
            print(f"[{i}/{len(todo)}] MISS {b['name']}")
            continue
        try:
            req = urllib.request.Request(hit["thumb"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                open(os.path.join(OUT, b["src"] + ".jpg"), "wb").write(r.read())
        except Exception as e:
            print(f"[{i}/{len(todo)}] DL FAIL {b['name']}: {e}")
            continue
        meta[b["src"]] = {k: hit[k] for k in ("by", "lic", "licUrl", "src", "title")}
        print(f"[{i}/{len(todo)}] {b['name']:38} {hit['lic']:18} {hit['by'][:30]}")
        json.dump(meta, open(META, "w"), ensure_ascii=False, indent=1)
        time.sleep(0.5)
    print("total:", len(meta), "/", len(B))


if __name__ == "__main__":
    main()
