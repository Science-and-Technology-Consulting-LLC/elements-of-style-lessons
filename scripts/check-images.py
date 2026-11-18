#!/usr/bin/env python3
"""Check every picture link in the lessons and case studies.

Run it from the repository folder before you push:

    python scripts/check-images.py            # checks files on your disk
    python scripts/check-images.py --online   # also fetches web addresses

It reads the .md files and the Markdown cells of the .ipynb files, and reports:

  * a picture whose file is missing (a relative path such as assets/x.png),
  * a picture link that is a GitHub page (github.com/.../blob/...), not a picture,
  * a broken picture line, such as a missing ] or ),
  * with --online, a web address that does not return a picture.

It exits with 1 if it found a problem, so a script or GitHub Actions can stop on it.
It also counts the "Picture to add" notes that still wait for a picture.
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

IMAGE_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE_HTML = re.compile(r"<img\b[^>]*?\bsrc=\"([^\"]+)\"", re.I)
SKIP_DIRS = {".ipynb_checkpoints", "_build", "build", ".git", "node_modules"}


def sources(root: Path):
    """Yield (path, text) for each file to check. A notebook gives its Markdown cells."""
    for folder in ("lessons", "case-studies"):
        base = root / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if SKIP_DIRS & set(path.parts):
                continue
            if path.suffix == ".md":
                yield path, path.read_text(encoding="utf-8")
            elif path.suffix == ".ipynb":
                nb = json.loads(path.read_text(encoding="utf-8"))
                cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "markdown"]
                yield path, "\n".join("".join(c.get("source", [])) for c in cells)


def web_check(url: str):
    """Return None if the address returns a picture, else a short reason."""
    req = urllib.request.Request(url, headers={"User-Agent": "check-images"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            kind = r.headers.get("Content-Type", "")
    except Exception as err:  # network and HTTP errors both land here
        return f"cannot fetch ({err})"
    return None if kind.startswith("image/") else f"returns {kind or 'no content type'}, not a picture"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--online", action="store_true", help="also fetch each web address")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="repository folder")
    args = ap.parse_args()
    root = Path(args.root)

    problems, checked, waiting = [], 0, 0
    seen_web = {}
    for path, text in sources(root):
        name = path.relative_to(root).as_posix()
        waiting += text.count("Picture to add")
        for number, line in enumerate(text.split("\n"), 1):
            if "![" in line and not IMAGE_MD.search(line):
                problems.append(f"{name}: broken picture line (missing ] or ) ?): {line.strip()[:90]}")
        for target in IMAGE_MD.findall(text) + IMAGE_HTML.findall(text):
            checked += 1
            if target.startswith(("http://", "https://")):
                if re.match(r"https://github\.com/[^/]+/[^/]+/(blob|tree)/", target):
                    problems.append(f"{name}: {target.rsplit('/', 1)[-1]} is a GitHub page, not a picture "
                                    "(use assets/<file> or raw.githubusercontent.com)")
                elif args.online:
                    if target not in seen_web:
                        seen_web[target] = web_check(target)
                    if seen_web[target]:
                        problems.append(f"{name}: {target.rsplit('/', 1)[-1]} {seen_web[target]}")
            elif not target.startswith(("data:", "#", "mailto:")):
                file = (path.parent / target.split("#")[0]).resolve()
                if not file.is_file():
                    problems.append(f"{name}: picture file not found: {target}")

    for p in problems:
        print("PROBLEM", p)
    print(f"{checked} picture links checked, {len(problems)} problems, {waiting} 'Picture to add' notes waiting.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
