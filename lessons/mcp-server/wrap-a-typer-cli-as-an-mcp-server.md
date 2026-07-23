# Wrap a Typer CLI as an MCP server

*Companion walkthrough to the [mcp-server](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — copy each shell block into your terminal; copy each
  Python block into `python -` or your editor.
- **In the paired notebook** [`wrap-a-typer-cli-as-an-mcp-server.ipynb`](wrap-a-typer-cli-as-an-mcp-server.ipynb) — every Python
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
conda create -n wrap-a-typer-cli-as-an-mcp-server -y python=3.11 ipykernel
conda activate wrap-a-typer-cli-as-an-mcp-server
python -m ipykernel install --user \
    --name wrap-a-typer-cli-as-an-mcp-server \
    --display-name "Python (wrap-a-typer-cli-as-an-mcp-server)"
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

A minimal MCP server that exposes the `greet` verb of the `hello-py`
Typer CLI (from
[`reusable-clis/walkthroughs/typer-cli-in-fifteen-minutes.md`](../reusable-clis/typer-cli-in-fifteen-minutes.md))
as an MCP *tool*. Once running, any MCP-aware agent (Claude Desktop,
Cursor, `mcp` CLI) can call it.

## Setup

```bash
conda create -n mcp-demo -y python=3.11
conda activate mcp-demo
pip install "mcp[cli]" typer
```

## Write the server

Create `hello_mcp_server.py`:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-py-mcp")

@mcp.tool()
def greet(name: str = "world") -> str:
    """Return a friendly greeting for `name`."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

## Run it

```bash
python hello_mcp_server.py
```

The server speaks the MCP protocol over stdio by default; leave it
running.

## Register it with an agent — Claude Desktop example

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS) or the equivalent on Linux / Windows:

```json
{
  "mcpServers": {
    "hello-py": {
      "command": "python",
      "args": ["/absolute/path/to/hello_mcp_server.py"]
    }
  }
}
```

Restart Claude Desktop. In a new chat, type: *"Use the hello-py MCP
tool to greet Annie."* The agent finds the `greet` tool, calls it,
returns `"Hello, Annie!"`.

## Why this pattern matters

- The tool description, the parameter names, and the docstring **are
  the API** for the agent. Well-written docstrings = usable tools.
- The MCP server is a *thin* wrapper around your existing Typer CLI —
  no duplication of logic.
- Every container in this repo can be exposed the same way — see the
  `mcp-nsforest-server` container in [containers](../containers/README.md).

## Where to next

→ Back to the [mcp-server lesson](README.md).

→ [publishing-for-agents](../publishing-for-agents/README.md) — the
schemas + docs that make your tools discoverable.
