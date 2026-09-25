# -*- coding: utf-8 -*-
"""Render queue-memes.json into the project document the scheduled runs read."""
import json, pathlib, datetime

HERE = pathlib.Path(__file__).parent
Q = json.loads((HERE / "queue-memes.json").read_text(encoding="utf-8"))
M = Q["_meta"]
DAY = {1: "dinsdag", 3: "donderdag", 5: "zaterdag"}
MON = {9: "september", 10: "oktober", 11: "november", 12: "december", 1: "januari",
       2: "februari"}
P = Q["posts"]
last = datetime.date.fromisoformat(P[-1]["date"])

L = ["# Onder ons, publiceerklaar\n\n",
     "De dinsdag-, donderdag- en zaterdagslots van @mijnpil.nu. Bijgewerkt 25 september\n"
     f"2026. Loopt tot en met {last.day} {MON[last.month]} {last.year}. De uitlegqueue op maandag,\n"
     "woensdag en vrijdag staat hier los van en heeft zijn eigen document.\n\n",
     "In deze slots staan drie soorten posts: memes (Onder ons, id begint met m),\n"
     "inhakers (id begint met i) en drie posts die bovenaan het profiel worden\n"
     "vastgepind (id begint met p). Per post staat hieronder precies wat er moet gebeuren.\n\n",
     "Alle beelden en stories staan al op de beeldhost. Er hoeft niets gebouwd of\n"
     "gepusht te worden. De werkomgeving kan de host zelf niet bereiken, dus een\n"
     "mislukte curl zegt niets: Instagram haalt de bestanden wel op.\n\n",
     "## Vaste werkwijze per post\n\n",
     "1. Zoek hieronder het kopje met de datum van vandaag in Europe/Amsterdam.\n"
     "   Staat die datum er niet, dan is er vandaag niets te doen.\n"
     "2. Feed: connector `instagram`, account `17841408082040893`. Gebruik de actie\n"
     "   die bij de post staat (`create_image_post` of `create_carousel_post`) met de\n"
     "   URL's en de letterlijke caption.\n"
     "3. Staat er een eerste reactie bij, plaats die direct met `create_comment`,\n"
     "   media_id is wat stap 2 teruggaf.\n"
     "4. Staat er een story bij: actie `create_story` met video_url. Stories kennen\n"
     "   geen caption. Mislukt de story, laat de feedpost dan staan en meld alleen de\n"
     "   story. Staat er geen story bij, sla deze stap over.\n"
     "5. Staat er bij de post \"vastpinnen\", meld dan in de pushmelding dat Alexander\n"
     "   deze post handmatig bovenaan het profiel moet vastzetten. De API kan niet pinnen.\n\n",
     f"Vaste hashtags: {' '.join(M['standing_tags'])}. Die staan al in elke caption\n"
     "hieronder, dus neem de caption letterlijk over en voeg niets toe.\n\n",
     "---\n"]

cur = None
for p in P:
    d = datetime.date.fromisoformat(p["date"])
    if (d.year, d.month) != cur:
        cur = (d.year, d.month)
        L.append(f"\n# {MON[d.month]} {d.year}\n")
    cap = p["caption"] + "\n\n" + " ".join(p["tags"])
    L.append(f"\n## {p['date']} · {p['id']} · {DAY[d.weekday()]} {p['slot'].split()[-1]}\n")
    if p["concept"] == "onder_ons":
        L.append(f"Meme. Kleur: {p['theme']}. Regel: {p['subject']}\n")
    elif p["concept"] == "inhaker":
        L.append(f"Inhaker. {p['subject']}\n")
    else:
        L.append(f"Vastpinnen. {p['subject']}. Na publicatie handmatig bovenaan het profiel vastzetten.\n")
    if p["format"] == "carousel":
        L.append("- Feed, `create_carousel_post`, image_urls in deze volgorde:\n")
        L += [f"  - {u}\n" for u in p["image_urls"]]
    else:
        L.append(f"- Feed, `create_image_post`\n  image_url: {p['image_url']}\n")
    if p.get("story"):
        L.append(f"- Story, `create_story`\n  video_url: {p['story_url']}\n")
    else:
        L.append("- Geen story.\n")
    L.append("\n**Caption, letterlijk**\n\n```\n" + cap + "\n```\n")
    if p.get("first_comment"):
        L.append("\n**Eerste reactie eronder**\n\n```\n" + p["first_comment"] + "\n```\n")
    else:
        L.append("\nGeen eerste reactie. Deze post doet geen medische uitspraak.\n")

out = HERE / "onder-ons-publiceerklaar.md"
out.write_text("".join(L), encoding="utf-8")
print(out, out.stat().st_size // 1024, "kB")
