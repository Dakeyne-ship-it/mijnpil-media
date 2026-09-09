"""Google Business Profile post images: 1200 x 900 landscape.

Same visual language as the Instagram poster concept (flat colour field, XL
Athiti, pink arc motif), retuned for landscape. Google crops posts towards
square in some surfaces, so the type block sits left of centre and the arc
motif is bled off the right edge where a crop can safely eat it.

    python3 gbp.py                 render every entry in gbp_queue.json
    python3 gbp.py 2026-09-14      render one entry by date
"""
import json
import math
import pathlib
import sys

from playwright.sync_api import sync_playwright

from base import page

HERE = pathlib.Path(__file__).parent
QUEUE = json.loads((HERE / "gbp_queue.json").read_text(encoding="utf-8"))
OUT = HERE / "out" / "gbp"
HTML = HERE / "out" / "html"
W, H = 1200, 900

MARK = "<div class='mark'><span class='dot'></span>mijnpil.nu</div>"

# Rotating background fields. The queue names one of these per post so the
# sequence never shows the same colour twice in a row.
FIELDS = {
    "mint": "var(--mint)",
    "peach": "var(--peach)",
    "sky": "var(--sky)",
    "blush": "var(--blush)",
    "lilac": "var(--lilac)",
    "paper": "var(--paper)",
}


def poster(kicker, lines, note, field="mint"):
    """One landscape poster. `lines` is a list of strings; <em> renders pink."""
    css = f"""
    /* Google crops towards square on some surfaces. A centre crop of 1200x900
       keeps x 150 to 1050, so every element that matters sits inside that band
       and only the decorative arcs are allowed to fall outside it. */
    .stage{{background:{FIELDS[field]};color:var(--indigo);
            padding:60px 165px}}
    .arcs{{position:absolute;right:-260px;top:-150px;opacity:.5}}
    .k{{color:var(--pink)}}
    .rule{{width:180px;height:3px;background:var(--pink);margin-top:16px}}
    .q{{font-family:'Athiti';font-size:78px;font-weight:600;line-height:1.08;
        letter-spacing:-.03em;max-width:740px}}
    .q span{{display:block}}
    .q em{{font-style:normal;color:var(--pink);font-weight:700}}
    .kicker{{font-size:17px}}
    .mark{{font-size:20px}}
    .note{{font-size:17px}}
    """
    arcs = ""
    for rs in ((120, 230, 340), (175, 285), (395,)):
        ring = ""
        for r in rs:
            c = 2 * math.pi * r
            ring += (f"<circle cx='280' cy='280' r='{r}' fill='none' stroke='#ea4f79' "
                     f"stroke-width='2.5' stroke-linecap='round' "
                     f"stroke-dasharray='{c * 0.60:.0f} {c * 0.40:.0f}'/>")
        arcs += f"<g>{ring}</g>"
    ls = "".join(f"<span>{t}</span>" for t in lines)
    return page(f"""<div class='stage'>
      <svg class='arcs' width='600' height='600'>{arcs}</svg>
      <div class='head'><div class='k kicker'>{kicker}</div><div class='rule'></div></div>
      <div class='mid'><div class='q'>{ls}</div></div>
      <div class='foot'>{MARK}<div class='note'>{note}</div></div>
    </div>""", css, W, H)


def render(entries):
    OUT.mkdir(parents=True, exist_ok=True)
    HTML.mkdir(parents=True, exist_ok=True)
    written = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for e in entries:
            html = poster(e["kicker"], e["lines"], e["note"], e.get("field", "mint"))
            f = HTML / f"gbp-{e['date']}.html"
            f.write_text(html, encoding="utf-8")
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.goto(f"file://{f}")
            pg.wait_for_timeout(400)
            dest = OUT / f"{e['date']}.jpg"
            pg.screenshot(path=str(dest), type="jpeg", quality=92)
            pg.close()
            written.append(dest)
            print(f"rendered {dest.name}  {e['kicker']}")
        b.close()
    return written


if __name__ == "__main__":
    want = sys.argv[1:]
    entries = [e for e in QUEUE if not want or e["date"] in want]
    if not entries:
        print("NO MATCHING ENTRIES")
        sys.exit(0)
    render(entries)
