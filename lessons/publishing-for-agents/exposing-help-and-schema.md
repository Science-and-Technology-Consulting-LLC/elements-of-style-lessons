# Exposing help and schema

You will make a command-line tool describe itself in two ways: a `--help` page for people and a JSON schema for programs. This matters because an AI agent can call your tool reliably only if it can read exactly what the tool accepts.

*Part of the [publishing-for-agents](README.md) lesson.*

## What you will do

- Make a clean conda environment with Typer installed.
- Read the `--help` pages of the `hello-py` command.
- Write a JSON schema for the `greet` input with Pydantic.
- Save the schema in a `schemas/` folder.

## What you need

- [conda](https://docs.conda.io/) and a terminal. See [creating a conda environment](../conda-environments/creating-a-conda-environment.md) and [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- The `hello-py` command from [typer-cli-in-fifteen-minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md), installed in your environment. [Typer](https://typer.tiangolo.com/) is a Python package for making command-line tools.
- [Pydantic](https://docs.pydantic.dev/), a Python package that describes data and writes [JSON Schema](https://json-schema.org/) for it (step 6 shows how to install it).
- [JupyterLab](https://jupyter.org/) with a Python kernel, if you want to read this as a notebook.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`exposing-help-and-schema.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/publishing-for-agents/exposing-help-and-schema.ipynb) and run each cell in order, top to bottom.

## Step 1. Make a clean environment for this walkthrough (in a terminal)

Why: a *conda environment* is a private folder of programs. Installing here keeps everything you add out of your other work. See [creating a conda environment](../conda-environments/creating-a-conda-environment.md). Run these lines in a **terminal**, not in a notebook cell. `conda create` makes the environment, `conda activate` switches to it, and `ipykernel install` lets Jupyter use it.

```bash
conda create -n exposing-help-and-schema -y python=3.11 ipykernel
conda activate exposing-help-and-schema
python -m ipykernel install --user \
    --name exposing-help-and-schema \
    --display-name "Python (exposing-help-and-schema)"
```

**What you should see:** conda prints a plan and downloads packages. At the end `ipykernel install` prints `Installed kernelspec exposing-help-and-schema`. Your terminal prompt now starts with `(exposing-help-and-schema)`. After you restart JupyterLab, the Launcher shows a tile called **Python (exposing-help-and-schema)**.

> **Check:** the `ipykernel` kernel installed here has no `typer`. Which environment should the notebook run in, this one or the one in the next step?

## Step 2. Check which Python this notebook uses

Why: the walkthrough runs its commands in a terminal, but it is good to know which Python and tools your notebook sees.

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "docker"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```

**What you should see:** the first line shows which Python the notebook uses. The other lines show where `conda`, `pip`, `git` and `docker` live, or `MISSING`. For this walkthrough only the Python line matters. `MISSING` for `docker` is fine.

## Step 3. The two descriptions

Why: an agent needs two things from your tool.

- **`--help`** is a page of text for people, and for an agent that scans your command. Typer, `click`, `argparse` and `docopt` all produce it.
- **A JSON schema of the tool's inputs** is a file for programs. An agent that reads a tool's declaration (for example an MCP tool) uses it to build a correct call.

An agent that has both can call your tool reliably. An agent that has only one has to guess.

## Step 4. Set up an environment (in a terminal)

Why: a clean environment keeps these packages away from your other work. Run these lines in a **terminal**, not in a notebook cell:

```bash
conda create -n publish-demo -y python=3.11
conda activate publish-demo
pip install typer typer-slim[standard]
```

**What you should see:** conda prints a plan and returns to the prompt, which now starts with `(publish-demo)`. `pip` ends with `Successfully installed` and a list of packages that includes `typer`.

> **Check:** step 1 and step 4 make two different environments. Please confirm which one to use. Also, `pip install typer typer-slim[standard]` installs two Typer packages. Is one of them meant to be left out?

## Step 5. Show the `--help` pages

Why: this is what an agent sees first. Use the `hello-py` command from [typer-cli-in-fifteen-minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md). It must be installed in the active environment. Run these lines in a **terminal**:

```bash
hello-py --help
hello-py greet --help
```

**What you should see:** the first command lists the tool's commands, with `greet` among them. The second shows the usage line, the options of `greet` and a one-line help text for each. The second page is what an agent actually reads when it decides how to call `greet`. Every option should have a `help="..."` string, because the agent uses them word for word.

## Step 6. Write a JSON schema

Why: `--help` is for reading. A *JSON schema* is the same information in a form a program can check.

> **Check:** the lesson says Typer has built-in schema emission in recent releases. Is that correct, and from which Typer version?

For a portable schema, describe the same inputs with Pydantic. Install it first, in the terminal:

```bash
pip install pydantic
```

> **Check:** the `pip install` line in step 4 does not install Pydantic. Should `pydantic` be added to that line?

Then this code prints the schema (you can run it in a notebook cell or save it in a file):

```python
from pydantic import BaseModel, Field
import json

class GreetInput(BaseModel):
    name: str = Field("world", description="Who to greet.")

print(json.dumps(GreetInput.model_json_schema(), indent=2))
```

**What you should see:** a block of JSON that lists one property, `name`, with the description `Who to greet.` and the default `world`. It looks like this:

```json
{
  "properties": {
    "name": {
      "default": "world",
      "description": "Who to greet.",
      "title": "Name",
      "type": "string"
    }
  },
  "title": "GreetInput",
  "type": "object"
}
```

## Step 7. Save the schema in a file

Why: an agent reads a file, not your terminal. This saves the same schema as `schemas/greet.schema.json` and prints it back. Run it in a **terminal**:

```bash
mkdir -p schemas
python -c "from pydantic import BaseModel, Field; import json
class GreetInput(BaseModel):
    name: str = Field('world', description='Who to greet.')
print(json.dumps(GreetInput.model_json_schema(), indent=2))" > schemas/greet.schema.json
cat schemas/greet.schema.json
```

**What you should see:** the same JSON as in step 6, printed by `cat`.

## Step 8. Publish the schemas next to the code

The convention in this repository is:

```text
container/<name>/context/schemas/<verb>.schema.json
```

CI publishes the files under a GitHub Pages route, so agents can fetch them without cloning the repository. See [continuous-integration](../continuous-integration/README.md).

## If something goes wrong

- **`hello-py: command not found`.** The `hello-py` command is not installed in this environment. Do [typer-cli-in-fifteen-minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md) first, in the same environment.
- **`ModuleNotFoundError: No module named 'pydantic'`.** Run `pip install pydantic` in the active environment (see step 6) and try again.
- **The schema file is empty or `python -c` complains about quotes.** On Windows use *Git Bash*, not PowerShell. Check that the three lines after `python -c "...` are copied exactly, with the closing quote.

## Next

[MCP server](../mcp-server/README.md): the protocol that uses these schemas as tool declarations. Or return to the [publishing-for-agents lesson](README.md).
