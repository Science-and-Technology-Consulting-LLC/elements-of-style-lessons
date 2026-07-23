# Wiring a Claude Code loop around your tools

*Companion walkthrough to the [agentic-harness](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`wiring-a-claude-code-loop.ipynb`](wiring-a-claude-code-loop.ipynb) — every code cell
  is a shell command executed by the Jupyter **Bash** kernel.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — register the Bash kernel

Only needed if you'll run the paired notebook in JupyterLab. Skip if
you're doing everything in a terminal.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

Restart JupyterLab; the launcher now shows a **Bash** tile.

### Every time — verify the tools this walkthrough uses

The commands below call one or more of these tools. Where a check
fails, the linked lesson has the install instructions.

| Tool | Check | If missing, see |
|---|---|---|
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/README.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/README.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/README.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/README.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```


## What we build

A minimal, reproducible Claude Code (or Cursor / any MCP-aware client)
setup that uses one of your own MCP servers as a tool — the shape
Chapter 17 calls the *agentic harness*.

## Setup

Install Claude Code (CLI) — see
[docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code).

Have one MCP server ready — the one from
[`mcp-server/walkthroughs/wrap-a-typer-cli-as-an-mcp-server.md`](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md)
is enough.

## Add the MCP server

From a project directory:

```bash
claude mcp add hello-py python /absolute/path/to/hello_mcp_server.py
```

Confirm it registered:

```bash
claude mcp list
```

## Try the loop

Start Claude Code in this directory:

```bash
claude
```

Then in the chat:

> Use the `hello-py` tool to greet Annie, then commit the greeting to
> a new file `greetings/annie.txt`, then push.

Watch: Claude calls `greet(name="Annie")`, writes the file, runs `git
add / commit / push`. The *"agent driving your tools"* loop, in real life.

## The harness is the whole point

An agentic harness isn't magic. It is:

1. Your CLIs — [reusable-clis](../reusable-clis/README.md).
2. Wrapped as MCP servers — [mcp-server](../mcp-server/README.md).
3. Registered with a client — this walkthrough.
4. Driven from natural-language chat — the client.

Every step is small, well-documented, and testable in isolation. The
"agentic" part is emergent.

## Where to next

→ Back to the [agentic-harness lesson](README.md).

→ [publishing-for-agents](../publishing-for-agents/README.md) — how
your tools become discoverable *without* someone adding them by hand.
