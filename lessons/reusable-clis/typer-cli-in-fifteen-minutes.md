# A Typer CLI in fifteen minutes

You will build a small command-line tool in Python that prints its own honest help screen, because tools that explain themselves are tools other people (and programs) can use.

**What you will do:**

- Make a clean Python environment for this walkthrough.
- Write a two-command tool, `hello-py`, with [Typer](https://typer.tiangolo.com/).
- Install it so that you can type `hello-py` from any folder.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Interactive computing with Jupyter](../interactive-computing/README.md), is done.
- A terminal. A JupyterLab terminal works: choose *File*, then *New*, then *Terminal*.
- A plain text editor. JupyterLab has one: choose *File*, then *New*, then *Text File*.

You do not need an account for this lesson.

> **Where to type the commands.** The gray command boxes in this lesson run in your **terminal**, not in a notebook cell. The only notebook cell is in *Check that Python is the one you expect*. Keep your terminal open next to this page.

## Steps to execute

### Make a clean environment (once)

*Why:* a conda environment is a private box of programs, as in the [conda environments lesson](../conda-environments/README.md). This one is new, so what we install here cannot break your other work. The last command gives it its own kernel, so you can pick it in JupyterLab.

In your terminal, run:

```bash
conda create -n typer-cli-in-fifteen-minutes -y python=3.11 ipykernel
conda activate typer-cli-in-fifteen-minutes
python -m ipykernel install --user \
    --name typer-cli-in-fifteen-minutes \
    --display-name "Python (typer-cli-in-fifteen-minutes)"
```

Lesson-specific `pip install` commands appear in the steps below. They land in this environment.

**What you should see:** conda prints a list of packages and finishes without an error. After `conda activate`, your prompt starts with `(typer-cli-in-fifteen-minutes)`. The last command prints a line that begins `Installed kernelspec`.

> **Picture to add:** a terminal whose prompt shows `(typer-cli-in-fifteen-minutes)` (save as assets/typer-cli-step-1.png)

### Check that Python is the one you expect

*Why:* if the wrong Python runs your commands, nothing else in this lesson works. The next cell prints where Python lives and whether four other tools are found. `MISSING` for `podman` is fine here; this lesson does not use it.

Run the next cell.

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "podman"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```

**What you should see:** a line for `python` that contains `typer-cli-in-fifteen-minutes` (if your notebook uses the kernel from *Make a clean environment (once)*), then a path or `MISSING` for each other tool.

> **Check:** The notebook cell above runs in whichever kernel the notebook uses. If it prints a path without the environment name, choose *Kernel*, then *Change Kernel*, then *Python (typer-cli-in-fifteen-minutes)*. Please confirm that this is the menu path in your JupyterLab version.

### What we build

A single-file Python tool, `hello-py`, with two commands, `greet` and `version`. By the end you can type:

```bash
hello-py greet --name Annie
hello-py --help
```

and get a properly formatted help screen. This is the same help an AI agent will read later in the [MCP server lesson](../mcp-server/README.md).

### Create a project folder

*Why:* all the files for this tool should live together in one new folder. A **command-line interface** (CLI) is a program you control by typing its name and options.

In your terminal, run:

```bash
mkdir hello-py-cli && cd hello-py-cli
pwd
```

**What you should see:** a path that ends in `hello-py-cli`.

### Install Typer

*Why:* [Typer](https://typer.tiangolo.com/) is the Python library that turns an ordinary function into a command with options and a help screen. `pip` is Python's installer.

```bash
pip install 'typer[all]'
```

The quotes matter on a Mac. Without them the default Mac shell (zsh) stops with `no matches found`.

**What you should see:** pip ends with `Successfully installed` followed by a list that includes `typer`. If pip also warns that Typer does not provide the extra `all`, you can ignore the warning.

### Write the tool

*Why:* this is the whole tool. The function `greet` becomes a command, and the options and help text come from the function itself, so the help cannot drift away from the code. A **decorator** (the line starting with `@`) marks a function as a command.

First make the folder and an empty marker file that tells Python this folder is a package:

```bash
mkdir hello_py
touch hello_py/__init__.py
```

Now create the file `hello_py/main.py` inside `hello-py-cli`. In JupyterLab, use the file browser on the left, open `hello_py`, and choose *New*, then *Text File*, then rename it `main.py`. In a terminal you can use `nano hello_py/main.py`. Paste this:

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

> **Picture to add:** the JupyterLab file browser showing hello_py/main.py open in the editor (save as assets/typer-cli-step-5.png)

### Run it before you install it

*Why:* `python -m hello_py.main` runs the file as a module, so you can test the tool before you package it. Run both commands from inside `hello-py-cli`.

```bash
python -m hello_py.main greet --name Annie
python -m hello_py.main --help
```

**What you should see:** the first command prints `Hello, Annie!`. The second prints a help screen that starts with a `Usage:` line, shows the text `A hello-world CLI to demonstrate Typer.`, and lists two commands, `greet` and `version`.

> **Picture to add:** the terminal showing the `--help` screen with the two commands (save as assets/typer-cli-step-6.png)

### Make it installable

*Why:* the file `pyproject.toml` tells Python the name of your tool, what it needs, and which function starts it. The line under `[project.scripts]` says: make a command called `hello-py` that runs `app` in `hello_py/main.py`.

Create `pyproject.toml` in the `hello-py-cli` folder (next to the `hello_py` folder, not inside it) and paste:

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

Now install it in **editable mode**. That means Python links to your files instead of copying them, so a change to `main.py` takes effect at once.

```bash
pip install -e .
```

The dot means "the folder I am in".

**What you should see:** pip finishes with a line like `Successfully installed hello-py-0.1.0`.

### Use your new command

*Why:* the tool is now a real command on your `PATH`, the list of folders your terminal searches for programs.

```bash
hello-py greet --name Annie
hello-py version
hello-py --help
```

**What you should see:** `Hello, Annie!`, then `hello-py 0.1.0`, then the same help screen as in *Run it before you install it*, now headed by `hello-py` instead of `python -m hello_py.main`. Try it from another folder: it still works.

### Why this shape reappears everywhere

- Every container in this repo ships a CLI in exactly this shape.
- Every Nextflow module wraps exactly one CLI command.
- Every MCP server exposes each command as a tool.
- Every AI agent that touches your work reads the `--help` first.

Get this pattern into your fingers and the rest of the curriculum unlocks.

### If something goes wrong

- **`conda: command not found`.** Close the terminal and open a new one. If it still fails, see the [Introduction page](../introduction/README.md).
- **`zsh: no matches found: typer[all]`.** Put quotes around the name: `pip install 'typer[all]'`.
- **`No module named hello_py`, or `hello-py: command not found`.** You are in the wrong folder, or the environment is not active. Run `pwd` (it must end in `hello-py-cli`), run `conda activate typer-cli-in-fifteen-minutes`, and try again. If `hello-py` is still not found, run `pip install -e .` again.

## Next

Take this tool and put it in a container: [containers](../containers/README.md). Or go back to the [reusable CLIs lesson](README.md).
