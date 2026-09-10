"""Google Business Profile posts: one object, drawn large, readable at 250px.

The knowledge panel and Maps render a post image at roughly 250 pixels wide.
Typography does not survive that; a single high contrast silhouette does. Each
image is therefore one object filling most of the frame on a flat brand field,
with at most a short label.

Everything is hand built SVG in the brand palette. Nothing photographic, and
nothing that makes a prescription medicine the subject of the picture: where a
method has to be referenced, the picture shows the rhythm of using it (a daily
dot, a weekly strip) rather than the medicine itself.

    python3 gbp_object.py              render all
    python3 gbp_object.py pakket cup   render some
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FONTS = (HERE / "fonts").resolve()
OUT = HERE / "out" / "gbp2"
W, H = 1200, 900

INDIGO, PINK, PEACH, MINT, BLUSH, LILAC, SKY, PAPER = (
    "#2c2e7b", "#ea4f79", "#f9d2b8", "#cfeae5",
    "#f9c1b7", "#9e9dce", "#d4eff9", "#fef5ff",
)


def frame(field, inner, label=""):
    """One object centred on a flat field, with an optional short label."""
    lab = f"<div class='label'>{label}</div>" if label else ""
    return f"""<html><head><meta charset='utf-8'><style>
@font-face{{font-family:'Athiti';src:url('file://{FONTS}/athiti-latin-600-normal.woff2') format('woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:{field};display:flex;align-items:center;justify-content:center;
     position:relative}}
svg{{display:block;margin-top:{-34 if label else 0}px}}
.label{{position:absolute;left:0;right:0;bottom:54px;text-align:center;
        font-family:'Athiti',sans-serif;font-size:58px;font-weight:600;
        color:{INDIGO};letter-spacing:-.02em}}
</style></head><body>
<svg width='620' height='620' viewBox='0 0 620 620'>{inner}</svg>{lab}</body></html>"""


# ------------------------------------------------- blok 1: het bezwaar weg

def pakket():
    """A parcel in three quarter view carrying one deliberately blank label."""
    return frame(MINT, f"""
  <path d="M104 236 L310 168 L516 236 L310 306 Z" fill="{PEACH}"
        stroke="{INDIGO}" stroke-width="13" stroke-linejoin="round"/>
  <path d="M104 236 V430 L310 500 V306 Z" fill="{PEACH}" stroke="{INDIGO}"
        stroke-width="13" stroke-linejoin="round"/>
  <path d="M516 236 V430 L310 500 V306 Z" fill="{BLUSH}" stroke="{INDIGO}"
        stroke-width="13" stroke-linejoin="round"/>
  <path d="M310 306 V500" stroke="{INDIGO}" stroke-width="13"/>
  <path d="M207 202 L207 396" stroke="{INDIGO}" stroke-width="11" opacity=".35"/>
  <rect x="352" y="332" width="132" height="94" rx="10" fill="{PAPER}"
        stroke="{INDIGO}" stroke-width="11" transform="rotate(-9 418 379)"/>
""", "geen afzender")


def keurmerk():
    """Shield with a pharmacy cross and a tick."""
    return frame(SKY, f"""
  <path d="M310 84 L522 164 V332 c0 122 -92 174 -212 214
           C190 506 98 454 98 332 V164 Z" fill="{INDIGO}"/>
  <rect x="268" y="186" width="80" height="204" rx="12" fill="{PAPER}"/>
  <rect x="206" y="248" width="204" height="80" rx="12" fill="{PAPER}"/>
  <circle cx="430" cy="410" r="82" fill="{PINK}"/>
  <path d="M396 410 l26 28 l48 -58" fill="none" stroke="{PAPER}"
        stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>
""", "een echte apotheek")


def zelfbetalen():
    """Bank card and receipt."""
    return frame(PEACH, f"""
  <rect x="80" y="222" width="382" height="248" rx="26" fill="{INDIGO}"/>
  <rect x="80" y="284" width="382" height="46" fill="{PAPER}"/>
  <rect x="122" y="378" width="148" height="30" rx="15" fill="{PAPER}"
        opacity=".6"/>
  <g transform="rotate(9 470 250)">
    <path d="M386 104 h190 v252 l-31 -22 l-32 22 l-32 -22 l-32 22 l-32 -22
             l-31 22 Z" fill="{PAPER}" stroke="{INDIGO}" stroke-width="11"
          stroke-linejoin="round"/>
    <rect x="416" y="154" width="130" height="17" rx="9" fill="{INDIGO}"/>
    <rect x="416" y="198" width="94" height="17" rx="9" fill="{INDIGO}"
          opacity=".45"/>
    <rect x="416" y="242" width="130" height="17" rx="9" fill="{PINK}"/>
  </g>
""", "jij betaalt zelf")


def controle():
    """Magnifier over a form."""
    return frame(LILAC, f"""
  <rect x="104" y="88" width="330" height="424" rx="22" fill="{PAPER}"
        stroke="{INDIGO}" stroke-width="13"/>
  <rect x="156" y="152" width="226" height="21" rx="11" fill="{INDIGO}"
        opacity=".5"/>
  <rect x="156" y="208" width="160" height="21" rx="11" fill="{INDIGO}"
        opacity=".5"/>
  <rect x="156" y="264" width="204" height="21" rx="11" fill="{INDIGO}"
        opacity=".5"/>
  <circle cx="386" cy="380" r="126" fill="{SKY}" fill-opacity=".7"
          stroke="{INDIGO}" stroke-width="17"/>
  <path d="M478 472 L556 550" stroke="{INDIGO}" stroke-width="32"
        stroke-linecap="round"/>
  <path d="M344 380 l30 32 l58 -70" fill="none" stroke="{PINK}"
        stroke-width="21" stroke-linecap="round" stroke-linejoin="round"/>
""", "altijd gecontroleerd")


# --------------------------------------------- blok 2: de methode is er

def dagelijks():
    """A clean circular arrow: continuous use, no stop week. No stray strokes,
    and nothing that resembles a strip of tablets."""
    return frame(MINT, f"""
  <path d="M310 122 a178 178 0 1 1 -126 52" fill="none" stroke="{INDIGO}"
        stroke-width="58" stroke-linecap="butt"/>
  <path d="M296 40 L400 122 L296 204 Z" fill="{INDIGO}"/>
  <circle cx="310" cy="300" r="64" fill="{PINK}"/>
""", "geen stopweek")


def ring():
    """Abstract torus."""
    return frame(BLUSH, f"""
  <circle cx="310" cy="300" r="184" fill="none" stroke="{INDIGO}"
          stroke-width="78"/>
  <circle cx="310" cy="300" r="184" fill="none" stroke="{PAPER}"
          stroke-width="16" stroke-dasharray="66 1100"
          transform="rotate(-54 310 300)" stroke-linecap="round"/>
""", "drie weken in")


def week():
    """Four weeks as four plain bars: three on, one off. No dots, because a
    grid of dots in rounded bars reads as a strip of tablets."""
    rows = ""
    for r in range(4):
        y = 178 + r * 96
        on = r < 3
        rows += (f"<rect x='68' y='{y}' width='484' height='68' rx='34' "
                 f"fill='{INDIGO if on else PAPER}' stroke='{INDIGO}' "
                 f"stroke-width='13'/>")
        if on:
            rows += (f"<path d='M118 {y + 34} l22 24 l40 -50' fill='none' "
                     f"stroke='{PAPER}' stroke-width='15' "
                     f"stroke-linecap='round' stroke-linejoin='round'/>")
    return frame(SKY, rows, "3 weken op, 1 af")


def voorraad():
    """Boxes with a tick and a cross: see what is available before you order.
    Peach boxes need a field they can sit on, so this one is mint."""
    out = ""
    for i, ok in enumerate((True, True, False)):
        x = 66 + i * 166
        out += (f"<rect x='{x}' y='214' width='140' height='158' rx='14' "
                f"fill='{PEACH if ok else PAPER}' stroke='{INDIGO}' "
                f"stroke-width='13'/>"
                f"<path d='M{x + 70} 214 V372' stroke='{INDIGO}' "
                f"stroke-width='13' opacity='{1 if ok else .28}'/>")
        cx, cy = x + 70, 428
        if ok:
            out += (f"<circle cx='{cx}' cy='{cy}' r='46' fill='{INDIGO}'/>"
                    f"<path d='M{cx - 20} {cy} l15 16 l27 -33' fill='none' "
                    f"stroke='{PAPER}' stroke-width='13' stroke-linecap='round' "
                    f"stroke-linejoin='round'/>")
        else:
            out += (f"<circle cx='{cx}' cy='{cy}' r='46' fill='{PINK}'/>"
                    f"<path d='M{cx - 18} {cy - 18} l36 36 M{cx + 18} {cy - 18} "
                    f"l-36 36' stroke='{PAPER}' stroke-width='13' "
                    f"stroke-linecap='round'/>")
    return frame(MINT, out, "zie het meteen")


def maanden():
    """One box is three months, so the stacks are 1, 2 and 4 boxes.

    Each box carries a lid seam near the top and a small label. An earlier
    version put a seam down the middle, which split every box into two squares
    and made the stacks read as 2, 4 and 8.
    """
    out = ""
    for i, n in enumerate((1, 2, 4)):
        x = 96 + i * 150
        for k in range(n):
            y = 408 - k * 76
            out += (f"<rect x='{x}' y='{y}' width='128' height='68' rx='12' "
                    f"fill='{PEACH}' stroke='{INDIGO}' stroke-width='12'/>"
                    f"<path d='M{x} {y + 22} H{x + 128}' stroke='{INDIGO}' "
                    f"stroke-width='9' opacity='.5'/>"
                    f"<rect x='{x + 88}' y='{y + 36}' width='26' height='18' "
                    f"rx='5' fill='{PINK}'/>")
    return frame(LILAC, out, "3, 6 of 12 maanden")


# ------------------------------------------------------ blok 3: de service

def herhaal():
    """Month grid with one day circled."""
    cells = ""
    for r in range(4):
        for c in range(6):
            cells += (f"<circle cx='{118 + c * 73}' cy='{262 + r * 66}' r='14' "
                      f"fill='{INDIGO}' opacity='.3'/>")
    return frame(SKY, f"""
  <rect x="58" y="142" width="504" height="396" rx="30" fill="{PAPER}"
        stroke="{INDIGO}" stroke-width="13"/>
  <path d="M58 172 a30 30 0 0 1 30 -30 h444 a30 30 0 0 1 30 30 v56 H58 Z"
        fill="{INDIGO}"/>
  <rect x="158" y="98" width="23" height="82" rx="12" fill="{INDIGO}"/>
  <rect x="440" y="98" width="23" height="82" rx="12" fill="{INDIGO}"/>
  {cells}
  <circle cx="410" cy="394" r="48" fill="{PINK}"/>
  <circle cx="410" cy="394" r="15" fill="{PAPER}"/>
""", "jij kiest wanneer")


def gratis():
    """Package with a struck through price tag."""
    return frame(MINT, f"""
  <rect x="76" y="196" width="366" height="286" rx="22" fill="{PEACH}"
        stroke="{INDIGO}" stroke-width="13"/>
  <path d="M259 196 V482" stroke="{INDIGO}" stroke-width="13"/>
  <g transform="rotate(-13 452 232)">
    <path d="M352 144 h194 a20 20 0 0 1 20 20 v100 a20 20 0 0 1 -20 20 h-194
             l-58 -70 Z" fill="{PAPER}" stroke="{INDIGO}" stroke-width="12"
          stroke-linejoin="round"/>
    <circle cx="338" cy="214" r="16" fill="{INDIGO}"/>
    <rect x="382" y="196" width="142" height="32" rx="16" fill="{INDIGO}"
          opacity=".3"/>
    <path d="M366 214 H548" stroke="{PINK}" stroke-width="16"
          stroke-linecap="round"/>
  </g>
""", "altijd gratis")


def klok():
    """Clock plus an open sign."""
    return frame(PEACH, f"""
  <circle cx="286" cy="284" r="194" fill="{PAPER}" stroke="{INDIGO}"
          stroke-width="17"/>
  <circle cx="286" cy="284" r="17" fill="{INDIGO}"/>
  <path d="M286 284 V162" stroke="{INDIGO}" stroke-width="21"
        stroke-linecap="round"/>
  <path d="M286 284 L372 334" stroke="{PINK}" stroke-width="21"
        stroke-linecap="round"/>
  <g transform="rotate(-8 456 468)">
    <rect x="332" y="396" width="252" height="126" rx="20" fill="{INDIGO}"/>
    <rect x="370" y="436" width="176" height="19" rx="10" fill="{PAPER}"/>
    <rect x="370" y="474" width="114" height="19" rx="10" fill="{PINK}"/>
  </g>
""", "ook 's avonds")


# ------------------------------------------- blok 4: aangrenzend assortiment

def cup():
    """Menstrual cup, drawn to shape."""
    return frame(BLUSH, f"""
  <path d="M176 186 h268 l-30 176 c-10 60 -50 104 -104 104
           c-54 0 -94 -44 -104 -104 Z"
        fill="{PAPER}" stroke="{INDIGO}" stroke-width="15"
        stroke-linejoin="round"/>
  <ellipse cx="310" cy="186" rx="134" ry="28" fill="{PAPER}"
           stroke="{INDIGO}" stroke-width="15"/>
  <path d="M310 466 v58" stroke="{INDIGO}" stroke-width="21"
        stroke-linecap="round"/>
  <circle cx="310" cy="538" r="17" fill="{PINK}"/>
""")


def test():
    """A test stick: long and narrow, with a cap and a result window."""
    return frame(PAPER, f"""
  <g transform="rotate(-20 310 300)">
    <rect x="252" y="52" width="116" height="496" rx="54" fill="{SKY}"
          stroke="{INDIGO}" stroke-width="14"/>
    <path d="M252 106 a54 54 0 0 1 54 -54 h8 a54 54 0 0 1 54 54 v96 H252 Z"
          fill="{INDIGO}"/>
    <rect x="278" y="268" width="64" height="112" rx="12" fill="{PAPER}"
          stroke="{INDIGO}" stroke-width="12"/>
    <circle cx="310" cy="324" r="19" fill="{PINK}"/>
    <rect x="286" y="440" width="48" height="14" rx="7" fill="{INDIGO}"
          opacity=".35"/>
  </g>
""")


OBJECTS = {
    "pakket": pakket, "keurmerk": keurmerk, "zelfbetalen": zelfbetalen,
    "controle": controle, "dagelijks": dagelijks, "ring": ring, "week": week,
    "voorraad": voorraad, "maanden": maanden, "herhaal": herhaal,
    "gratis": gratis, "klok": klok, "cup": cup, "test": test,
}


def render(names):
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n in names:
            f = OUT / f"{n}.html"
            f.write_text(OBJECTS[n](), encoding="utf-8")
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.goto(f"file://{f}")
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / f"{n}.jpg"), type="jpeg", quality=92)
            pg.close()
            print("rendered", n)
        b.close()


if __name__ == "__main__":
    render(sys.argv[1:] or list(OBJECTS))
