"""Shared page shell: brand type, brand palette, layout frame, animation base.

Fonts ship inside this repository so a fresh container needs no npm install.
"""
import pathlib

FONTS = (pathlib.Path(__file__).parent / "fonts").resolve()

BASE = """
<style>
@font-face{font-family:'Athiti';src:url('file://FONTS/athiti-latin-400-normal.woff2') format('woff2');font-weight:400}
@font-face{font-family:'Athiti';src:url('file://FONTS/athiti-latin-500-normal.woff2') format('woff2');font-weight:500}
@font-face{font-family:'Athiti';src:url('file://FONTS/athiti-latin-600-normal.woff2') format('woff2');font-weight:600}
@font-face{font-family:'Athiti';src:url('file://FONTS/athiti-latin-700-normal.woff2') format('woff2');font-weight:700}
@font-face{font-family:'RobotoSlab';src:url('file://FONTS/roboto-slab-latin-400-normal.woff2') format('woff2');font-weight:400}
@font-face{font-family:'RobotoSlab';src:url('file://FONTS/roboto-slab-latin-500-normal.woff2') format('woff2');font-weight:500}
@font-face{font-family:'RobotoSlab';src:url('file://FONTS/roboto-slab-latin-700-normal.woff2') format('woff2');font-weight:700}
:root{
  --indigo:#2c2e7b; --pink:#ea4f79; --peach:#f9d2b8; --mint:#cfeae5;
  --blush:#f9c1b7; --lilac:#9e9dce; --sky:#d4eff9; --paper:#fef5ff;
  --pad:76px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:WIDTHpx;height:HEIGHTpx;overflow:hidden}
body{font-family:'RobotoSlab',Georgia,serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,.title{font-family:'Athiti',ui-sans-serif,system-ui,sans-serif}

.stage{position:absolute;inset:0;display:flex;flex-direction:column;
       padding:var(--pad);overflow:hidden}
.head{flex:0 0 auto}
.mid{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;min-height:0}
.foot{flex:0 0 auto;display:flex;align-items:flex-end;justify-content:space-between}

.kicker{font-family:'RobotoSlab';font-size:18px;font-weight:500;
        letter-spacing:.17em;text-transform:uppercase}
.mark{font-family:'RobotoSlab';display:flex;align-items:center;gap:12px;
      font-size:21px;font-weight:500;letter-spacing:.01em}
.dot{width:15px;height:15px;border-radius:50%;background:var(--pink);flex:0 0 auto}
.note{font-family:'RobotoSlab';font-size:18px;font-weight:400;opacity:.5}

/* every animation is authored paused; the renderer scrubs currentTime */
.anim{animation-fill-mode:both;animation-play-state:paused;
      animation-timing-function:cubic-bezier(.22,.75,.28,1)}
@keyframes rise{from{opacity:0;transform:translateY(46px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes pop{0%{opacity:0;transform:scale(.86)}60%{opacity:1;transform:scale(1.03)}
               100%{opacity:1;transform:scale(1)}}
@keyframes wipe{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes draw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
/* the animation shorthand in each concept resets fill-mode, so force it back:
   without this, elements are visible before their delay has elapsed */
*{animation-fill-mode:both!important}
</style>
"""


def page(body, css="", w=1080, h=1350):
    return ("<html><head><meta charset='utf-8'>"
            + BASE.replace("FONTS", str(FONTS)).replace("WIDTH", str(w)).replace("HEIGHT", str(h))
            + "<style>" + css + "</style></head><body>" + body + "</body></html>")
