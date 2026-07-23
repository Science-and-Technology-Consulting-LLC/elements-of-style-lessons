# A Typer CLI in fifteen minutes

*Companion walkthrough to the [reusable-clis](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — copy each shell block into your terminal; copy each
  Python block into `python -` or your editor.
- **In the paired notebook** [`typer-cli-in-fifteen-minutes.ipynb`](../ipynb/typer-cli-in-fifteen-minutes.ipynb) — every Python
  cell is executed by a dedicated Jupyter **Python 3** kernel. Run the
  shell blocks in a terminal FIRST to create the env and register the
  kernel; then pick that kernel when you open the notebook.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### Once per walkthrough — a dedicated conda env + Jupyter kernel

Isolating the walkthrough in its own env means nothing you install here
leaks out. See [conda-environments](../conda-environments/README.md).

```bash
conda create -n typer-cli-in-fifteen-minutes -y python=3.11 ipykernel
conda activate typer-cli-in-fifteen-minutes
python -m ipykernel install --user \
    --name typer-cli-in-fifteen-minutes \
    --display-name "Python (typer-cli-in-fifteen-minutes)"
```

Lesson-specific `pip install`s appear in the steps below — they land in
this env.

### Every time — verify Python is on your PATH

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "docker"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```


## What we build

A single-file Python CLI, `hello-py`, with two verbs — `greet` and
`version` — using [Typer](https://typer.tiangolo.com). By the end you can
type:

```bash
hello-py greet --name Annie
hello-py --help
```

and get a properly formatted help screen — the same help an MCP agent
will later read.

## Create a project folder

```bash
mkdir hello-py-cli && cd hello-py-cli
```

## Install Typer

```bash
pip install typer[all]
```

## Write the CLI — one file

Create `hello_py/main.py`:

```python
import typer

app = typer.Typer(help="A hello-world CLI to demonstrate Typer.")

@app.command()
def greet(name: str = typer.Option("world", help="Who to greet.")):
    """Print a friendly greeting."""
    typer.echo(f"Hello, {name}!")

@app.command()
def version():
    """Print the version and exit."""
    typer.echo("hello-py 0.1.0")

if __name__ == "__main__":
    app()
```

Run it:

```bash
python -m hello_py.main greet --name Annie
python -m hello_py.main --help
```

## Make it installable — `pyproject.toml`

```toml
[project]
name = "hello-py"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = ["typer[all]"]

[project.scripts]
hello-py = "hello_py.main:app"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

Install in editable mode:

```bash
pip install -e .
```

Now `hello-py greet --name Annie` works from anywhere on your `PATH`.

## Why this shape reappears everywhere

- Every container in this repo ships a CLI in exactly this shape.
- Every Nextflow module wraps exactly one CLI verb.
- Every MCP server exposes each verb as a tool.
- Every AI agent that touches your work reads the `--help` first.

Get this pattern into your fingers and the rest of the curriculum unlocks.

## Where to next

→ Back to the [reusable-clis lesson](README.md).

→ [containers](../containers/README.md) — wrap this CLI in a Docker
image.
