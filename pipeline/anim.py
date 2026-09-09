"""Render a paused-CSS-animation page to a frame sequence, then to MP4."""
import sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
HTML = HERE / "html"; OUT = HERE / "out"; FR = HERE / "frames"
for d in (HTML, OUT, FR): d.mkdir(exist_ok=True)

FPS = 25

SCRUB = """(t) => {
  document.getAnimations().forEach(a => {
    try { a.pause(); a.currentTime = t; } catch(e) {}
  });
}"""


def render_clip(browser, name, html, dur, w, h):
    """Screenshot every frame of one animated page; return the frame directory."""
    d = FR / name
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
    f = HTML / f"{name}.html"
    f.write_text(html, encoding="utf-8")
    pg = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
    pg.goto(f"file://{f}")
    pg.wait_for_timeout(400)
    n = int(round(dur * FPS))
    for i in range(n):
        pg.evaluate(SCRUB, i * 1000.0 / FPS)
        pg.screenshot(path=str(d / f"{i:04d}.jpg"), type="jpeg", quality=88)
    pg.close()
    print(f"  {name}: {n} frames @ {w}x{h}")
    return d, n


def encode(frame_dirs, out_name):
    """Concatenate frame directories in order into one MP4."""
    stage = FR / f"_{out_name}"
    if stage.exists(): shutil.rmtree(stage)
    stage.mkdir(parents=True)
    k = 0
    for d in frame_dirs:
        for p in sorted(d.glob("*.jpg")):
            (stage / f"{k:05d}.jpg").symlink_to(p)
            k += 1
    out = OUT / f"{out_name}.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
        "-i", str(stage / "%05d.jpg"),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-shortest", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k",
        "-movflags", "+faststart", str(out)], check=True)
    shutil.rmtree(stage)
    print(f"  -> {out.name} ({k} frames, {k/FPS:.1f}s)")
    return out
