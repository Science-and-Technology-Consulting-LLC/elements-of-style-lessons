# Wiring a Claude Code loop

You will connect your own tool to Claude Code, an AI coding assistant that runs in your terminal, and watch it use that tool on its own. This is the *agentic harness*: your command-line tools, wrapped as MCP servers, registered with an assistant you talk to in plain language.

*Part of the [agentic-harness](README.md) lesson.*

## Start here

### What you will do

- Install Claude Code.
- Register your MCP server with it using one command.
- Check that the server is registered.
- Start Claude Code and ask it to use your tool.

### What you need

- [Claude Code](https://docs.claude.com/en/docs/claude-code), installed. See its [setup page](https://docs.claude.com/en/docs/claude-code/setup).
- An MCP server ready to register. The one from [wrap a Typer CLI as an MCP server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md) is enough. Know the full path to its `hello_mcp_server.py` file.
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- [Git](https://git-scm.com/), a repository you own and `gh` signed in, because the last request in *Try the loop* asks Claude to push. See [version-control](../version-control/why-git-and-setup.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`wiring-a-claude-code-loop.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/agentic-harness/wiring-a-claude-code-loop.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

### What we build

A reproducible Claude Code setup (Cursor or any MCP-aware client works too) that uses one of your own MCP servers as a tool. This is the shape Chapter 17 of the book calls the *agentic harness*.

## Steps to execute

### Install Claude Code and have a server ready

Why: Claude Code is the assistant, and the MCP server is the tool it will call.

1. Install Claude Code by following [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code).
2. Have one MCP server ready. The one from [wrap-a-typer-cli-as-an-mcp-server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md) is enough.

**What you should see:** in a terminal, `claude --version` prints a version number. If it prints `command not found`, the install did not finish (see below).

### Add the MCP server

Why: registering tells Claude Code that a tool called `hello-py` exists, and how to start it. Run this from a project directory. Replace the path with the full path to your server file, then run it **in a terminal** (this is a text block, not a notebook cell):

```bash
claude mcp add hello-py python /absolute/path/to/hello_mcp_server.py
```

*Absolute path* means the full path from the root of your disk, for example `/Users/you/elements-of-style-lessons/lessons/mcp-server/hello_mcp_server.py`.

**What you should see:** a short message that the server `hello-py` was added.

### Confirm it registered

Why: it is better to see the server in the list now than to wonder later why Claude cannot find it. The cell below lists every MCP server Claude Code knows.

```bash
claude mcp list
```

**What you should see:** a list that includes a line for `hello-py` and the `python` command with your path. Servers you registered earlier are listed too. If `hello-py` is missing, run *Try the loop* again.

### Try the loop

Why: this is the point of the whole walkthrough. Start Claude Code in this directory. Run this **in a terminal, not in a notebook cell**. It opens an interactive chat that a notebook cannot drive:

```bash
claude
```

Then type this in the chat:

> Use the `hello-py` tool to greet Annie, then commit the greeting to a new file `greetings/annie.txt`, then push.

> **Check:** the last request pushes to a remote. Run Claude in a practice repository you own (for example the `hello-ci` one from [add-a-first-ci-job](../continuous-integration/add-a-first-ci-job.md)), not in the course clone, where you cannot push. Is that the intended setup?

**What you should see:** Claude asks permission to run the `hello-py` tool and calls `greet(name="Annie")`. It then writes the file and runs `git add`, `git commit` and `git push`. That is the "agent driving your tools" loop in real life.

> **Picture to add:** the Claude Code chat after the request, showing the greet tool call and the git commands (save as assets/wiring-a-claude-code-loop-step-5.png)

### The harness is the whole point

An agentic harness is not magic. It is four plain parts:

1. Your CLIs ([reusable-clis](../reusable-clis/README.md)).
2. Wrapped as MCP servers ([mcp-server](../mcp-server/README.md)).
3. Registered with a client (this walkthrough).
4. Driven from plain-language chat (the client).

Each part is small, documented and testable alone. The "agentic" part comes from putting them together.

### If something goes wrong

- **`claude: command not found`.** Claude Code is not installed, or your terminal does not see it. Follow the [setup page](https://docs.claude.com/en/docs/claude-code/setup), then open a new terminal window. On Windows use *Git Bash*.
- **`hello-py` is not in the list, or shows as failed.** The path in *Try the loop* is wrong, or `python` there is not the environment that has the `mcp` package. Check the path with `ls`, and see [wrap-a-typer-cli-as-an-mcp-server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md).
- **Claude says the push failed.** The folder is not a repository you can push to. Use a repository you own, such as the practice one from the [continuous-integration](../continuous-integration/README.md) lesson.

## Next

[Publishing for agents](../publishing-for-agents/README.md): how your tools become discoverable without anyone adding them by hand. Or return to the [agentic-harness lesson](README.md).
