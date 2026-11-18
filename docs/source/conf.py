# Configuration file for the Sphinx documentation builder.
#
# Elements of Style in Creating Workflows for Biomedical Research in the Era of Agentic AI
# A pragmatic set of lessons for biomedical workflow creation.
#
# Mirrors the pattern used in sibling repo `sc-nsforest-qc-nf`:
#   - sphinx_rtd_theme for visual continuity with the MkDocs reference sites
#   - MyST (myst-parser) so pages can be authored in Markdown
#   - MyST-NB so Jupyter notebooks (.ipynb) render with their saved outputs
#
# Full Sphinx options: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
import sys
from pathlib import Path

# Make the repo root importable in case future autodoc needs it
# (e.g., when Typer CLIs land — see curriculum/06-typer-clis.md)
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "Elements of Style in Creating Workflows for Biomedical Research in the Era of Agentic AI"
copyright = "2026, Anne Deslattes Mays"
author = "Anne Deslattes Mays"
release = "0.1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    # myst_nb subsumes myst_parser — listing both registers the same config
    # twice and the build aborts. Keep just myst_nb for both .md and .ipynb.
    "myst_nb",             # Jupyter notebook rendering (.ipynb) + Markdown (.md)
    "sphinx_copybutton",   # one-click copy on code blocks
    "sphinx_design",       # grids, cards, tabs (used on landing page)
]

# Source suffixes. myst_nb registers .md and .ipynb with parser name "myst-nb"
# at extension setup time; we only need to declare .rst explicitly here.
source_suffix = {
    ".rst": "restructuredtext",
}

# MyST extensions — pick the ones the MkDocs reference relies on:
#   colon_fence  → ::: admonitions, just like MkDocs
#   deflist      → definition lists (used in "Bridge patterns")
#   attrs_inline → ![alt](img.png){width=500} for image sizing
#   html_image   → raw <img> tags (useful for screenshots)
#   linkify      → bare URLs become links
#   substitution → {{ variable }} replacements
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_inline",
    "html_image",
    "linkify",
    "substitution",
]

# Notebook execution: do NOT execute at build time. The starter notebooks
# can be re-executed by the author or the learner; CI only validates that the
# .ipynb files parse and renders the saved outputs.
nb_execution_mode = "off"

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "jupyter_execute",
]

# Suppress:
#   myst.header       — heading-level jumps (common with MyST-NB includes)
#
# myst.xref_missing is NOT suppressed: a lesson link that does not resolve to
# a Sphinx document is a dead link on the site, and the build should say so.
# Lesson links use "../<topic>/index.md" for lessons, "<page>.md" for sibling
# pages, and full GitHub URLs for files outside docs/.
suppress_warnings = ["myst.header"]

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "Elements of Style — Lessons"
html_short_title = "Elements of Style — Lessons"
html_baseurl = "https://science-and-technology-consulting-llc.github.io/elements-of-style-lessons/"

# Theme options chosen for parity with the MkDocs ReadTheDocs theme of the sibling sites.
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": False,
}

# GitHub source link in the header (RTD theme convention).
html_context = {
    "display_github": True,
    "github_user": "Science-and-Technology-Consulting-LLC",
    "github_repo": "elements-of-style-lessons",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}


# -- "Edit on GitHub" override for include-shim pages -----------------------
#
# Lesson narratives live at `lessons/<topic>/README.md` (canonical).
# `docs/source/lessons/<topic>.md` are include-shims that pull the
# canonical content in so Sphinx can render it.
#
# Without this override, "Edit on GitHub" lands on the shim. We want it to
# land directly on the canonical README — one click, the right file.
#
# The override sets `canonical_edit_path` in the page context; the
# overridden `_templates/breadcrumbs.html` uses it when present.

def _canonical_edit_path_for(pagename: str) -> str | None:
    """Return the canonical repo-relative file path for a shim page,
    or None if this page isn't a shim that needs overriding.

    Shim layout after the flatten:
      docs/source/lessons/<topic>/index.md          → shim for lessons/<topic>/README.md
      docs/source/lessons/<topic>/<walkthrough>.md  → shim for lessons/<topic>/<walkthrough>.md

    pagename (no extension) matches one of:
      "lessons/<topic>/index"
      "lessons/<topic>/<walkthrough>"
      "lessons/git-survival-guide"      (legacy flat sub-asset)
    """
    if not pagename.startswith("lessons/"):
        return None

    # git-survival-guide lives at the version-control lesson root
    if pagename == "lessons/git-survival-guide":
        return "lessons/version-control/git-survival-guide.md"

    rest = pagename[len("lessons/"):]
    if rest.endswith("/index"):
        topic = rest[:-len("/index")]
        return f"lessons/{topic}/README.md"
    if "/" in rest:
        # A walkthrough shim: docs/source/lessons/<topic>/<name>.md
        return f"lessons/{rest}.md"
    # Legacy flat form — shouldn't occur post-flatten, but safe.
    return f"lessons/{rest}/README.md"


def _add_canonical_edit_path(app, pagename, templatename, context, doctree):
    canonical = _canonical_edit_path_for(pagename)
    if not canonical and pagename.startswith("case-studies/"):
        name = pagename[len("case-studies/"):]
        canonical = "case-studies/README.md" if name == "index" else f"case-studies/{name}/README.md"
    if canonical:
        context["canonical_edit_path"] = canonical


# -- Links that work on GitHub and on this site ------------------------------
#
# The lesson and case-study pages are written for GitHub: a link to another
# lesson ends in `README.md`, which GitHub opens as that lesson's page. On
# this site each lesson page is `index.md`, and each case study is
# `case-studies/<name>.md`. So that one source file serves both, the links are
# rewritten as the page is pulled in by an `{include}` in a shim page.
# Full web addresses (http, https) are never touched.

_CASE_STUDIES = (
    "sc-nsforest-qc-nf", "endometriosis", "oadr-autoantibody", "oadr-cpep",
    "lrp2", "multiqc-workflow", "nlm-ckn",
)
_CASE_NAMES = "|".join(re.escape(n) for n in _CASE_STUDIES)


def _site_links(text: str, source_path: str) -> str:
    """`source_path` is the included file, such as ../../case-studies/lrp2/README.md."""
    if "case-studies/" in source_path:
        # The shim page sits one folder up from the source file it includes.
        text = re.sub(r"\]\((?:\.\./)+lessons/", "](../lessons/", text)
        text = re.sub(r"\]\(\.\./(%s)/README\.md" % _CASE_NAMES, r"](\1.md", text)
        text = re.sub(r"\]\((%s)/(?:README\.md)?(?=[)#])" % _CASE_NAMES, r"](\1.md", text)
        if not source_path.endswith("case-studies/README.md"):
            text = re.sub(r"\]\(\.\./README\.md", "](index.md", text)
    # A case study linked from a lesson, or by its folder, is a page of its own on the site.
    text = re.sub(r"\]\(((?:\.\./)+)case-studies/(%s)/README\.md" % _CASE_NAMES, r"](\1case-studies/\2.md", text)
    text = re.sub(r"\]\(\.\./(%s)/(?=[)#])" % _CASE_NAMES, r"](\1.md", text) if "case-studies/" in source_path else text
    # README.md at the end of a path becomes index.md; web addresses are skipped.
    return re.sub(r"\]\((?!https?:)((?:[^)\s]*/)?)README\.md", r"](\1index.md", text)


# -- Pictures: write `assets/name.png`, it works everywhere ------------------
#
# A lesson names its pictures with a plain relative path, such as
# `![Menu bar](assets/menu-bar.png)`. That path works on GitHub and in
# JupyterLab as it stands, because it is relative to the lesson's own folder.
# On this site the lesson is pulled in by a shim page that lives in another
# folder, so the same path would point at nothing. The rewrite below points
# it back at the picture in the lesson's folder. Web addresses are not touched.

_IMAGE_MD = re.compile(r"(!\[[^\]]*\]\()(?!https?:|/|#|data:|mailto:)([^)\s]+)")
_IMAGE_HTML = re.compile(r"(<img\b[^>]*?\bsrc=\")(?!https?:|/|data:)([^\"]+)")


def _site_images(app, text: str, source_path: str) -> str:
    """Point relative picture paths in an included file at the file's own folder."""
    posix = Path(source_path).as_posix()
    m = re.search(r"((?:lessons|case-studies)/.*)$", posix)
    if not m:
        return text
    repo_root = Path(app.srcdir).resolve().parent.parent
    source_rel = Path(m.group(1))
    source_dir = (repo_root / source_rel).parent
    # The shim page sits at docs/source/lessons/<topic>/, mirroring the lesson's
    # folder, or at docs/source/case-studies/ for any case study.
    if source_rel.parts[0] == "case-studies":
        shim_dir = Path(app.srcdir).resolve() / "case-studies"
    else:
        shim_dir = Path(app.srcdir).resolve() / source_rel.parent

    def fix(match):
        target = (source_dir / match.group(2)).resolve()
        return match.group(1) + Path(os.path.relpath(target, shim_dir)).as_posix()

    return _IMAGE_HTML.sub(fix, _IMAGE_MD.sub(fix, text))


def _rewrite_included_links(app, relative_path, parent_docname, content):
    source = Path(relative_path).as_posix()
    text = _site_links(content[0], source)
    content[0] = _site_images(app, text, source)


def setup(app):
    app.connect("html-page-context", _add_canonical_edit_path)
    app.connect("include-read", _rewrite_included_links)
