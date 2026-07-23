# Exposing `--help` and schema — the two things an agent reads first

*Companion walkthrough to the [publishing-for-agents](README.md)
lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — copy each shell block into your terminal; copy each
  Python block into `python -` or your editor.
- **In the paired notebook** [`exposing-help-and-schema.ipynb`](exposing-help-and-schema.ipynb) — every Python
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
conda create -n exposing-help-and-schema -y python=3.11 ipykernel
conda activate exposing-help-and-schema
python -m ipykernel install --user \
    --name exposing-help-and-schema \
    --display-name "Python (exposing-help-and-schema)"
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


## The two artefacts

- **`--help`** — human-readable, discovered by an agent scanning your
  CLI. Typer, `click`, `argparse`, and `docopt` all emit this.
- **A JSON schema of the CLI's inputs** — machine-readable, discovered
  by an agent introspecting an MCP tool declaration.

An agent that has both can *reliably* call your tool. An agent that has
only one has to guess.

## Setup

```bash
conda create -n publish-demo -y python=3.11
conda activate publish-demo
pip install typer typer-slim[standard]
```

## Emit help

Take the `hello-py` CLI from
[`reusable-clis/walkthroughs/typer-cli-in-fifteen-minutes.md`](../reusable-clis/typer-cli-in-fifteen-minutes.md):

```bash
hello-py --help
hello-py greet --help
```

The second line is what an agent actually sees when it decides how to
call `greet`. Every option should have a `help="..."` string — the agent
uses these verbatim.

## Emit a JSON schema

Typer has a `--show-completion` and (as of recent releases) built-in
schema emission. For portable schema generation, wrap the same functions
in Pydantic:

```python
from pydantic import BaseModel, Field
import json

class GreetInput(BaseModel):
    name: str = Field("world", description="Who to greet.")

print(json.dumps(GreetInput.model_json_schema(), indent=2))
```

Save the output as `schemas/greet.schema.json`:

```bash
mkdir -p schemas
python -c "from pydantic import BaseModel, Field; import json
class GreetInput(BaseModel):
    name: str = Field('world', description='Who to greet.')
print(json.dumps(GreetInput.model_json_schema(), indent=2))" > schemas/greet.schema.json
cat schemas/greet.schema.json
```

## Publish the schemas alongside the code

The convention in this repo:

```
container/<name>/context/schemas/<verb>.schema.json
```

CI publishes them under a GitHub Pages route so agents can `GET` them
without cloning the repo.

## Where to next

→ Back to the [publishing-for-agents lesson](README.md).

→ [mcp-server](../mcp-server/README.md) — the MCP protocol that
consumes these schemas as tool declarations.
