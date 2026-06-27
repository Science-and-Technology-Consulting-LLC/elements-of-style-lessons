# Building reusable command-line tools


> *In the book: Chapter 7 — Building reusable command-line tools.*

:::{admonition} What you'll learn
:class: tip

- Write a Typer CLI in ten lines and a real `--help` for free.
- Convert an existing script into a CLI with subcommands.
- Install the CLI as a console script via `pip install -e .`.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

A command-line interface — a *CLI* — turns a one-off script into a
*tool*. A teammate can run it without reading your code. CI can run it
without anyone watching. Nextflow can run it as a `bin/` step. And —
the headline of this whole curriculum — *an AI agent can run it because
`--help` actually tells the truth.*

:::{admonition} The rule
:class: tip

**If `--help` lies, the CLI is broken.** Every researcher on the team
should accumulate a small compendium of CLIs over their career — six or
seven tools they reach for again and again. This lesson is how you
start building yours.
:::

## What this lesson teaches

By the end you'll be able to:

1. Write a Typer CLI in 10 lines that produces a real, honest `--help`.
2. Convert an existing single-purpose script into a CLI with
   subcommands.
3. Package the CLI so it installs as a real console script (`pip
   install -e .` gives you a command on your PATH).
4. Test it the same way users will use it.
5. Drop the same CLI into a Nextflow `bin/` step without changes.

## Why Typer

[Typer](https://typer.tiangolo.com/) is a modern Python library that
turns type-annotated functions into CLIs. You write a function with
type hints; Typer infers the flags, prints a real `--help`, and
validates the inputs against your types.

A few reasons it beats `argparse` and `click` for our use:

- **The CLI matches the function.** No separate argument-parsing layer
  that drifts out of sync with your code.
- **`--help` is generated from your docstrings and types.** It can't
  lie because it's the same source-of-truth as your code.
- **It composes with FastAPI** if you ever need an HTTP surface for
  the same tool.

For R folks: the equivalents are `optparse` and `docopt`. Same ideas,
slightly different ergonomics.

## Hello, Typer — in 10 lines

```python
# hello.py
import typer

app = typer.Typer(help="A tiny greeting CLI.")

@app.command()
def greet(name: str = "world", shout: bool = False) -> None:
    """Say hello to someone."""
    msg = f"Hello, {name}!"
    typer.echo(msg.upper() if shout else msg)

if __name__ == "__main__":
    app()
```

Run it:

```bash
python hello.py --help
python hello.py greet --help
python hello.py greet --name "your-name"
python hello.py greet --name "your-name" --shout
```

What just happened:

- `app = typer.Typer(...)` creates the CLI application.
- The `@app.command()` decorator turns `greet` into a subcommand.
- The type hints on `name: str` and `shout: bool` become `--name TEXT`
  and `--shout / --no-shout` automatically.
- The docstring `"""Say hello to someone."""` becomes the subcommand's
  help text.

You didn't write *any* argument parsing. The function and the CLI are
the same thing.

## Converting `scanpy_qc.py` — your conversion target

The book companion's
[`containers/scanpy-qc/scanpy_qc.py`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/containers/scanpy-qc/scanpy_qc.py)
is a single-purpose script today. The pedagogical exercise: turn it
into `scanpy-qc qc` (and later, `scanpy-qc convert`, `scanpy-qc
inspect`).

The shape after conversion:

```python
# src/scanpy_qc_cli/main.py
import typer
from pathlib import Path

app = typer.Typer(help="Single-cell QC and h5ad conversion.")

@app.command("qc")
def qc_command(
    input: Path = typer.Option(..., "--input", "-i", help="Raw h5ad to QC."),
    output: Path = typer.Option(..., "--output", "-o", help="Where to write QC'd h5ad."),
    min_genes: int = typer.Option(200, help="Drop cells with fewer than this many genes."),
    min_cells: int = typer.Option(3,   help="Drop genes detected in fewer than this many cells."),
) -> None:
    """Run scanpy QC: drop low-quality cells and lightly filter genes."""
    from .qc import run_qc  # the actual logic lives here, importable from notebooks too
    run_qc(input=input, output=output, min_genes=min_genes, min_cells=min_cells)


@app.command("convert")
def convert_command(
    input: Path = typer.Option(..., "--input", "-i"),
    output: Path = typer.Option(..., "--output", "-o"),
) -> None:
    """Convert a 10x h5 file into a Scanpy h5ad."""
    from .convert import run_convert
    run_convert(input=input, output=output)


if __name__ == "__main__":
    app()
```

Three things changed structurally from the original script:

1. **`typer.Option(...)`** makes every flag self-documenting.
2. **The actual work is in `.qc` / `.convert` modules**, not in the
   command function. That lets you `from scanpy_qc_cli.qc import
   run_qc` from a notebook too.
3. **The subcommands** (`qc`, `convert`) split what was one
   monolithic script into composable verbs.

## Packaging it as an installable command

The CLI lives at `src/scanpy_qc_cli/main.py`. Tell `pyproject.toml`
that it has an entry point:

```toml
[project]
name = "scanpy-qc-cli"
version = "1.0.0"
dependencies = ["typer>=0.9", "scanpy>=1.9", "anndata>=0.10"]

[project.scripts]
scanpy-qc = "scanpy_qc_cli.main:app"

[tool.setuptools.packages.find]
where = ["src"]
```

Install it locally in editable mode:

```bash
pip install -e .

# Now `scanpy-qc` is a real command on your PATH
scanpy-qc --help
scanpy-qc qc --help
scanpy-qc qc --input raw.h5ad --output qc.h5ad
```

`pip install -e .` is one of the most-underrated commands in Python.
It makes your code installable *and* keeps it editable — change
`main.py`, the `scanpy-qc` command picks up the change instantly.

## Testing the CLI the way users use it

Typer ships with a test runner that calls the CLI exactly the way the
shell does:

```python
# tests/test_cli.py
from typer.testing import CliRunner
from scanpy_qc_cli.main import app

runner = CliRunner()

def test_help_does_not_crash():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Single-cell QC" in result.output

def test_qc_subcommand_exists():
    result = runner.invoke(app, ["qc", "--help"])
    assert result.exit_code == 0
    assert "--min-genes" in result.output
```

Those two tests catch the most common breakage: the day someone renames
a flag and forgets to update the help text. CI runs them on every push.

## Dropping the CLI into Nextflow's `bin/`

Once your CLI is on PATH inside the container, a Nextflow process can
call it directly:

```groovy
process SCANPY_QC {
    container "ghcr.io/adeslatt/scanpy-qc-cli:1.0.0"

    input:
    tuple val(sample_id), path(raw)

    output:
    tuple val(sample_id), path("${sample_id}.qc.h5ad")

    script:
    """
    scanpy-qc qc --input ${raw} --output ${sample_id}.qc.h5ad
    """
}
```

No `bin/` script needed. No Python boilerplate. The Nextflow process
just calls your CLI the same way you would from the terminal — and the
same way an AI agent will, in the [MCP server](mcp-server.md) lesson.

## The agent-readiness payoff

The whole reason this lesson is here, before [MCP server](mcp-server.md),
is that **an agent's primary interface to your tool is `--help`.**

When you write good Typer CLIs:

- Subcommands are *verbs* (`qc`, `convert`, `inspect`).
- Each subcommand's docstring is its own *one-sentence summary*.
- Every flag has a `help=` describing what it does and what units it's in.
- Required flags use `typer.Option(..., "--name", "-n", help="...")`.
- Boolean flags have honest names (`--shout / --no-shout`).

Do that and a Claude or ChatGPT instance, given access via MCP, can
invoke your tool correctly *the first time* — without reading your
source.

## What you'll have at the end

A Typer CLI converted from one of your existing scripts, installed as
a real console script via `pip install -e .`, with a test suite that
exercises its `--help`, and a Nextflow process that calls it. From
that point on, the same tool serves humans, CI, Nextflow, and AI
agents — without changes.

## Where to next

→ [MCP server](mcp-server.md) — wrap your CLI as an MCP server and let
an agent drive it.
