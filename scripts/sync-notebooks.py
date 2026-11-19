#!/usr/bin/env python3
"""Rebuild each lesson notebook from its .md page, so you edit only one file.

The .md page is the page of record. The notebook keeps its code cells exactly as
they are; only the text between them is taken from the page. A code block in the
page becomes a notebook cell only if its content equals the next unmatched code
cell of the notebook, so an example block inside the text stays text.

Run it from the repository folder:

    python scripts/sync-notebooks.py                 # every lesson page that has a notebook
    python scripts/sync-notebooks.py lessons/containers/building-dockerfiles.md
    python scripts/sync-notebooks.py --check         # report problems, write nothing

To change a command, change it in the page and in the notebook cell, in the same
way. The script stops with an error if a code cell cannot be found in the page.
Outputs are cleared from the notebooks it writes. The README.md of a lesson has
no notebook and is skipped.
"""
import argparse
import glob
import json
import os
import re
import sys

LANG = {"bash": "bash", "python3": "python", "ir": "r"}


def lines(text):
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])


def rebuild(md_path, nb_path):
    """Return (errors, notebook) for the page and its notebook."""
    nb = json.load(open(nb_path, encoding="utf-8"))
    md = open(md_path, encoding="utf-8").read()
    lang = LANG.get(nb["metadata"].get("kernelspec", {}).get("name", "bash"), "bash")
    codes = [c for c in nb["cells"] if c["cell_type"] == "code"]
    fence = re.compile(r"^(`{3,})%s\n(.*?)\n\1[ \t]*$" % lang, re.S | re.M)

    spans, ci = [], 0
    for m in fence.finditer(md):
        if ci < len(codes) and m.group(2) == "".join(codes[ci]["source"]).rstrip("\n"):
            spans.append((m.start(), m.end(), codes[ci]))
            ci += 1
    errors = []
    if ci != len(codes):
        errors.append("found %d of %d code cells in the page" % (ci, len(codes)))

    def text_cell(text):
        text = text.strip("\n")
        return {"cell_type": "markdown", "metadata": {}, "source": lines(text)} if text.strip() else None

    cells, pos = [], 0
    for start, end, code in spans:
        cell = text_cell(md[pos:start])
        if cell:
            cells.append(cell)
        code = dict(code)
        code["outputs"], code["execution_count"] = [], None
        cells.append(code)
        pos = end
    cell = text_cell(md[pos:])
    if cell:
        cells.append(cell)
    nb["cells"] = cells
    return errors, nb


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*", help="lesson pages (.md); default: all that have a notebook")
    ap.add_argument("--check", action="store_true", help="report problems and write nothing")
    args = ap.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pages = args.pages or sorted(glob.glob(os.path.join(root, "lessons", "*", "*.md")))
    problems = done = 0
    for md in pages:
        nbp = os.path.splitext(md)[0] + ".ipynb"
        if os.path.basename(md) == "README.md" or not os.path.exists(nbp):
            continue
        errors, nb = rebuild(md, nbp)
        if errors:
            problems += 1
            print("PROBLEM", os.path.relpath(md, root), "-", "; ".join(errors))
            continue
        done += 1
        if not args.check:
            with open(nbp, "w", encoding="utf-8") as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
                f.write("\n")
    print("%d notebooks %s, %d problems." % (done, "checked" if args.check else "rebuilt", problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
