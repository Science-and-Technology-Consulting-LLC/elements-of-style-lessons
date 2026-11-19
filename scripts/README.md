# scripts/

Helper utilities used during teaching and CI: data fixture generators,
small renderers, the kind of one-off shell tools every workflow repo
accumulates. Mirrors the `scripts/` directory pattern in
[`NIH-NLM/sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf).

## check-images.py

Checks every picture link in `lessons/` and `case-studies/` (the `.md` files and
the Markdown cells of the notebooks). Run it from the repository folder before
you push:

```bash
python scripts/check-images.py
```

Write a picture as `![What it shows](assets/name.png)`, with the file in the
lesson's own `assets` folder. That path works on GitHub, in JupyterLab and on the
Sphinx site. The script reports a missing file, a link to a GitHub page instead
of a picture, and a broken `![...]( )` line. Add `--online` to also fetch web
addresses. It counts the "Picture to add" notes that still wait for a picture.

## sync-notebooks.py

Each lesson page (`.md`) has a notebook twin (`.ipynb`). Edit the page, then run:

```bash
python scripts/sync-notebooks.py
```

The notebook is rebuilt from the page. Its code cells are kept exactly as they are, and only
the text between them changes. Add `--check` to see problems without writing anything. To change
a command, change it in the page and in the notebook cell the same way; the script stops with an
error if it cannot find a code cell in the page. Run `python scripts/check-images.py` after it.
