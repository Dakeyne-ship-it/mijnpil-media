# -*- coding: utf-8 -*-
"""Bouwt het publicatiedocument van de uitlegpijler uit queue.json.
Uitvoer: docs/instagram-publiceerklaar-week-1-2.md (de naam die de geplande
taken kennen)."""
import json, pathlib, datetime

HERE = pathlib.Path(__file__).parent
REPO = HERE.parent
Q = json.loads((HERE / "queue.json").read_text(encoding="utf-8"))
PAGES = "https://dakeyne-ship-it.github.io/mijnpil-media/ig"
DAG = {0: "ma", 2: "wo", 4: "vr"}
ACTIE = {"reel": "create_video_post", "carousel": "create_carousel_post", "image": "create_image_post"}
DISC = Q["_meta"]["disclaimer"]


def urls(p):
    d = datetime.date.fromisoformat(p["date"])
    base = f"{PAGES}/{d.year}/{d.month:02d}/{p['id']}"
    if p["format"] == "reel":
        return [f"{base}.mp4"]
    if p["format"] == "image":
        return [f"{base}.jpg"]
    if p["concept"] == "anatomie":
        return [f"{base}__1-plaat.jpg", f"{base}__2-onthoud.jpg"]
    return [f"{base}__1-mythe.jpg", f"{base}__2-feit.jpg"]


posts = Q["posts"]
laatste = datetime.date.fromisoformat(posts[-1]["date"])
L = ["# Publiceerklaar: uitlegpijler\n\n",
     f"Bijgewerkt 25 september 2026. {len(posts)} posts, van 14 september 2026 tot en met "
     f"{laatste.day} januari {laatste.year}. Alle beeld is gerenderd en staat op de publieke host. "
     "Vrijdag 25 december en vrijdag 1 januari zijn bewust vrij.\n\n",
     "Publiceer **alleen** de post waarvan de datum gelijk is aan vandaag\n"
     "(Europe/Amsterdam). Staat die datum er niet bij, publiceer dan niets.\n\n",
     "Staat er bij een reel een **cover_url**, geef die mee als `cover_url` aan\n"
     "`create_video_post`. Zonder omslag pakt Instagram het eerste frame, en dat is\n"
     "een leeg kleurvlak. Gebruik nooit `cover_url` en `thumb_offset` tegelijk.\n\n",
     "Connector `instagram`, account `17841408082040893`. Plaats daarna de eerste\n"
     "reactie met `create_comment`, media_id is wat de publicatie teruggaf.\n"]

for p in posts:
    d = datetime.date.fromisoformat(p["date"])
    L.append(f"\n---\n\n## {p['date']} ({p['slot']}) · {p['subject']}\n\n")
    L.append(f"- **post_id:** `{p['id']}`\n- **format:** `{p['format']}`\n"
             f"- **Windsor-actie:** `{ACTIE[p['format']]}`\n")
    u = urls(p)
    if len(u) == 1:
        L.append(f"- **URL:**\n  - {u[0]}\n")
    else:
        L.append("- **URL's, in deze volgorde:**\n" + "".join(f"  - {x}\n" for x in u))
    if p["format"] == "reel" and (p.get("cover") or p["date"] >= "2026-09-25"):
        L.append(f"- **cover_url:** {PAGES}/{d.year}/{d.month:02d}/{p['id']}-cover.jpg\n")
    cap = p["caption"] + "\n\n" + " ".join(p["tags"])
    L.append("\n**Caption (letterlijk overnemen):**\n\n```\n" + cap + "\n```\n")
    if p.get("disclaimer"):
        L.append("\n**Eerste reactie eronder:**\n\n```\n" + DISC + "\n```\n")

out = REPO / "docs" / "instagram-publiceerklaar-week-1-2.md"
out.parent.mkdir(exist_ok=True)
out.write_text("".join(L), encoding="utf-8")
print(out, len(posts), "posts")
