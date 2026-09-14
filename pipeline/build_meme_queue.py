# -*- coding: utf-8 -*-
"""Turn memes_source.POSTS into queue-memes.json: dates, colours, captions."""
import json, datetime, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from memes_source import POSTS, D
from concepts import MEME_ROTATION

START = datetime.date(2026, 9, 15)          # dinsdag
DAYS = {1: "di 20:00", 3: "do 20:00", 5: "za 11:00"}
STANDING = ["#vrouwenonderelkaar", "#mijnpilnu"]
PAGES = "https://dakeyne-ship-it.github.io/mijnpil-media"


def slots(start, n):
    out, d = [], start
    while len(out) < n:
        if d.weekday() in DAYS:
            out.append((d, DAYS[d.weekday()]))
        d += datetime.timedelta(days=1)
    return out


def plain(lines):
    return " ".join(x.replace("<em>", "").replace("</em>", "") for x in lines)


def main():
    dates = slots(START, len(POSTS))
    posts = []
    for i, (src, lines, opener, share, tags, comment) in enumerate(POSTS):
        day, slot = dates[i]
        theme = MEME_ROTATION[i % len(MEME_ROTATION)]
        caption = f"{opener}\n\n{share}"
        pid = f"m{i+1:02d}"
        base = f"{PAGES}/ig/{day.year}/{day.month:02d}"
        posts.append({
            "id": pid,
            "source_line": src,
            "date": day.isoformat(),
            "slot": slot,
            "concept": "onder_ons",
            "format": "image",
            "theme": theme,
            "lines": lines,
            "subject": plain(lines),
            "caption": caption,
            "tags": tags + STANDING,
            "first_comment": comment,
            "alt": (f"{theme.capitalize()} vlak met de tekst: {plain(lines)} "
                    "Linksboven de hashtag vrouwen onder elkaar, linksonder het "
                    "logo van MijnPil.nu."),
            "story": True,
            "image_url": f"{base}/{pid}.jpg",
            "story_url": f"{base}/{pid}-story.mp4",
        })
    doc = {
        "_meta": {
            "brand": "mijnpil.nu",
            "pillar": "Onder ons",
            "written": "2026-09-13",
            "rhythm": "di 20:00 · do 20:00 · za 11:00, naast de uitlegqueue op ma/wo/vr",
            "layout": "vullend",
            "face": "slab",
            "anchor": "onder",
            "hashtag_position": "eyebrow",
            "standing_tags": STANDING,
            "disclaimer": D,
            "note": ("Elke post is één stille 4:5 plaat voor de feed plus dezelfde "
                     "plaat bewegend in 9:16 voor Stories. De kleur roteert vast, "
                     "zodat twee posts achter elkaar nooit hetzelfde vlak hebben."),
        },
        "posts": posts,
    }
    out = pathlib.Path(__file__).parent / "queue-memes.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(posts)} posts, {posts[0]['date']} t/m {posts[-1]['date']}")
    from collections import Counter
    print(Counter(p["theme"] for p in posts))


if __name__ == "__main__":
    main()
