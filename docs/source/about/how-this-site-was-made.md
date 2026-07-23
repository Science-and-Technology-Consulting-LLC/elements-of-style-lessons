# How this site was made

This site is built with [Sphinx](https://www.sphinx-doc.org/), the
documentation generator behind the official Python docs and thousands
of other technical sites. Three reasons for choosing Sphinx:

1. **Sphinx is taught in the curriculum.** Voice and tool continuity
   matter — using the tool you teach is the cleanest demonstration of
   why the tool earns its place.
2. **It pairs naturally with notebooks.** Via `myst-nb`, the same
   parser handles Markdown pages *and* Jupyter notebooks, so the
   curriculum and the worked-example notebooks live side by side.
3. **It deploys to GitHub Pages from one workflow file** — see
   `.github/workflows/docs.yml` in this repo.

## The pieces

| Piece | Tool | Where it lives |
|-------|------|----------------|
| Pages | Markdown via [MyST](https://myst-parser.readthedocs.io/) | `lessons/<topic>/README.md` (canonical), `docs/source/lessons/<topic>.md` (include-shim) |
| Notebooks | Jupyter via [myst-nb](https://myst-nb.readthedocs.io/) | `lessons/<topic>/notebooks/{python,r}.ipynb` and `lessons/<topic>/eye-candy/{python,r}.ipynb` |
| Theme | [`sphinx_rtd_theme`](https://sphinx-rtd-theme.readthedocs.io/) | `docs/source/conf.py` |
| Code copy buttons | [`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/) | `docs/source/conf.py` |
| Grids, cards, admonitions, tabs | [`sphinx-design`](https://sphinx-design.readthedocs.io/) | `docs/source/conf.py` |
| Build + deploy | GitHub Actions | `.github/workflows/docs.yml` |
| Notebook + Dockerfile lint | GitHub Actions | `.github/workflows/ci.yml` |

## Build it locally

```bash
conda env create -f eos.yml   # one time
conda activate eos
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

## Build it in CI

Every push to `main` triggers `.github/workflows/docs.yml`, which:

1. Installs Sphinx and the extensions named in the table above.
2. Runs `sphinx-build -b html docs/source docs/build/html`.
3. Uploads the result as a Pages artifact and deploys it to
   <https://science-and-technology-consulting-llc.github.io/elements-of-style-lessons/>.

The pattern is borrowed (with thanks) from the sibling project
[`NIH-NLM/sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf).

## Add a new page

1. Create a new directory `lessons/<new-topic>/` with a `README.md` inside
   (and optionally `notebooks/`, `eye-candy/`).
2. Add an include-shim at `docs/source/lessons/<new-topic>.md` pointing
   at that README:

   ```markdown
   ```{include} ../../../lessons/<new-topic>/README.md
   ```
   ```

3. Add `lessons/<new-topic>` to the toctree in `docs/source/index.md`.
4. Run `make html` and reload the browser.

The canonical content lives next to its container, notebooks, and
modules under `lessons/<topic>/`. The `docs/source/lessons/` files are
include-shims so "Edit on GitHub" lands at a clear pointer to the
canonical file.

## Lineage

The course has been taught **seven times** over six years. Each
iteration informed the structure of this site.

| Date | Setting | Platform / Partner |
|------|---------|--------------------|
| Dec 2020 | 5-day course — *the origin* | Jackson Laboratory + Lifebit (co-taught with Christina Chatzipiantzou) |
| Fall 2021 | 3-hour ISCB Academy course | Lifebit |
| Mar 2022 | 3-hour NICHD Scholar course | INCLUDE platform / Seven Bridges CAVATICA |
| Jul 2022 | 1-hour presentation | Univ Colorado — Data Science for Diverse Scholars (Down Syndrome) |
| Aug 2022 | 5-day NICHD Scholar course | Kids First / Seven Bridges CAVATICA |
| Mar 2023 | NICHD Scholar — Kids First + INCLUDE | Velsera |
| 2024 | Federated Data and Learning Fabric | Lifebit |

The pattern of *every container ships a CLI, every Nextflow module
wraps that CLI, every workflow composes the modules* is descended from
the sibling project
[`sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf)
— which itself is the production-grade version of what this site
teaches.

## Acknowledgements

- **Christina Chatzipiantzou** and the **Lifebit** team — origin of
  the course, December 2020.
- The **NICHD Scholar** programmes (Kids First, INCLUDE) for hosting
  the iterations that sharpened the curriculum.
- **Seven Bridges / Velsera** and **CAVATICA** for the platforms that
  let earlier cohorts practise on real data.
- **Anton Wellstein** — PhD mentor; the Sydney Brenner attribution
  comes from him.
