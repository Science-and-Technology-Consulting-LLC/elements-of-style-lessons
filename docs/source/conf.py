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
import sys

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

# Suppress warnings about heading levels skipping (common with MyST-NB).
suppress_warnings = ["myst.header"]

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "Elements of Style — Lessons"
html_short_title = "Elements of Style — Lessons"
html_baseurl = "https://science-and-technology-consulting-llc.github.io/elements-of-style-lessons/"

# Theme options chosen for parity with Annie's MkDocs ReadTheDocs theme.
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
    """Return the canonical file path (relative to repo root) for a shim
    page, or None if this page isn't a shim that needs overriding.
    """
    if not pagename.startswith("lessons/"):
        return None
    # The git-survival-guide page is a sub-asset of the version-control lesson
    if pagename == "lessons/git-survival-guide":
        return "lessons/version-control/git-survival-guide.md"
    # Standard lesson shim
    topic = pagename.split("/", 1)[1]
    return f"lessons/{topic}/README.md"


def _add_canonical_edit_path(app, pagename, templatename, context, doctree):
    canonical = _canonical_edit_path_for(pagename)
    if canonical:
        context["canonical_edit_path"] = canonical


def setup(app):
    app.connect("html-page-context", _add_canonical_edit_path)
