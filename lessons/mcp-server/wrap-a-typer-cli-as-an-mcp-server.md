# Wrap a Typer CLI as an MCP server

You will write a short program that lets an AI assistant call your command-line tool. This matters because once a tool speaks the *Model Context Protocol* (MCP), any MCP-aware assistant can use it in plain language.

*Part of the [MCP server](README.md) lesson.*

## Start here

### What you will do

- Make a clean conda environment and install the MCP package.
- Write a small MCP server that offers one *tool*, `greet`.
- Run the server.
- Tell Claude Desktop where the server is, and ask it to greet someone.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson page, [MCP server](README.md), is read.
- The [`hello-py` Typer CLI](../reusable-clis/typer-cli-in-fifteen-minutes.md) from lesson 7.
- A way to write a small text file: any text editor, or JupyterLab's *File, New, Text File*.
- An assistant that understands MCP, such as [Claude Desktop](https://claude.ai/download) or [Claude Code](https://docs.claude.com/en/docs/claude-code), for the last step.
- The notebook is open: `wrap-a-typer-cli-as-an-mcp-server.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb)). Run each cell in order, top to bottom. It uses a Python kernel.

## Steps to execute

### Make a clean environment for this walkthrough (in a terminal)

Why: a clean environment keeps what we add out of our other work. Environments are explained in [creating a conda environment](../conda-environments/creating-a-conda-environment.md). Run these lines in a **terminal**, not in a notebook cell. `conda create` makes the environment, `conda activate` switches to it, and `ipykernel install` lets Jupyter use it.

```bash
conda create -n wrap-a-typer-cli-as-an-mcp-server -y python=3.11 ipykernel
conda activate wrap-a-typer-cli-as-an-mcp-server
python -m ipykernel install --user \
    --name wrap-a-typer-cli-as-an-mcp-server \
    --display-name "Python (wrap-a-typer-cli-as-an-mcp-server)"
```

**What you should see:** conda prints a plan and downloads packages. At the end `ipykernel install` prints `Installed kernelspec wrap-a-typer-cli-as-an-mcp-server`. Your terminal prompt now starts with `(wrap-a-typer-cli-as-an-mcp-server)`. After you restart JupyterLab, the Launcher shows a tile called **Python (wrap-a-typer-cli-as-an-mcp-server)**.

> **Check:** the `ipykernel` kernel installed here has no `mcp`. Which environment should the notebook run in, this one or the one in the next step?

### Check which Python this notebook uses

Why: it is good to know which Python and tools your notebook sees.

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "podman"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```

**What you should see:** the first line shows which Python the notebook uses. The other lines show where `conda`, `pip`, `git` and `podman` live, or `MISSING`. Only the Python line matters here. `MISSING` for `podman` is fine.

### What we build

A minimal MCP server that offers the `greet` verb of the `hello-py` Typer CLI (from [lesson 7](../reusable-clis/typer-cli-in-fifteen-minutes.md)) as an MCP *tool*. [Typer](https://typer.tiangolo.com/) is the Python package behind that CLI. A *tool* is one action an assistant is allowed to call. Once the server runs, any MCP-aware assistant (Claude Desktop, Cursor, the `mcp` command) can call it.

### Install the MCP package (in a terminal)

Why: `mcp` is the official Python package for writing MCP servers, and Typer is the library behind the CLI. Run these lines in a **terminal**, not in a notebook cell:

```bash
conda create -n mcp-demo -y python=3.11
conda activate mcp-demo
pip install "mcp[cli]" typer
```

**What you should see:** conda prints a plan and returns to the prompt, which now starts with `(mcp-demo)`. Then `pip` prints `Successfully installed` with a long list of package names that includes `mcp` and `typer`.

> **Check:** *Make a clean environment for this walkthrough (in a terminal)* and *Install the MCP package (in a terminal)* make two different environments. Please confirm which environment the server should run in. The server only needs the `mcp-demo` one.

### Write the server

Why: the server is a short Python file. `FastMCP("hello-py-mcp")` creates a server with a name. `@mcp.tool()` marks a function as a tool the assistant may call. The text in triple quotes under `def greet` is the tool's description, and the assistant reads it to decide when to use the tool.

Create a new file called `hello_mcp_server.py` in this folder and paste in this code. In JupyterLab, use *File, New, Text File*, paste, then *File, Rename* to give it the name.

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

**What you should see:** a file named `hello_mcp_server.py` in the folder, with those lines. To check, run `ls hello_mcp_server.py` in a terminal.

### Run the server

Why: this shows the file has no mistakes. In your terminal, with `(mcp-demo)` active, run:

```bash
python hello_mcp_server.py
```

The server talks the MCP protocol over *stdio* (the terminal's input and output) by default. It is meant to be started by an assistant, not read by you.

**What you should see:** the terminal prints nothing and does not return to the prompt. That is normal: the server is waiting for a message. Press Ctrl-C to stop it. A Python error message instead means a typo in the file or a missing package (see *If something goes wrong* below).

### Register the server with an assistant (Claude Desktop example)

Why: the assistant has to be told where your server is. For Claude Desktop, edit `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, or the equivalent file on Linux or Windows. Add this, with the real path to your file:

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

An *absolute path* starts at the root of your disk, for example `/Users/you/elements-of-style-lessons/lessons/mcp-server/hello_mcp_server.py`. Run `pwd` in the terminal in this folder to get the start of it.

Restart Claude Desktop. In a new chat, type: *"Use the hello-py MCP tool to greet Annie."*

**What you should see:** Claude asks permission to use the `greet` tool, calls it and replies with `Hello, Annie!`.

> **Picture to add:** the Claude Desktop chat showing the hello-py tool call and the reply "Hello, Annie!" (save as assets/wrap-a-typer-cli-as-an-mcp-server-step-7.png)

> **Check:** `"command": "python"` uses whichever `python` Claude Desktop finds. If that is not the `mcp-demo` environment's Python, the `mcp` package will not be found. Should the config give the full path to the environment's `python`?

### Why this pattern matters

- The tool's description, its parameter names and its docstring *are* the API for the assistant. Good docstrings make usable tools.
- An MCP server can be a thin wrapper around your existing Typer CLI. To keep this example small, `greet` writes the greeting itself. In a real server the tool would call the CLI, so no logic is repeated.
- Every container in this repository can be exposed the same way. See the [`mcp-nsforest-server` container](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/container/mcp-nsforest-server) in this repository.

### If something goes wrong

- **`ModuleNotFoundError: No module named 'mcp'` when you run the server.** The terminal is not using the `mcp-demo` environment. Run `conda activate mcp-demo` and `pip install "mcp[cli]" typer` again.
- **Claude Desktop does not show the tool.** Check the JSON for a missing comma or quote, check that the path to `hello_mcp_server.py` is absolute, and restart Claude Desktop completely (quit, then reopen).
- **`conda: command not found`.** Open a new terminal, as described on the [Introduction page](../introduction/README.md), then try again.

## Next

[Agentic harness](../agentic-harness/README.md): set up the assistant that calls your server. Or return to the [MCP server lesson](README.md), or see [Publishing for agents](../publishing-for-agents/README.md) for the schemas and docs that make tools discoverable.
