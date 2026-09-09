import math
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
def anatomie(w=1080, h=1350):
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
    pills = ""
    for i in range(28):
        col, row = i % 7, i // 7
        cx, cy = 66 + col * 84, 232 + row * 84
        if i < 21:
            pills += f"<circle cx='{cx}' cy='{cy}' r='29' fill='#2c2e7b'/>"
        else:
            pills += (f"<circle cx='{cx}' cy='{cy}' r='29' fill='none' stroke='#ea4f79' "
                      f"stroke-width='2.5' stroke-dasharray='7 6'/>")
    callouts = """
      <path d='M 596 232 L 700 232 L 700 150' fill='none' stroke='#ea4f79' stroke-width='2'/>
      <circle cx='700' cy='131' r='19' fill='#ea4f79'/>
      <text class='num' x='700' y='139' text-anchor='middle'>1</text>
      <text class='lbl' x='596' y='68'>21 hormoondagen</text>
      <text class='sub' x='596' y='102'>elke dag rond hetzelfde tijdstip</text>

      <path d='M 596 484 L 700 484 L 700 566' fill='none' stroke='#ea4f79' stroke-width='2'/>
      <circle cx='700' cy='585' r='19' fill='#ea4f79'/>
      <text class='num' x='700' y='593' text-anchor='middle'>2</text>
      <text class='lbl' x='596' y='646'>7 stopdagen</text>
      <text class='sub' x='596' y='680'>de bloeding hier is een</text>
      <text class='sub' x='596' y='706'>onttrekkingsbloeding</text>
    """
    return page(f"""<div class='stage'>
      <div class='head'><div class='k kicker'>Anatomie van</div>
        <div class='t'>Een strip<br>van 28 dagen</div></div>
      <div class='mid plate'><svg width='928' height='760'>{pills}{callouts}</svg></div>
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


# Style D, "Soft data illustration" in motion: the curve draws itself.
def cyclus_v(w=1080, h=1920):
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
