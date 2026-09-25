# -*- coding: utf-8 -*-
"""Bouwt queue-memes.json voor de dinsdag/donderdag/zaterdag-slots.

Versie 2, 25 september 2026:
- m01 t/m m05 staan live en blijven zoals ze waren (oude stijl).
- vanaf 26 september: stijl H "het briefje" (richting A).
- volgorde op thema: geen thema twee keer binnen drie memes, en geen meme over een
  onderwerp waar de uitlegpijler (of een inhaker) diezelfde week over gaat.
- inhakers en de drie vast te pinnen posts staan op vaste data in memeslots.
- kleur per meme op basis van de buren in het raster (posities -1, -3, +1, +3
  en -6 in de chronologische reeks), niet op basis van de weekdag.
"""
import json, datetime, pathlib, sys
from collections import Counter
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from memes_source import POSTS
from inhakers import INHAKERS, VAST

DAYS = {1: "di 20:00", 3: "do 20:00", 5: "za 11:00"}
STANDING = ["#vrouwenonderelkaar", "#mijnpilnu"]
PAGES = "https://dakeyne-ship-it.github.io/mijnpil-media"
START = datetime.date(2026, 9, 26)
LIVE_IDS = ("m01", "m02", "m03", "m04", "m05")
OLD = json.loads((HERE / "queue-memes.json").read_text(encoding="utf-8"))
LIVE = [p for p in OLD["posts"] if p["id"] in LIVE_IDS]
if len(LIVE) != 5:
    raise SystemExit("verwacht m01 t/m m05 uit de oude queue")

THEMA = {
    "Stopweek": [7], "Menstruatie dagelijks": [6, 34, 35, 41, 44],
    "Pil kwijt of vergeten": [8, 9, 10, 11, 12],
    "Voorraad en herhaalrecept": [13, 14, 15, 16, 17, 18, 20, 43],
    "Tampons en cup": [19, 21, 22, 23, 24, 42, 56, 57, 58, 59],
    "Krampen": [25, 26, 27, 28, 29, 30, 40],
    "Hormonen en humeur": [31, 32, 33, 45, 46, 47, 48, 49, 50, 51],
    "Op reis": [36, 37, 38, 39], "Herinneringen": [52, 53, 54, 55],
}
MID = {k: [f"m{n:02d}" for n in v] for k, v in THEMA.items()}
THEMA_VAN = {m: k for k, v in MID.items() for m in v}

# per maandag van de week: memethema's die botsen met uitleg of inhaker
BOTS = {
    "2026-09-28": {"Pil kwijt of vergeten"},
    "2026-10-05": {"Stopweek", "Menstruatie dagelijks"},
    "2026-10-12": {"Hormonen en humeur"},
    "2026-10-19": {"Herinneringen", "Pil kwijt of vergeten"},
    "2026-10-26": {"Pil kwijt of vergeten"},
    "2026-11-02": {"Hormonen en humeur", "Stopweek"},
    "2026-12-07": {"Stopweek"},
}

UITLEG_KLEUR = {"klare_taal": "indigo", "mythe_feit": "zalm", "anatomie": "papier",
                "de_cyclus": "papier", "uit_de_dm": "lichtblauw"}
VELD = {"var(--mint)": "mint", "var(--peach)": "perzik", "var(--sky)": "lichtblauw",
        "var(--blush)": "zalm"}
PALET = ["roze", "indigo", "lavendel", "perzik"]


def slots(start, n):
    out, d = [], start
    while len(out) < n:
        if d.weekday() in DAYS:
            out.append(d)
        d += datetime.timedelta(days=1)
    return out


def maandag(d):
    return (d - datetime.timedelta(days=d.weekday())).isoformat()


def plain(lines):
    return " ".join(x.replace("<em>", "").replace("</em>", "") for x in lines)


def main():
    src = {f"m{i+1:02d}": row for i, row in enumerate(POSTS)}
    vast = {x["date"]: x for x in INHAKERS + VAST}
    rest = {k: [m for m in v if m not in LIVE_IDS] for k, v in MID.items()}
    totaal = {k: len(v) for k, v in rest.items()}
    n_memes = sum(totaal.values())
    dates = slots(START, n_memes + len(vast))

    # 1. volgorde: per open slot het thema met de grootste achterstand
    geplaatst, plan, laatste, k_meme = Counter(), [], [], 0
    for d in dates:
        if d.isoformat() in vast:
            plan.append((d, vast[d.isoformat()]["id"]))
            continue
        verboden = BOTS.get(maandag(d), set())

        def score(k):
            s = (k_meme + 1) * totaal[k] / n_memes - geplaatst[k]
            if k in laatste[-2:]:
                s -= 100
            if k in verboden:
                s -= 1000
            return s
        k = max((k for k in rest if rest[k]), key=score)
        plan.append((d, rest[k].pop(0)))
        geplaatst[k] += 1
        k_meme += 1
        laatste.append(k)

    # 2. kleur op rasterpositie; vast te pinnen posts verhuizen naar de
    #    bovenste rij en tellen daarom niet mee in de reeks
    uitleg = json.loads((HERE / "queue.json").read_text(encoding="utf-8"))["posts"]
    reeks = []
    for p in uitleg:
        c = (VELD.get(p.get("field"), "mint") if p["concept"] == "de_vraag"
             else UITLEG_KLEUR[p["concept"]])
        reeks.append((p["date"], 0, p["id"], c))
    reeks += [(p["date"], 1, p["id"], p["theme"]) for p in LIVE]
    for d, pid in plan:
        if pid.startswith("p"):
            continue
        c = VELD.get(vast[d.isoformat()]["field"]) if pid.startswith("i") else None
        reeks.append((d.isoformat(), 1, pid, c))
    reeks.sort()
    kleur = [c for *_, c in reeks]
    ids = [r[2] for r in reeks]
    gebruikt = Counter()
    for i, c in enumerate(kleur):
        if c is not None:
            continue
        buren = {kleur[j] for j in (i - 1, i - 3, i + 1, i + 3, i - 6) if 0 <= j < len(kleur)}
        keus = [x for x in PALET if x not in buren] or PALET
        keus.sort(key=lambda x: (gebruikt[x], PALET.index(x)))
        kleur[i] = keus[0]
        gebruikt[keus[0]] += 1
    kleur_van = dict(zip(ids, kleur))

    # 3. queue
    posts = list(LIVE)
    for d, pid in plan:
        slot = DAYS[d.weekday()]
        base = f"{PAGES}/ig/{d.year}/{d.month:02d}"
        if pid.startswith("m"):
            _, lines, opener, share, tags, comment = src[pid]
            posts.append({
                "id": pid, "date": d.isoformat(), "slot": slot, "concept": "onder_ons",
                "style": "briefje", "format": "image", "thema": THEMA_VAN[pid],
                "theme": kleur_van[pid], "lines": lines, "subject": plain(lines),
                "caption": f"{opener}\n\n{share}", "tags": tags + STANDING,
                "first_comment": comment, "story": True,
                "image_url": f"{base}/{pid}-a.jpg", "story_url": f"{base}/{pid}-a-story.mp4",
            })
        else:
            x = dict(vast[d.isoformat()])
            x["slot"] = slot
            if pid.startswith("i"):
                x.update({"concept": "inhaker", "format": "image", "story": True,
                          "image_url": f"{base}/{pid}.jpg",
                          "story_url": f"{base}/{pid}-story.mp4"})
            else:
                x.update({"concept": "vast", "format": "carousel", "story": False,
                          "image_urls": [f"{base}/{pid}__{k+1}.jpg"
                                         for k in range(1 + len(x["slides"]))]})
            posts.append(x)

    meta = dict(OLD["_meta"])
    meta.update(written="2026-09-25", style="briefje (richting A)",
                note=("Vanaf 26 september in stijl H, het briefje. Volgorde op thema, kleur op "
                      "rasterpositie. Inhakers en de drie vast te pinnen posts staan in memeslots."))
    for k in ("layout", "face", "anchor", "border", "hashtag_position"):
        meta.pop(k, None)
    (HERE / "queue-memes.json").write_text(
        json.dumps({"_meta": meta, "posts": posts}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(posts)} items, t/m {posts[-1]['date']}")
    print(Counter(p["theme"] for p in posts if p.get("style") == "briefje"))
    for p in posts[5:]:
        print(p["date"], p["slot"][:2], p["id"], p.get("thema", p["concept"]), p.get("theme", ""))


if __name__ == "__main__":
    main()
