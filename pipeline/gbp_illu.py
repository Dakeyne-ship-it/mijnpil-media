# -*- coding: utf-8 -*-
"""GBP-posts met een illustratie uit library/illustraties.

    python3 gbp_illu.py              alle posts met een illustratie
    python3 gbp_illu.py 2026-11-09   losse datums


Zelfde uitgangspunt als gbp_object.py: één beeld, groot, leesbaar op 250 px,
met hooguit een kort label. De illustratie staat op haar eigen doorgetrokken
vlak, het label in een indigo pil onderaan. 1200 x 900."""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
import illu

HERE = pathlib.Path(__file__).parent
FONTS = (HERE / "fonts").resolve()
OUT = HERE / "out" / "gbp3"
W, H = 1200, 900


def pagina(naam, label, schaal=0.9, anker=1.0):
    img, bg = illu.in_vak(naam, W, H, schaal=schaal, anker=anker)
    return f"""<html><head><meta charset='utf-8'><style>
@font-face{{font-family:'Athiti';src:url('file://{FONTS}/athiti-latin-600-normal.woff2') format('woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{bg}}}
img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}
.label{{position:absolute;left:50%;bottom:48px;transform:translateX(-50%);background:#2c2e7b;
  color:#fef5ff;font-family:'Athiti';font-weight:600;font-size:44px;line-height:1;
  padding:20px 44px 18px;border-radius:999px;white-space:nowrap}}
</style></head><body><img src='file://{img}'><div class='label'>{label}</div></body></html>"""


def uit_posts(datums=None):
    """Alle posts met een `illustratie` uit gbp_posts.json, op datum als bestandsnaam."""
    posts = json.loads((HERE / "gbp_posts.json").read_text(encoding="utf-8"))
    return {p["date"]: (p["illustratie"]["img"], p["illustratie"]["label"],
                        p["illustratie"]["schaal"], p["illustratie"]["anker"])
            for p in posts if p.get("illustratie") and (not datums or p["date"] in datums)}


def render(items):
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for key, (naam, label, *opt) in items.items():
            f = OUT / f"{key}.html"
            f.write_text(pagina(naam, label, *opt), encoding="utf-8")
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.goto(f"file://{f}")
            pg.wait_for_timeout(400)
            pg.screenshot(path=str(OUT / f"{key}.jpg"), type="jpeg", quality=92)
            pg.close()
        b.close()


if __name__ == "__main__":
    render(uit_posts(sys.argv[1:]))
