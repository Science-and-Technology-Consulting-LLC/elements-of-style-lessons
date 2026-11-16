# Building reusable command-line tools

> *In the book: Section 5.4, Building Reusable Command-Line Tools.*

This lesson shows you how to turn a script into a command-line tool that explains itself with `--help`, in Python (Typer) and in R (docopt).

## Start here

### Before you start

The previous lesson is [Interactive computing with Jupyter](../interactive-computing/README.md). You also need the `eos` environment from [Reproducible environments with Conda](../conda-environments/README.md).

### Do this

1. **Clone the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/reusable-clis/typer-cli-in-fifteen-minutes.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`, then open the file. You can also [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/reusable-clis/typer-cli-in-fifteen-minutes.ipynb). Run each cell in order, top to bottom.

### What you should see

A small tool that you type by name, such as `hello-py greet --name Annie`, which prints `Hello, Annie!`, and a `--help` screen that lists its commands. The R walkthrough gives you `hello-r` in the same way.

> **Picture to add:** the `hello-py --help` screen in a terminal (save as assets/overview.png)

### Where the files are

- The lesson folder is [`lessons/reusable-clis`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/reusable-clis).
- The notebooks and web pages are in that folder. Each walkthrough exists as a `.ipynb` notebook and a `.md` page with the same steps.
- The tools you build are saved in new folders you create in the walkthroughs: `hello-py-cli` and `hello-r-cli`.

## Steps to execute

1. [A Typer CLI in fifteen minutes](typer-cli-in-fifteen-minutes.md) (notebook: `typer-cli-in-fifteen-minutes.ipynb`)
2. [An Rscript CLI in fifteen minutes](rscript-cli-in-fifteen-minutes.md) (notebook: `rscript-cli-in-fifteen-minutes.ipynb`)

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what a command-line interface is and why the same function is easier to repeat as a command than as a cell in a notebook. Use `greet --name Annie` as the example.
```

**Ask it to build.**

```text
Here is a Python function: <paste function>. Wrap it in a Typer command-line tool with one command, typed options with help text, and a `--help` page that explains each option. Put the logic in the function and keep the command script thin. Show me three example runs and what each prints. (For R: use Rscript and docopt in the same way.)
```

**Ask it to review.**

```text
Review this command-line tool. Check that every option has help text, that it exits with a clear message and a non-zero code when an input is missing, and that the logic is in a function that can be tested without the command line. List problems; do not rewrite.

<paste script>
```


## Further reading

- [Typer](https://typer.tiangolo.com/) and [Click](https://click.palletsprojects.com/), the library Typer is built on
- [Command Line Interface Guidelines](https://clig.dev/)
- [argparse, Python standard library](https://docs.python.org/3/library/argparse.html)
- [docopt for R](https://cran.r-project.org/package=docopt) and [optparse for R](https://cran.r-project.org/package=optparse)

## Supplementary information

A command-line interface (CLI) turns a one-off script into a *tool*. A teammate can run it without reading your code. CI (automatic checks on every push) can run it without anyone watching. Nextflow can run it as a step. An AI agent can run it because `--help` tells the truth.

**The rule: if `--help` lies, the CLI is broken.** Over a career, build a small collection of six or seven tools you reach for again and again.

### What this lesson teaches

1. Write a Typer CLI in 10 lines that produces a real, honest `--help`.
2. Convert a single-purpose script into a CLI with subcommands.
3. Package the CLI so it installs as a real command (`pip install -e .`).
4. Test it the way users will use it.
5. Drop the same CLI into a Nextflow step without changes.

### Why Typer

[Typer](https://typer.tiangolo.com/) is a Python library that turns type-annotated functions into CLIs. The CLI matches the function, `--help` comes from your docstrings and types, and so it cannot drift away from the code. For R, the equivalents are [`optparse`](https://cran.r-project.org/package=optparse) and [`docopt`](https://cran.r-project.org/package=docopt).

### Hello, Typer in 10 lines

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

### Converting a real script

The book companion has a single-purpose script, `scanpy_qc.py`. The exercise is to turn it into `scanpy-qc qc` (and later `convert` and `inspect`). Three things change: `typer.Option(...)` makes every flag self-documenting; the real work moves into importable modules (`.qc`, `.convert`) so a notebook can use it too; and the subcommands split one script into composable verbs.

> **Check:** The text points to `containers/scanpy-qc/scanpy_qc.py` ([link](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/containers/scanpy-qc/scanpy_qc.py)). The repository folder is named `container/` (singular) and holds `scanpy-qc/context`. Which path is correct?

### Packaging, testing and Nextflow

Install the CLI with `pip install -e .` after adding a `[project.scripts]` entry in `pyproject.toml`. Test it with Typer's `CliRunner`, which calls the CLI the way a shell does; two tests (`--help` works, and `qc --help` lists `--min-genes`) catch the commonest breakage, a renamed flag with stale help. In a Nextflow process, call the command directly in the `script:` block, with the container on the `container` line. No extra `bin/` script is needed.

### The agent-readiness payoff

An agent's main interface to your tool is `--help`. Use verbs for subcommands, one-sentence docstrings, a `help=` on every flag with units, and honest boolean names (`--shout / --no-shout`). Then an agent that reaches your tool through an MCP server (see the [MCP server lesson](../mcp-server/README.md)) can call it correctly the first time.

## Next

[Containers](../containers/README.md): put your tool in a single-purpose container.
