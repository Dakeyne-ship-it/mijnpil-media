# -*- coding: utf-8 -*-
"""Render queue-memes.json into the project document the scheduled runs read."""
import json, pathlib, datetime

HERE = pathlib.Path(__file__).parent
Q = json.loads((HERE / "queue-memes.json").read_text(encoding="utf-8"))
M = Q["_meta"]
DAY = {1: "dinsdag", 3: "donderdag", 5: "zaterdag"}
MON = {9: "september", 10: "oktober", 11: "november", 12: "december", 1: "januari"}

L = ["# Onder ons, publiceerklaar\n",
     "De memepijler van @mijnpil.nu. Negenenvijftig posts, drie per week op\n"
     "dinsdag, donderdag en zaterdag, van 15 september 2026 tot en met\n"
     "28 januari 2027. De uitlegqueue op maandag, woensdag en vrijdag staat hier\n"
     "los van en heeft zijn eigen document.\n",
     "Alle beelden en stories staan al op de beeldhost. Er hoeft niets gebouwd of\n"
     "gepusht te worden. De werkomgeving kan de host zelf niet bereiken, dus een\n"
     "mislukte curl zegt niets: Instagram haalt de bestanden wel op.\n",
     "## Vaste werkwijze per post\n",
     "1. Zoek hieronder het kopje met de datum van vandaag in Europe/Amsterdam.\n"
     "   Staat die datum er niet, dan is er vandaag geen memepost.\n"
     "2. Feed: connector `instagram`, account `17841408082040893`, actie\n"
     "   `create_image_post` met image_url en de letterlijke caption.\n"
     "3. Staat er een eerste reactie bij, plaats die direct met `create_comment`,\n"
     "   media_id is wat stap 2 teruggaf.\n"
     "4. Story: actie `create_story` met video_url. Stories kennen geen caption.\n"
     "   Mislukt de story, laat de feedpost dan staan en meld alleen de story.\n",
     f"Vaste hashtags: {' '.join(M['standing_tags'])}. Die staan al in elke caption\n"
     "hieronder, dus neem de caption letterlijk over en voeg niets toe.\n",
     "---\n"]

cur = None
for p in Q["posts"]:
    d = datetime.date.fromisoformat(p["date"])
    if (d.year, d.month) != cur:
        cur = (d.year, d.month)
        L.append(f"\n# {MON[d.month]} {d.year}\n")
    cap = p["caption"] + "\n\n" + " ".join(p["tags"])
    L.append(f"\n## {p['date']} · {p['id']} · {DAY[d.weekday()]} {p['slot'].split()[-1]}\n")
    L.append(f"Kleur: {p['theme']}. Regel: {p['subject']}\n")
    L.append(f"- Feed, `create_image_post`\n  image_url: {p['image_url']}\n")
    L.append(f"- Story, `create_story`\n  video_url: {p['story_url']}\n")
    L.append("\n**Caption, letterlijk**\n\n```\n" + cap + "\n```\n")
    if p["first_comment"]:
        L.append("\n**Eerste reactie eronder**\n\n```\n" + p["first_comment"] + "\n```\n")
    else:
        L.append("\nGeen eerste reactie. Deze post doet geen medische uitspraak.\n")

out = HERE / "onder-ons-publiceerklaar.md"
out.write_text("".join(L), encoding="utf-8")
print(out, out.stat().st_size // 1024, "kB")
