import math, pathlib
from base import page

MARK = "<div class='mark'><span class='dot'></span>mijnpil.nu</div>"

# Seconds a scene holds STILL after its last element has finished animating in.
# Every animated concept sizes itself as (settle time + REST), so the reader
# always gets this long with the finished frame in front of them.
# Set by Alexander, 9 sep 2026: 3.0 dragged, 1.5 reads as brisk but legible.
REST = 1.5


# =========================================================== STILLS (4:5 feed)

# Style A as a static feed post: editorial poster, one flat field, big Athiti.
def de_vraag_img(kicker, lines, note="het antwoord staat in de caption",
                 field="var(--mint)", w=1080, h=1350):
    css = f"""
    .stage{{background:{field};color:var(--indigo)}}
    .arcs{{position:absolute;right:-215px;top:-170px;opacity:.55}}
    .k{{color:var(--pink)}}
    .rule{{width:210px;height:3px;background:var(--pink);margin-top:20px}}
    .q{{font-family:'Athiti';font-size:104px;font-weight:600;line-height:1.06;
        letter-spacing:-.03em;max-width:900px}}
    .q span{{display:block}}
    .q em{{font-style:normal;color:var(--pink);font-weight:700}}
    """
    arcs = ""
    for rs in ((130, 250, 370), (190, 310), (430,)):
        ring = ""
        for r in rs:
            c = 2 * math.pi * r
            ring += (f"<circle cx='300' cy='300' r='{r}' fill='none' stroke='#ea4f79' "
                     f"stroke-width='2.5' stroke-linecap='round' "
                     f"stroke-dasharray='{c*0.60:.0f} {c*0.40:.0f}'/>")
        arcs += f"<g>{ring}</g>"
    ls = "".join(f"<span>{t}</span>" for t in lines)
    return page(f"""<div class='stage'>
      <svg class='arcs' width='640' height='640'>{arcs}</svg>
      <div class='head'><div class='k kicker'>{kicker}</div><div class='rule'></div></div>
      <div class='mid'><div class='q'>{ls}</div></div>
      <div class='foot'>{MARK}<div class='note'>{note}</div></div>
    </div>""", css, w, h)


# Closing slide for the Anatomie carousel: same plate language, one takeaway.
def anatomie_slot2(takeaway, sub, w=1080, h=1350):
    css = """
    .stage{background:var(--paper);color:var(--indigo);
      background-image:linear-gradient(#2c2e7b0d 1px,transparent 1px),
                       linear-gradient(90deg,#2c2e7b0d 1px,transparent 1px);
      background-size:54px 54px}
    .k{color:var(--pink)}
    .t{font-family:'Athiti';font-size:88px;font-weight:600;line-height:1.06;
       letter-spacing:-.025em}
    .t em{font-style:normal;color:var(--pink);font-weight:700}
    .s{margin-top:40px;font-size:29px;font-weight:400;line-height:1.5;
       max-width:820px;border-left:3px solid var(--pink);padding-left:24px}
    """
    return page(f"""<div class='stage'>
      <div class='head'><div class='k kicker'>Onthoud dit</div></div>
      <div class='mid'><div class='t'>{takeaway}</div><div class='s'>{sub}</div></div>
      <div class='foot'>{MARK}<div class='note'>2 / 2</div></div>
    </div>""", css, w, h)


# Style B, "Hard-cut two-tone". Carousel slide 1 of 2.
def mythe(lines, n="1 / 2", w=1080, h=1350):
    """`lines` is a list of strings; each gets its own strike-through bar."""
    css = """
    .stage{background:var(--blush);color:var(--indigo)}
    .tag{font-family:'Athiti';font-size:170px;font-weight:700;
         letter-spacing:-.045em;line-height:.88}
    .s{font-family:'Athiti';font-size:86px;font-weight:600;line-height:1.16;
       letter-spacing:-.025em}
    .s i{position:relative;font-style:normal;display:inline-block}
    .s i::after{content:'';position:absolute;left:-10px;right:-10px;top:54%;
      height:11px;border-radius:6px;background:var(--pink)}
    .n{font-size:18px;font-weight:500;opacity:.42}
    """
    body = "".join(f"<div><i>{t}</i></div>" for t in lines)
    return page(f"""<div class='stage'>
      <div class='head'><div class='tag'>MYTHE</div></div>
      <div class='mid'><div class='s'>{body}</div></div>
      <div class='foot'>{MARK}<div class='n'>{n}</div></div>
    </div>""", css, w, h)


def feit(statement, source, n="2 / 2", w=1080, h=1350):
    css = """
    .stage{background:var(--indigo);color:var(--paper)}
    .tag{font-family:'Athiti';font-size:170px;font-weight:700;
         letter-spacing:-.045em;line-height:.88}
    .tag span{color:var(--pink)}
    .s{font-family:'Athiti';font-size:74px;font-weight:600;line-height:1.15;
       letter-spacing:-.02em}
    .s b{font-weight:700;color:var(--peach)}
    .src{margin-top:50px;font-size:22px;font-weight:400;line-height:1.55;
      color:var(--lilac);border-left:3px solid var(--pink);padding-left:22px;max-width:830px}
    .n{font-size:18px;font-weight:500;opacity:.42}
    """
    return page(f"""<div class='stage'>
      <div class='head'><div class='tag'>FEIT<span>.</span></div></div>
      <div class='mid'><div class='s'>{statement}</div><div class='src'>{source}</div></div>
      <div class='foot'>{MARK}<div class='n'>{n}</div></div>
    </div>""", css, w, h)


# Style C, "Studio medical plate".
# One shared plate: hairline grid, precise line work in indigo, numbered pink
# leader callouts. Each variant supplies its own title and drawing.

def _callout(n, leader, num_xy, lbl_x, label, subs, side="above"):
    """A numbered pink leader line with a heading and sub-lines.

    The text block is positioned from the disc outwards, so it never collides
    with the disc however many sub-lines it carries. `side` says whether the
    text sits above or below the numbered disc.
    """
    nx, ny = num_xy
    if side == "above":
        last_sub = ny - 19 - 16
        first_sub = last_sub - (len(subs) - 1) * 26
        ly = first_sub - 34
    else:
        ly = ny + 19 + 42
        first_sub = ly + 34
    out = (f"<path d='{leader}' fill='none' stroke='#ea4f79' stroke-width='2'/>"
           f"<circle cx='{nx}' cy='{ny}' r='19' fill='#ea4f79'/>"
           f"<text class='num' x='{nx}' y='{ny+8}' text-anchor='middle'>{n}</text>"
           f"<text class='lbl' x='{lbl_x}' y='{ly}'>{label}</text>")
    for i, s in enumerate(subs):
        out += f"<text class='sub' x='{lbl_x}' y='{first_sub + i*26}'>{s}</text>"
    return out


def _plate_strip28():
    pills = ""
    for i in range(28):
        col, row = i % 7, i // 7
        cx, cy = 66 + col * 84, 232 + row * 84
        if i < 21:
            pills += f"<circle cx='{cx}' cy='{cy}' r='29' fill='#2c2e7b'/>"
        else:
            pills += (f"<circle cx='{cx}' cy='{cy}' r='29' fill='none' stroke='#ea4f79' "
                      f"stroke-width='2.5' stroke-dasharray='7 6'/>")
    c = (_callout(1, "M 596 232 L 700 232 L 700 150", (700, 131), 596,
                  "21 hormoondagen", ["elke dag rond hetzelfde tijdstip"], "above")
         + _callout(2, "M 596 484 L 700 484 L 700 566", (700, 585), 596,
                    "7 stopdagen", ["de bloeding hier is een",
                                    "onttrekkingsbloeding"], "below"))
    return "Een strip<br>van 28 dagen", 928, 760, pills + c


def _plate_spiraal():
    # drawn to scale: 110 px = 1 cm, so the body is 3,2 cm tall
    CX, TOP, BOT = 380, 210, 562
    arm_l, arm_r = CX - 176, CX + 176
    d = (
        # arms: lift very slightly at the tips so it reads as a T, not a droop
        f"<path d='M {arm_l} {TOP+8} Q {CX-88} {TOP+30} {CX} {TOP+22} "
        f"Q {CX+88} {TOP+30} {arm_r} {TOP+8}' fill='none' stroke='#2c2e7b' "
        f"stroke-width='17' stroke-linecap='round'/>"
        # stem
        f"<path d='M {CX} {TOP+18} L {CX} {BOT}' stroke='#2c2e7b' stroke-width='19' "
        f"stroke-linecap='round'/>"
        # threads
        f"<path d='M {CX-5} {BOT} Q {CX-26} {BOT+48} {CX-16} {BOT+88}' fill='none' "
        f"stroke='#2c2e7b' stroke-width='4' stroke-linecap='round' opacity='.75'/>"
        f"<path d='M {CX+5} {BOT} Q {CX+28} {BOT+46} {CX+14} {BOT+90}' fill='none' "
        f"stroke='#2c2e7b' stroke-width='4' stroke-linecap='round' opacity='.75'/>"
    )
    # dimension line, clear to the left of the arms
    DX = 150
    d += (f"<path d='M {DX} {TOP+18} L {DX} {BOT}' stroke='#ea4f79' stroke-width='2'/>"
          f"<path d='M {DX-13} {TOP+18} L {DX+13} {TOP+18}' stroke='#ea4f79' stroke-width='2'/>"
          f"<path d='M {DX-13} {BOT} L {DX+13} {BOT}' stroke='#ea4f79' stroke-width='2'/>"
          f"<text class='lbl' x='{DX-24}' y='{(TOP+BOT)//2+10}' text-anchor='end' "
          f"fill='#ea4f79'>3,2 cm</text>")
    c = (_callout(1, f"M {arm_r} {TOP+10} L 792 {TOP+10} L 792 231", (792, 212), 560,
                  "De armpjes vouwen",
                  ["samen tijdens het plaatsen,", "en klappen daarna open"], "above")
         + _callout(2, "M 400 500 L 792 500 L 792 541", (792, 560), 500,
                    "Hormoon of koper",
                    ["hormoon maakt je menstruatie lichter,",
                     "koper juist wat zwaarder"], "below"))
    return "Een spiraaltje,<br>op ware grootte", 928, 760, d + c


def _plate_pleister():
    d = ""
    for i in range(4):
        x = 40 + i * 196
        y = 250
        if i < 3:
            d += (f"<rect x='{x}' y='{y}' width='150' height='150' rx='34' fill='#2c2e7b'/>"
                  f"<rect x='{x+26}' y='{y+26}' width='98' height='98' rx='20' fill='none' "
                  f"stroke='#fef5ff' stroke-width='2' opacity='.45'/>")
        else:
            d += (f"<rect x='{x}' y='{y}' width='150' height='150' rx='34' fill='none' "
                  f"stroke='#ea4f79' stroke-width='2.5' stroke-dasharray='8 7'/>")
        d += (f"<text class='sub' x='{x+75}' y='{y+196}' text-anchor='middle'>"
              f"week {i+1}</text>")
    # leaders route around the squares rather than across them
    c = (_callout(1, "M 313 250 L 313 196 L 792 196 L 792 231", (792, 212), 470,
                  "Elke week een nieuwe",
                  ["steeds op een andere plek:", "bil, buik, bovenarm of rug"], "above")
         + _callout(2, "M 778 325 L 850 325 L 850 481", (850, 500), 470,
                    "Week 4: geen pleister",
                    ["in die week komt de bloeding,",
                     "net als in de stopweek van de pil"], "below"))
    return "De pleister,<br>week voor week", 928, 760, d + c


ANATOMIE_PLATES = {
    "strip28": _plate_strip28,
    "spiraal": _plate_spiraal,
    "pleister": _plate_pleister,
}


def anatomie(variant="strip28", w=1080, h=1350):
    title, sw, sh, inner = ANATOMIE_PLATES[variant]()
    css = """
    .stage{background:var(--paper);color:var(--indigo);
      background-image:linear-gradient(#2c2e7b0d 1px,transparent 1px),
                       linear-gradient(90deg,#2c2e7b0d 1px,transparent 1px);
      background-size:54px 54px}
    .k{color:var(--pink)}
    .t{font-family:'Athiti';font-size:92px;font-weight:600;line-height:1.02;
       letter-spacing:-.025em;margin-top:6px}
    .plate{flex:1 1 auto;position:relative}
    svg{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)}
    .lbl{font-family:'Athiti';font-size:29px;font-weight:600;fill:#2c2e7b}
    .sub{font-family:'RobotoSlab';font-size:19px;font-weight:400;fill:#2c2e7b;opacity:.62}
    .num{font-family:'Athiti';font-size:23px;font-weight:700;fill:#fef5ff}
    """
    return page(f"""<div class='stage'>
      <div class='head'><div class='k kicker'>Anatomie van</div>
        <div class='t'>{title}</div></div>
      <div class='mid plate'><svg width='{sw}' height='{sh}'>{inner}</svg></div>
      <div class='foot'>{MARK}<div class='note'>bewaar 'm voor later</div></div>
    </div>""", css, w, h)


# ================================================== ANIMATED (9:16 reel/story)
# Each returns (html, duration_seconds).

# Style A, "Editorial poster" in motion: lines rise in, arc field drifts.
def de_vraag_v(kicker, lines, note="het antwoord staat in de caption",
               field="var(--mint)", w=1080, h=1920):
    css = f"""
    .stage{{background:{field};color:var(--indigo);padding:200px 90px 330px}}
    .arcs{{position:absolute;right:-250px;top:-190px;opacity:.55;
      animation:fade 1.1s ease .05s}}
    .arcs g{{transform-origin:320px 320px}}
    .arcs g:nth-of-type(1){{animation:spin 60s linear infinite}}
    .arcs g:nth-of-type(2){{animation:spin 44s linear infinite reverse}}
    .arcs g:nth-of-type(3){{animation:spin 78s linear infinite}}
    .k{{color:var(--pink)}}
    .rule{{width:220px;height:4px;background:var(--pink);margin-top:20px;
      transform-origin:left;animation:wipe .6s .18s}}
    .q{{font-family:'Athiti';font-size:112px;font-weight:600;line-height:1.04;
        letter-spacing:-.03em}}
    .q span{{display:block}}
    .q em{{font-style:normal;color:var(--pink);font-weight:700}}
    .note{{animation:fade .7s 2.5s}}
    .mark{{animation:fade .7s 2.5s}}
    .k{{animation:rise .7s .05s}}
    """
    ls = "".join(
        f"<span class='anim' style='animation:rise .78s {0.55 + i*0.34:.2f}s'>{t}</span>"
        for i, t in enumerate(lines))
    arcs = ""
    for rs in ((140, 270, 400), (205, 335), (465,)):
        ring = ""
        for r in rs:
            c = 2 * math.pi * r
            ring += (f"<circle cx='320' cy='320' r='{r}' fill='none' "
                     f"stroke='#ea4f79' stroke-width='2.5' stroke-linecap='round' "
                     f"stroke-dasharray='{c*0.60:.0f} {c*0.40:.0f}'/>")
        arcs += f"<g class='anim'>{ring}</g>"
    html = page(f"""<div class='stage'>
      <svg class='arcs anim' width='680' height='680'>{arcs}</svg>
      <div class='head'><div class='k kicker anim'>{kicker}</div>
        <div class='rule anim'></div></div>
      <div class='mid'><div class='q'>{ls}</div></div>
      <div class='foot'>{MARK.replace("mark'","mark anim'")}
        <div class='note anim'>{note}</div></div>
    </div>""", css, w, h)
    settle = max(0.55 + (len(lines) - 1) * 0.34 + 0.78, 2.5 + 0.7)
    return html, round(settle + REST, 2)


# Style D, "Soft data illustration" in motion.
def cyclus_v(variant="hormonen", w=1080, h=1920):
    if variant == "vruchtbaar":
        return _cyclus_vruchtbaar(w, h)
    W, H = 900, 720
    L, R, TOP, BOT = 64, W - 64, 60, 520
    x = lambda d: L + (R - L) * d / 28
    pts = []
    for i in range(0, 141):
        d = i / 5
        v = math.exp(-((d - 13.5) ** 2) / 15) + 0.6 * math.exp(-((d - 21) ** 2) / 34)
        pts.append((x(d), BOT - v * (BOT - TOP) * 0.95))
    nat = "M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts)
    area = nat + f" L {R} {BOT} L {L} {BOT} Z"
    flat = f"M {L} {BOT-66} L {x(21)} {BOT-66} L {x(21)} {BOT-16} L {R} {BOT-16}"
    natlen = sum(math.dist(pts[i], pts[i+1]) for i in range(len(pts)-1))
    flatlen = (x(21) - L) + 50 + (R - x(21))
    ticks = "".join(
        f"<line x1='{x(d)}' y1='{BOT}' x2='{x(d)}' y2='{BOT+13}' stroke='#2c2e7b' "
        f"stroke-width='2' opacity='.3'/>"
        f"<text class='ax' x='{x(d)}' y='{BOT+50}' text-anchor='middle'>dag {d}</text>"
        for d in (0, 7, 14, 21, 28))
    css = f"""
    .stage{{background:linear-gradient(168deg,var(--paper) 0%,#ece3f6 100%);
      color:var(--indigo);padding:200px 90px 330px}}
    .k{{color:var(--pink);animation:rise .7s .05s}}
    .t{{font-family:'Athiti';font-size:98px;font-weight:600;line-height:1.02;
       letter-spacing:-.025em;margin-top:8px;animation:rise .8s .3s}}
    .chart{{flex:1 1 auto;position:relative}}
    svg{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)}}
    .ax{{font-family:'RobotoSlab';font-size:21px;font-weight:400;fill:#2c2e7b;opacity:.45}}
    .lg{{font-family:'RobotoSlab';font-size:26px;font-weight:500;fill:#2c2e7b}}
    #axis{{--len:{R-L};stroke-dasharray:{R-L};animation:draw .6s .75s}}
    #nat{{--len:{natlen:.0f};stroke-dasharray:{natlen:.0f};animation:draw 2.0s .95s}}
    #area{{animation:fade 1.0s 2.05s}}
    #flat{{--len:{flatlen:.0f};stroke-dasharray:{flatlen:.0f};animation:draw 1.1s 2.5s}}
    #tk{{animation:fade .7s 1.3s}}
    #lg1{{animation:rise .7s 3.5s}} #lg2{{animation:rise .7s 3.8s}}
    .mark{{animation:fade .7s 4.1s}} .note{{animation:fade .7s 4.1s}}
    """
    html = page(f"""<div class='stage'>
      <div class='head'><div class='k kicker anim'>De cyclus, in beeld</div>
        <div class='t'>Wat de pil met<br>je hormonen doet</div></div>
      <div class='mid chart'><svg width='{W}' height='{H}'>
        <path id='area' class='anim' d="{area}" fill='#f9d2b8' opacity='.75'/>
        <path id='nat' class='anim' d="{nat}" fill='none' stroke='#ea4f79'
              stroke-width='6' stroke-linecap='round'/>
        <path id='flat' class='anim' d="{flat}" fill='none' stroke='#2c2e7b'
              stroke-width='6' stroke-linecap='round'/>
        <line id='axis' class='anim' x1='{L}' y1='{BOT}' x2='{R}' y2='{BOT}'
              stroke='#2c2e7b' stroke-width='2.5' opacity='.45'/>
        <g id='tk' class='anim'>{ticks}</g>
        <g id='lg1' class='anim'><circle cx='14' cy='612' r='9' fill='#ea4f79'/>
          <text class='lg' x='42' y='621'>zonder pil, hormonen pieken</text></g>
        <g id='lg2' class='anim'><circle cx='14' cy='666' r='9' fill='#2c2e7b'/>
          <text class='lg' x='42' y='675'>met de pil, vlak en geen eisprong</text></g>
      </svg></div>
      <div class='foot'>{MARK.replace("mark'","mark anim'")}
        <div class='note anim'>bewaar 'm voor later</div></div>
    </div>""", css, w, h)
    return html, round(4.8 + REST, 2)


# The fertile window: a six-day band, not a single day.
def _cyclus_vruchtbaar(w=1080, h=1920):
    W, H = 900, 720
    L, R, BOT = 64, W - 64, 470
    x = lambda d: L + (R - L) * d / 28
    band_l, band_r = x(9), x(14)
    OV = x(14)
    ticks = "".join(
        f"<line x1='{x(d)}' y1='{BOT}' x2='{x(d)}' y2='{BOT+13}' stroke='#2c2e7b' "
        f"stroke-width='2' opacity='.3'/>"
        f"<text class='ax' x='{x(d)}' y='{BOT+50}' text-anchor='middle'>dag {d}</text>"
        for d in (0, 7, 14, 21, 28))
    css = f"""
    .stage{{background:linear-gradient(168deg,var(--paper) 0%,#ece3f6 100%);
      color:var(--indigo);padding:200px 90px 330px}}
    .k{{color:var(--pink);animation:rise .7s .05s}}
    .t{{font-family:'Athiti';font-size:98px;font-weight:600;line-height:1.02;
       letter-spacing:-.025em;margin-top:8px;animation:rise .8s .3s}}
    .chart{{flex:1 1 auto;position:relative}}
    svg{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)}}
    .ax{{font-family:'RobotoSlab';font-size:21px;font-weight:400;fill:#2c2e7b;opacity:.45}}
    .lg{{font-family:'RobotoSlab';font-size:25px;font-weight:500;fill:#2c2e7b}}
    .big{{font-family:'Athiti';font-size:42px;font-weight:700;fill:#2c2e7b}}
    #axis{{--len:{R-L};stroke-dasharray:{R-L};animation:draw .6s .7s}}
    #tk{{animation:fade .7s 1.1s}}
    #band{{transform-origin:{band_l}px 0;animation:wipe .9s 1.5s}}
    #ovl{{animation:pop .6s 2.5s}}
    #sperm{{animation:fade .7s 3.0s}} #egg{{animation:fade .7s 3.4s}}
    .mark{{animation:fade .7s 3.9s}} .note{{animation:fade .7s 3.9s}}
    """
    html = page(f"""<div class='stage'>
      <div class='head'><div class='k kicker anim'>De cyclus, in beeld</div>
        <div class='t'>Wanneer ben je<br>vruchtbaar?</div></div>
      <div class='mid chart'><svg width='{W}' height='{H}'>
        <g id='band' class='anim'>
          <rect x='{band_l}' y='250' width='{band_r-band_l}' height='{BOT-250}'
                fill='#f9d2b8' opacity='.85' rx='6'/>
          <text class='big' x='{(band_l+band_r)/2}' y='226' text-anchor='middle'>6 dagen</text>
        </g>
        <line id='axis' class='anim' x1='{L}' y1='{BOT}' x2='{R}' y2='{BOT}'
              stroke='#2c2e7b' stroke-width='2.5' opacity='.45'/>
        <g id='tk' class='anim'>{ticks}</g>
        <g id='ovl' class='anim'>
          <line x1='{OV}' y1='250' x2='{OV}' y2='{BOT}' stroke='#ea4f79' stroke-width='5'/>
          <circle cx='{OV}' cy='250' r='13' fill='#ea4f79'/>
          <text class='lg' x='{OV+22}' y='244' fill='#ea4f79'>eisprong</text>
        </g>
        <g id='sperm' class='anim'><circle cx='14' cy='574' r='9' fill='#f9d2b8'/>
          <text class='lg' x='42' y='583'>zaadcellen overleven tot 5 dagen</text></g>
        <g id='egg' class='anim'><circle cx='14' cy='626' r='9' fill='#ea4f79'/>
          <text class='lg' x='42' y='635'>een eicel leeft ongeveer 24 uur</text></g>
      </svg></div>
      <div class='foot'>{MARK.replace("mark'","mark anim'")}
        <div class='note anim'>bewaar 'm voor later</div></div>
    </div>""", css, w, h)
    return html, round(4.6 + REST, 2)


# Style E, "Soft UI" in motion: bubble, typing dots, answer.
def uit_de_dm_v(vraag, antwoord, w=1080, h=1920):
    css = """
    .stage{background:var(--sky);color:var(--indigo);padding:200px 84px 330px}
    .k{opacity:.5;animation:fade .6s .05s}
    .hd{display:flex;align-items:center;gap:20px;margin-top:26px;animation:rise .7s .2s}
    .badge{width:78px;height:78px;border-radius:24px;background:var(--indigo);
      display:grid;place-items:center;flex:0 0 auto;
      box-shadow:0 10px 26px rgba(44,46,123,.24)}
    .who{font-family:'Athiti';font-size:34px;font-weight:600;line-height:1.2}
    .who span{display:block;font-family:'RobotoSlab';font-size:19px;
      font-weight:400;opacity:.5;margin-top:2px}
    .bub{max-width:84%;padding:40px 44px;font-size:38px;line-height:1.42;
         border-radius:38px}
    .in{background:#fff;border-bottom-left-radius:10px;font-weight:400;
        box-shadow:0 18px 46px rgba(44,46,123,.15);animation:pop .6s .75s}
    @keyframes typing{0%,28%{opacity:0}34%,52%{opacity:1}58%,100%{opacity:0}}
    @keyframes bounce{0%,60%,100%{transform:none}30%{transform:translateY(-11px)}}
    .typing{display:flex;gap:14px;align-items:center;background:#fff;width:132px;
      padding:26px 30px;border-radius:34px;border-bottom-left-radius:10px;
      margin-top:30px;box-shadow:0 12px 34px rgba(44,46,123,.13);
      animation:typing 5s linear}
    .typing i{width:16px;height:16px;border-radius:50%;background:var(--lilac);
      animation:bounce 1s linear infinite}
    .typing i:nth-child(2){animation-delay:.16s}
    .typing i:nth-child(3){animation-delay:.32s}
    .out{background:var(--indigo);color:var(--paper);margin-left:auto;margin-top:30px;
         border-bottom-right-radius:10px;font-weight:400;
         box-shadow:0 18px 46px rgba(44,46,123,.24);animation:pop .6s 2.95s}
    .out b{color:var(--peach);font-weight:700}
    .mark{animation:fade .7s 4.0s} .note{animation:fade .7s 4.0s}
    """
    bubble = ("<svg width='40' height='40' viewBox='0 0 24 24' fill='none' "
              "stroke='#fef5ff' stroke-width='1.8' stroke-linecap='round' "
              "stroke-linejoin='round'>"
              "<path d='M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.5-.6L3 21l1.8-4.6"
              "A8.4 8.4 0 0 1 12 3.1a8.4 8.4 0 0 1 9 8.4Z'/>"
              "<path d='M8.5 11.5h.01M12 11.5h.01M15.5 11.5h.01'/></svg>")
    html = page(f"""<div class='stage'>
      <div class='head'><div class='k kicker anim'>Uit onze DM's</div>
        <div class='hd anim'><div class='badge'>{bubble}</div>
        <div class='who'>anoniem<span>gedeeld met toestemming</span></div></div></div>
      <div class='mid'>
        <div class='bub in anim'>{vraag}</div>
        <div class='typing'><i></i><i></i><i></i></div>
        <div class='bub out anim'>{antwoord}</div>
      </div>
      <div class='foot'>{MARK.replace("mark'","mark anim'")}
        <div class='note anim'>vraag maar raak in de DM</div></div>
    </div>""", css, w, h)
    return html, round(4.7 + REST, 2)


# Style F, "Kinetic type". One scene, 2.5 s.
THEMES = {
    "open":  ("var(--indigo)", "var(--paper)", "var(--pink)"),
    "mint":  ("var(--mint)",   "var(--indigo)", "var(--pink)"),
    "peach": ("var(--peach)",  "var(--indigo)", "var(--pink)"),
    "pink":  ("var(--pink)",   "var(--paper)", "var(--indigo)"),
    "end":   ("var(--indigo)", "var(--paper)", "var(--peach)"),
}

def reel_scene_v(kind, lines, small="", w=1080, h=1920):
    bg, fg, ac = THEMES[kind]
    joined = " ".join(lines)
    size = 118 if len(joined) < 52 else 98
    css = f"""
    .stage{{background:{bg};color:{fg};padding:200px 90px 330px}}
    .bar{{width:160px;height:11px;background:{ac};border-radius:6px;
      transform-origin:left;animation:wipe .5s .05s}}
    .big{{font-family:'Athiti';font-size:{size}px;font-weight:600;line-height:1.06;
         letter-spacing:-.035em}}
    .big span{{display:block}}
    .big em{{font-style:normal;color:{ac};font-weight:700}}
    .sm{{margin-top:44px;font-size:38px;font-weight:400;line-height:1.42;
         opacity:.72;max-width:840px;animation:rise .7s 1.15s}}
    .mark{{font-size:30px;animation:fade .6s 1.2s}}
    .dot{{width:20px;height:20px;background:{ac}}}
    """
    ls = "".join(
        f"<span class='anim' style='animation:rise .7s {0.3 + i*0.26:.2f}s'>{t}</span>"
        for i, t in enumerate(lines))
    sm = f"<div class='sm anim'>{small}</div>" if small else ""
    html = page(f"""<div class='stage'>
      <div class='head'><div class='bar anim'></div></div>
      <div class='mid'><div class='big'>{ls}</div>{sm}</div>
      <div class='foot'>{MARK.replace("mark'","mark anim'")}</div>
    </div>""", css, w, h)
    # last thing to land is either the final headline line or the sub-line
    settle = max(0.3 + (len(lines) - 1) * 0.26 + 0.7,
                 1.15 + 0.7 if small else 0, 1.8)
    return html, round(settle + REST, 2)


# ===================================================== STYLE G, "ONDER ONS"
# The recognition pillar. No illustration: the line is the whole image, so the
# type fills the frame and the real logo is placed large enough to survive being
# screenshotted, cropped or reposted without a caption.
#
# The logo is two-coloured, so it always sits on an off-white surface, never
# straight on a saturated field. That off-white footer is the pillar's signature.
#
#   masthead  line left, off-white brand strip along the bottom
#   midden    line centred on a light field, logo centred underneath
#   vullend   line edge to edge, logo in an off-white chip in the corner

_LOGO = (pathlib.Path(__file__).parent / "brand" / "mijnpil-logo.png").resolve()
_LOGO_RATIO = 1489 / 350


def _logo(width, anim_style=""):
    return (f"<img class='logo{anim_style}' src='file://{_LOGO}' alt='MijnPil.nu' "
            f"style='width:{width}px;height:{width / _LOGO_RATIO:.0f}px'>")


MEME_THEMES = {
    # bg: the field. text: the line. acc: the one highlighted phrase.
    # paper: the surface the logo sits on, always off-white.
    # light: a pale field, where the logo label needs a hairline to read as a label.
    "roze":       {"bg": "#ea4f79", "text": "#fef5ff", "acc": "#f9d2b8",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": False,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
    "indigo":     {"bg": "#2c2e7b", "text": "#fef5ff", "acc": "#ea4f79",
                   "paper": "#fef5ff", "grain": "#fef5ff", "light": False,
                   "badge": "#ea4f79", "badgetext": "#fef5ff"},
    "lavendel":   {"bg": "#9e9dce", "text": "#2c2e7b", "acc": "#fef5ff",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": False,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
    "perzik":     {"bg": "#f9d2b8", "text": "#2c2e7b", "acc": "#ea4f79",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": True,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
    "mint":       {"bg": "#cfeae5", "text": "#2c2e7b", "acc": "#ea4f79",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": True,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
    "lichtblauw": {"bg": "#d4eff9", "text": "#2c2e7b", "acc": "#ea4f79",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": True,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
    "zalm":       {"bg": "#f9c1b7", "text": "#2c2e7b", "acc": "#ea4f79",
                   "paper": "#fef5ff", "grain": "#2c2e7b", "light": True,
                   "badge": "#2c2e7b", "badgetext": "#fef5ff"},
}

# the rotation the scheduled runs walk through, so no two posts in a row share
# a field colour
MEME_ROTATION = ["roze", "indigo", "lavendel"]


# character width of Athiti 600 relative to its font size, measured on the
# rendered face: used to fit the longest authored line to the column
_ATHITI = 0.455


def _fit(lines, avail, cap, per_char=None):
    per_char = per_char or _ATHITI
    longest = max(len(x.replace("<em>", "").replace("</em>", "")) for x in lines)
    return max(52, min(cap, int(avail / (longest * per_char))))


def _grain(col):
    return (f"<div class='grain' style=\"background-image:radial-gradient("
            f"circle,{col} 1.5px,transparent 1.6px)\"></div>")


BASE_G = """
.grain{position:absolute;inset:0;pointer-events:none;opacity:.18;
  background-size:15px 15px}
.eyebrow{font-family:'RobotoSlab';font-size:21px;font-weight:500;
  letter-spacing:.30em;text-transform:uppercase}
.line{font-family:'Athiti';font-weight:600;letter-spacing:-.032em;line-height:1.08}
.line span{display:block;white-space:nowrap}
.line em{font-style:normal;font-weight:700}
.logo{display:block}
"""


def _spans(lines, anim, t0, step=0.2):
    return "".join(
        (f"<span class='anim' style='animation:rise .65s {t0+i*step:.2f}s'>{x}</span>"
         if anim else f"<span>{x}</span>") for i, x in enumerate(lines))


def _eyebrow(anim, text="onder ons"):
    return "<div class='eyebrow%s'>%s</div>" % (
        " anim' style='animation:fade .5s .05s" if anim else "", text)


def _meme_masthead(lines, t, anim, w, h):
    strip_h = 198 if h <= 1400 else 240
    pad = 84
    size = _fit(lines, w - 2 * pad, 122 if h <= 1400 else 132)
    logo_w = 430 if h <= 1400 else 500
    css = BASE_G + f"""
    .stage{{background:{t['bg']};color:{t['text']};padding:{pad}px {pad}px {strip_h + 40}px}}
    .eyebrow{{color:{t['acc']}}}
    .rule{{width:132px;height:9px;border-radius:5px;background:{t['acc']};
      margin-top:26px;transform-origin:left}}
    .mid{{justify-content:center}}
    .line{{font-size:{size}px}}
    .line em{{color:{t['acc']}}}
    .strip{{position:absolute;left:0;right:0;bottom:0;height:{strip_h}px;
      background:{t['paper']};display:flex;align-items:center;justify-content:center}}
    """
    t_last = 0.75 + (len(lines) - 1) * 0.2 + 0.65
    strip = "<div class='strip%s'>%s</div>" % (
        " anim' style='animation:fade .6s %.2fs" % t_last if anim else "",
        _logo(logo_w))
    rl = "<div class='rule%s'></div>" % (
        " anim' style='animation:wipe .45s .3s" if anim else "")
    html = page(f"""<div class='stage'>{_grain(t['grain'])}
      <div class='head'>{_eyebrow(anim)}{rl}</div>
      <div class='mid'><div class='line'>{_spans(lines, anim, 0.75)}</div></div>
    </div>{strip}""", css, w, h)
    return html, (t_last + 0.6 if anim else 0)


def _meme_midden(lines, t, anim, w, h):
    """Light field only: the logo sits straight on the background."""
    pad = 92
    size = _fit(lines, w - 2 * pad, 112 if h <= 1400 else 122)
    logo_w = 400 if h <= 1400 else 460
    css = BASE_G + f"""
    .stage{{background:{t['bg']};color:{t['text']};align-items:center;
      text-align:center;padding:{pad}px}}
    .eyebrow{{color:{t['acc']};font-size:19px}}
    .mid{{align-items:center;gap:0;justify-content:center}}
    .line{{font-size:{size}px}}
    .line em{{color:{t['acc']}}}
    .sep{{width:150px;height:4px;background:{t['acc']};opacity:.6;margin:60px 0 42px}}
    .foot{{justify-content:center}}
    """
    t_last = 0.55 + len(lines) * 0.2
    logo = _logo(logo_w, " anim' style='animation:fade .6s %.2fs" % t_last if anim else "")
    html = page(f"""<div class='stage'>{_grain(t['grain'])}
      <div class='head'>{_eyebrow(anim)}</div>
      <div class='mid'><div class='line'>{_spans(lines, anim, 0.55)}</div>
        <div class='sep'></div>{logo}</div>
      <div class='foot'></div>
    </div>""", css, w, h)
    return html, (t_last + 0.6 if anim else 0)


def _meme_vullend(lines, t, anim, w, h, tag="eyebrow", face="athiti",
                  quotes=False, anchor="midden", badge=None, border=0):
    """tag:    where #vrouwenonderelkaar goes, "eyebrow" top left or "label"
               next to the logo.
    face:      "athiti" matches the uitlegposts, "slab" sets the line in Roboto
               Slab bold so the pillar reads as a different kind of post.
    quotes:    wrap the line in typographic quotation marks.
    anchor:    "midden" centres the block, "onder" pushes it against the logo
               so the silhouette in the feed differs from the uitlegposts."""
    pad = 68
    slab = face == "slab"
    cap = (150 if h <= 1400 else 160) if not slab else (120 if h <= 1400 else 130)
    size = _fit(lines, w - 2 * pad, cap, 0.56 if slab else _ATHITI)
    logo_w = 300 if h <= 1400 else 340
    css = BASE_G + f"""
    .stage{{background:{t['bg']};color:{t['text']};padding:{pad}px;
      {f"box-shadow:inset 0 0 0 {border}px {t['badge']}" if border else ""}}}
    .mid{{justify-content:{'flex-end' if anchor == 'onder' else 'center'}}}
    .line{{font-size:{size}px;line-height:{1.14 if slab else 1.02};
      {"font-family:'RobotoSlab';font-weight:700;letter-spacing:-.018em" if slab else ""}}}
    .line em{{color:{t['acc']}}}
    .foot{{margin-top:{54 if anchor == 'onder' else 0}px}}
    .head{{display:flex;align-items:center;justify-content:space-between;gap:24px}}
    .badge{{font-family:'Athiti';font-size:26px;font-weight:600;letter-spacing:.02em;
      background:{t['badge']};color:{t['badgetext']};border-radius:999px;
      padding:11px 26px 13px;white-space:nowrap;line-height:1}}
    .foot{{align-items:center;justify-content:flex-start}}
    .chip{{background:{t['paper']};border-radius:999px;padding:26px 40px;
      display:flex;align-items:center;
      border:{'3px solid #2c2e7b1f' if t['light'] else '0'}}}
    .head .eyebrow{{color:{t['acc']};font-size:19px}}
    """
    css += f"""
    .chip .hash{{font-family:'RobotoSlab';font-size:27px;font-weight:500;
      color:{t['bg'] if t['light'] else '#2c2e7b'};margin-left:26px;
      padding-left:26px;border-left:2px solid #2c2e7b26;white-space:nowrap}}
    """
    if quotes:
        lines = list(lines)
        lines[0] = "\u201c" + lines[0]
        lines[-1] = lines[-1] + "\u201d"
    t_last = 0.5 + len(lines) * 0.2
    inner = _logo(logo_w if tag != "label" else int(logo_w * 0.8))
    if tag == "label":
        inner += "<span class='hash'>#vrouwenonderelkaar</span>"
    chip = "<div class='chip%s'>%s</div>" % (
        " anim' style='animation:pop .6s %.2fs" % t_last if anim else "", inner)
    eb_text = "#vrouwenonderelkaar" if tag == "eyebrow" else "onder ons"
    bd = ("<div class='badge%s'>%s</div>"
          % (" anim' style='animation:pop .5s .15s" if anim else "", badge)
          if badge else "")
    html = page(f"""<div class='stage'>{_grain(t['grain'])}
      <div class='head'>{_eyebrow(anim, eb_text)}{bd}</div>
      <div class='mid'><div class='line'>{_spans(lines, anim, 0.5)}</div></div>
      <div class='foot'>{chip}</div>
    </div>""", css, w, h)
    return html, (t_last + 0.6 if anim else 0)


LAYOUTS = {"masthead": _meme_masthead, "midden": _meme_midden,
           "vullend": _meme_vullend}


def onder_ons(lines, layout="vullend", theme="roze", w=1080, h=1350,
              tag="eyebrow", **kw):
    """Static 4:5 feed post. The shareable unit of this pillar."""
    f = LAYOUTS[layout]
    args = (lines, MEME_THEMES[theme], False, w, h)
    return (f(*args, tag=tag, **kw) if layout == "vullend" else f(*args))[0]


def onder_ons_v(lines, layout="vullend", theme="roze", w=1080, h=1920,
                tag="eyebrow", **kw):
    """Animated 9:16 story or reel cut of the same post."""
    f = LAYOUTS[layout]
    args = (lines, MEME_THEMES[theme], True, w, h)
    html, settle = f(*args, tag=tag, **kw) if layout == "vullend" else f(*args)
    return html, round(settle + REST, 2)
