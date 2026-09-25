"""Render one or more queue entries into finished Instagram assets.

    python3 produce.py w01-ma w01-wo ...
    python3 produce.py --until 2026-09-25

Output lands in out/production/<id>/ and is named after the post id, which is
also the filename that ends up in the media repository.
"""
import json, sys, pathlib, shutil
from playwright.sync_api import sync_playwright
import concepts as C
import illu
from anim import render_clip, encode, HTML, OUT, FPS

HERE = pathlib.Path(__file__).parent
QUEUE = json.loads((HERE / "queue.json").read_text(encoding="utf-8"))
_MEMES = HERE / "queue-memes.json"
if _MEMES.exists():
    QUEUE["posts"] = QUEUE["posts"] + json.loads(_MEMES.read_text(encoding="utf-8"))["posts"]
PROD = OUT / "production"
PROD.mkdir(parents=True, exist_ok=True)

FEED = (1080, 1350)   # 4:5 feed and carousel
VERT = (1080, 1920)   # 9:16 reel and story

# Closing takeaways for the Anatomie carousel, per diagram variant.
ANATOMIE_SLOT2 = {
    "strip28": ("De bloeding in je<br>stopweek is <em>geen<br>menstruatie</em>.",
                "Er is geen eisprong geweest. Het is een onttrekkingsbloeding, "
                "en daarom kun je die week overslaan zonder dat er iets misgaat."),
    "spiraal": ("Ongeveer <em>drie<br>centimeter</em>, en<br>jarenlang betrouwbaar.",
                "Je hoeft er niets voor te onthouden. Dat maakt hem in de praktijk "
                "een van de betrouwbaarste vormen die er zijn."),
    "pleister": ("Drie weken plakken,<br>één week <em>niet</em>.",
                 "Geen dagelijks tijdstip om te onthouden, en misselijkheid of "
                 "braken maakt niets uit voor de opname."),
    "ring": ("Drie weken <em>in</em>,<br>één week <em>uit</em>.",
             "Je hoeft niet elke dag iets te onthouden. Valt hij eruit, spoel hem dan af met "
             "lauw water en doe hem binnen drie uur terug."),
    "minipil": ("Geen <em>stopweek</em>,<br>geen pauze.",
                "Je bloedingen kunnen daardoor onregelmatig zijn of helemaal wegblijven. Dat is "
                "bij de minipil normaal en geen teken dat hij minder goed werkt."),
}


def shot(browser, name, html, size):
    """Render one static page to a JPEG and return its path."""
    f = HTML / f"{name}.html"
    f.write_text(html, encoding="utf-8")
    pg = browser.new_page(viewport={"width": size[0], "height": size[1]})
    pg.goto(f"file://{f}")
    pg.wait_for_timeout(400)
    out = PROD / name.split("__")[0] / f"{name}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    pg.screenshot(path=str(out), type="jpeg", quality=93)
    pg.close()
    return out


def clip(browser, post_id, name, scenes, size, cover=False):
    """Render a list of (html, duration) scenes into one MP4.

    cover=True also writes <name>-cover.jpg: the last frame of the first scene,
    when everything in it has landed. Reels pass that as cover_url, because
    Instagram otherwise takes frame 0, which is an empty field."""
    dirs = []
    for i, (html, dur) in enumerate(scenes):
        d, _ = render_clip(browser, f"{name}_{i}", html, dur, size[0], size[1])
        dirs.append(d)
    if cover:
        last = sorted(dirs[0].glob("*.jpg"))[-1]
        cv = PROD / post_id / f"{name}-cover.jpg"
        cv.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(last, cv)
    mp4 = encode(dirs, name)
    dest = PROD / post_id / f"{name}.mp4"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(mp4), dest)
    for d in dirs:
        shutil.rmtree(d, ignore_errors=True)
    return dest


def build(browser, p):
    """Render one queue entry. Returns the list of asset paths, in order."""
    pid, concept, fmt = p["id"], p["concept"], p["format"]

    if concept == "klare_taal":
        scenes = [C.reel_scene_v(s["kind"], s["lines"], s.get("small", ""), w=VERT[0], h=VERT[1])
                  for s in p["scenes"]]
        return [clip(browser, pid, pid, scenes, VERT, cover=True)]

    if concept == "mythe_feit":
        return [
            shot(browser, f"{pid}__1-mythe", C.mythe(p["mythe_lines"], "1 / 2", w=FEED[0], h=FEED[1]), FEED),
            shot(browser, f"{pid}__2-feit",
                 C.feit(p["feit_statement"], p["feit_source"], "2 / 2", w=FEED[0], h=FEED[1]), FEED),
        ]

    if concept == "de_vraag":
        if fmt == "image":
            return [shot(browser, pid,
                         C.de_vraag_img(p["kicker"], p["lines"],
                                        field=p.get("field", "var(--mint)"), w=FEED[0], h=FEED[1]), FEED)]
        return [clip(browser, pid, pid,
                     [C.de_vraag_v(p["kicker"], p["lines"],
                                   field=p.get("field", "var(--mint)"), w=VERT[0], h=VERT[1])], VERT, cover=True)]

    if concept == "anatomie":
        v = p["variant"]
        take, sub = ANATOMIE_SLOT2[v]
        return [
            shot(browser, f"{pid}__1-plaat", C.anatomie(v, w=FEED[0], h=FEED[1]), FEED),
            shot(browser, f"{pid}__2-onthoud", C.anatomie_slot2(take, sub, w=FEED[0], h=FEED[1]), FEED),
        ]

    if concept == "de_cyclus":
        return [clip(browser, pid, pid,
                     [C.cyclus_v(p.get("variant", "hormonen"),
                                 w=VERT[0], h=VERT[1])], VERT, cover=True)]

    if concept == "onder_ons":
        if p.get("style") == "briefje":
            out = [shot(browser, f"{pid}-a", C.briefje(p["lines"], p["theme"])[0], FEED)]
            html, dur = C.briefje(p["lines"], p["theme"], anim=True, w=VERT[0], h=VERT[1])
            out.append(clip(browser, pid, f"{pid}-a-story", [(html, dur)], VERT))
            return out
        out = [shot(browser, pid,
                    C.onder_ons(p["lines"], "vullend", p["theme"],
                                w=FEED[0], h=FEED[1], tag="eyebrow",
                                face="slab", anchor="onder", border=16), FEED)]
        if p.get("story"):
            out.append(clip(browser, pid, f"{pid}-story",
                            [C.onder_ons_v(p["lines"], "vullend", p["theme"],
                                           w=VERT[0], h=VERT[1], tag="eyebrow",
                                           face="slab", anchor="onder",
                                           border=16)], VERT))
        return out

    if concept == "inhaker":
        return [shot(browser, pid, C.de_vraag_img(p["kicker"], p["lines"], field=p["field"],
                                                  w=FEED[0], h=FEED[1]), FEED),
                clip(browser, pid, f"{pid}-story",
                     [C.de_vraag_v(p["kicker"], p["lines"], field=p["field"],
                                   note="het antwoord staat in onze nieuwste post",
                                   w=VERT[0], h=VERT[1])], VERT)]

    if concept == "vast":
        n = 1 + len(p["slides"])
        out = [shot(browser, f"{pid}__1", C.vast_cover(p["kicker"], p["lines"], p["theme"]), FEED)]
        for k, sl in enumerate(p["slides"]):
            num, title, body = sl[:3]
            if len(sl) > 3:
                img, _ = illu.in_vak(sl[3], FEED[0], 700)
                html = C.vast_slide_beeld(num, title, body, img, f"{k+2} / {n}")
            else:
                html = C.vast_slide(num, title, body, f"{k+2} / {n}")
            out.append(shot(browser, f"{pid}__{k+2}", html, FEED))
        return out

    if concept == "uit_de_dm":
        return [clip(browser, pid, pid,
                     [C.uit_de_dm_v(p["vraag"], p["antwoord"], w=VERT[0], h=VERT[1])], VERT,
                     cover=True)]

    raise ValueError(f"unknown concept: {concept}")


KICKER = {"klare_taal": "klare taal", "uit_de_dm": "uit de dm", "de_cyclus": "de cyclus"}


def omslag(browser, p):
    """Reelomslag: illustratie uit de bibliotheek, titel onder een boog.
    Overschrijft de omslag uit het laatste frame die clip() heeft gemaakt."""
    img, bg = illu.in_vak(p["cover"]["img"], VERT[0], 900)
    html = C.beeld_pil(img, bg, KICKER[p["concept"]], p["cover"]["lines"], vorm="boog")
    f = HTML / f"{p['id']}-cover.html"
    f.write_text(html, encoding="utf-8")
    pg = browser.new_page(viewport={"width": VERT[0], "height": VERT[1]})
    pg.goto(f"file://{f}")
    pg.wait_for_timeout(400)
    out = PROD / p["id"] / f"{p['id']}-cover.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    pg.screenshot(path=str(out), type="jpeg", quality=92)
    pg.close()
    return out


def main():
    args = sys.argv[1:]
    posts = QUEUE["posts"]
    if "--until" in args:
        cut = args[args.index("--until") + 1]
        want = [p for p in posts if p["date"] <= cut]
    elif [a for a in args if not a.startswith("--")]:
        want = [p for p in posts if p["id"] in args]
    else:
        want = posts

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        alleen_omslag = "--omslag" in args
        for p in want:
            if alleen_omslag:
                paths = [omslag(b, p)] if p.get("cover") else []
            else:
                paths = build(b, p)
                if p.get("cover"):
                    paths.append(omslag(b, p))
            print(f"{p['id']:8s} {p['concept']:12s} {p['format']:9s} "
                  f"{p['subject']}")
            for path in paths:
                print(f"           {path.relative_to(PROD)}  "
                      f"{path.stat().st_size/1024:.0f} kB")
        b.close()


if __name__ == "__main__":
    main()
