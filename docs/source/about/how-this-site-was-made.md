# How this site was made

This site is built with [Sphinx](https://www.sphinx-doc.org/), the
documentation generator behind the official Python docs and thousands of
other technical sites. We chose Sphinx for three reasons:

1. **Teaching with Sphinx.** Voice and tool continuity matter.
2. **It pairs naturally with notebooks.** Via `myst-nb`, the same parser
   handles Markdown pages *and* Jupyter notebooks, so the curriculum and
   the worked-example notebooks live side by side.
3. **It deploys to GitHub Pages from one workflow file** — see
   `.github/workflows/docs.yml` in this repo.

## The pieces

| Piece | Tool | Where it lives |
|-------|------|----------------|
| Pages | Markdown via [MyST](https://myst-parser.readthedocs.io/) | `docs/source/**/*.md` |
| Notebooks | Jupyter via [myst-nb](https://myst-nb.readthedocs.io/) | `ipynb/*.ipynb` |
| Theme | [`sphinx_rtd_theme`](https://sphinx-rtd-theme.readthedocs.io/) | `docs/source/conf.py` |
| Code copy buttons | [`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/) | `docs/source/conf.py` |
| Grids, cards, admonitions | [`sphinx-design`](https://sphinx-design.readthedocs.io/) | `docs/source/conf.py` |
| Build + deploy | GitHub Actions | `.github/workflows/docs.yml` |

## Build it locally

```bash
conda env create -f environment.yml   # one time
conda activate eos
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

## Build it in CI

Every push to `main` triggers `.github/workflows/docs.yml`, which:

1. Installs Sphinx and the four extensions named in the table above.
2. Runs `sphinx-build -b html docs/source docs/build/html`.
3. Uploads the result as a Pages artifact and deploys it to
   <https://adeslatt.github.io/elements-of-style-workflows/>.

The pattern is borrowed (with thanks) from the sibling NIH-NLM project
[`sc-nsforest-qc-nf`](https://github.com/Science-and-Technology-Consulting-LLC/sc-nsforest-qc-nf).

## Add a new page

1. Create a new `.md` (or `.ipynb`) file under `docs/source/` (or
   `ipynb/`, then symlinked).
2. Add its filename to the nearest `toctree` block — usually in
   `docs/source/index.md` or one of the section `index.md` files.
3. Run `make html` and reload the browser.

That's it. No DSL to learn beyond Markdown.

## Acknowledgements

The voice and structure are descended from the author's
[Kids First + INCLUDE training site](https://github.com/NIH-NICHD/Kids-First-INCLUDE-Elements-of-Style-Workflow-Creation-Maintenance)
and her CAVATICA training. The Sphinx pattern is descended from
[`sc-nsforest-qc-nf`](https://github.com/Science-and-Technology-Consulting-LLC/sc-nsforest-qc-nf).
