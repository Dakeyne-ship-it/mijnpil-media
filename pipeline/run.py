"""One scheduled run: render today's queue item, push it, print what to publish.

    python3 pipeline/run.py                 # today, Europe/Amsterdam
    python3 pipeline/run.py --date 2026-09-14
    python3 pipeline/run.py --date 2026-09-14 --dry-run   # render, do not push

Prints a JSON block on stdout between BEGIN PUBLISH and END PUBLISH. The calling
session reads that block and does the publishing through Windsor, because
publishing needs an MCP tool this script cannot reach.

Exit codes: 0 = something to publish (or nothing scheduled today), 1 = failed.
"""
import json, os, sys, subprocess, base64, datetime, zoneinfo, pathlib, shutil

HERE = pathlib.Path(__file__).parent.resolve()
REPO = HERE.parent
QUEUE = json.loads((HERE / "queue.json").read_text(encoding="utf-8"))
TZ = zoneinfo.ZoneInfo("Europe/Amsterdam")
PAGES = "https://dakeyne-ship-it.github.io/mijnpil-media"
REMOTE = "https://github.com/Dakeyne-ship-it/mijnpil-media.git"

# git in this environment must not use the session's own credentials, and the
# token has to travel as a header: the proxy strips it from the URL.
GIT_ENV_STRIP = ["GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0",
                 "GIT_CONFIG_KEY_1", "GIT_CONFIG_VALUE_1", "GIT_CONFIG_KEY_2",
                 "GIT_CONFIG_VALUE_2", "GIT_ASKPASS", "GH_TOKEN", "GITHUB_TOKEN"]


def git(*args, token=None):
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_STRIP}
    cmd = ["git", "-C", str(REPO)]
    if token:
        b64 = base64.b64encode(f"x-access-token:{token}".encode()).decode()
        cmd += ["-c", f"http.extraHeader=Authorization: Basic {b64}"]
    cmd += list(args)
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{r.stderr.strip()}")
    return r.stdout.strip()


def main():
    argv = sys.argv[1:]
    dry = "--dry-run" in argv
    if "--date" in argv:
        day = argv[argv.index("--date") + 1]
    else:
        day = datetime.datetime.now(TZ).date().isoformat()

    post = next((p for p in QUEUE["posts"] if p["date"] == day), None)
    if post is None:
        print(f"NO POST TODAY ({day}). Niets te doen.")
        return 0

    token = os.environ.get("MIJNPIL_GH_TOKEN")
    if not token and not dry:
        print("FOUT: zet MIJNPIL_GH_TOKEN. Het token staat in de projectdocumentatie "
              "onder claude/instagram-toegang-en-beeldhost.md", file=sys.stderr)
        return 1

    sys.path.insert(0, str(HERE))
    import produce
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        paths = produce.build(b, post)
        b.close()

    year, month = day[:4], day[5:7]
    dest = REPO / "ig" / year / month
    dest.mkdir(parents=True, exist_ok=True)
    names = []
    for p in paths:
        shutil.copy(p, dest / p.name)
        names.append(p.name)

    urls = [f"{PAGES}/ig/{year}/{month}/{n}" for n in names]

    if not dry:
        git("add", "-A")
        status = git("status", "--porcelain")
        if status:
            git("-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com",
                "commit", "-q", "-m", f"{post['id']}: {post['subject']}")
            git("push", REMOTE, "main", token=token)
            print("gepusht naar de beeldhost")
        else:
            print("niets gewijzigd, beeld stond er al")

    block = {
        "id": post["id"],
        "date": post["date"],
        "slot": post["slot"],
        "subject": post["subject"],
        "concept": post["concept"],
        "format": post["format"],
        "urls": urls,
        "caption": post["caption"] + "\n\n" + " ".join(post["tags"]),
        "disclaimer_comment": QUEUE["_meta"]["disclaimer"] if post.get("disclaimer") else None,
        "wait_for_pages_seconds": 100,
    }
    print("BEGIN PUBLISH")
    print(json.dumps(block, ensure_ascii=False, indent=2))
    print("END PUBLISH")
    return 0


if __name__ == "__main__":
    sys.exit(main())
