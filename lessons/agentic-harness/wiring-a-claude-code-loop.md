# Wiring a Claude Code loop

You will connect your own tool to Claude Code, an AI coding assistant that runs in your terminal, and watch it use that tool on its own.

*Part of the [Agentic harness](README.md) lesson.*

## Start here

### What you will do

- Install Claude Code.
- Register your MCP server with it using one command.
- Check that the server is registered.
- Start Claude Code and ask it to use your tool.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [MCP server](../mcp-server/README.md), is done. Know the full path to the `hello_mcp_server.py` file you made in [wrap a Typer CLI as an MCP server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md).
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.
- A repository you own, with `gh` signed in, because the last request in *Try the loop* asks Claude to push. See [version control](../version-control/why-git-and-setup.md).

### What we build

A reproducible Claude Code setup that uses one of your own MCP servers as a tool. (Cursor or any MCP-aware client works too.) The book calls this the *agentic harness*.

## Steps to execute

### Install Claude Code and have a server ready

Why: Claude Code is the assistant, and the MCP server is the tool it will call.

1. Install Claude Code by following [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code).
2. Have one MCP server ready. The one from [wrap a Typer CLI as an MCP server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md) is enough.

**What you should see:** in a terminal, `claude --version` prints a version number. If it prints `command not found`, the install did not finish (see *If something goes wrong*).

### Add the MCP server

Why: registering tells Claude Code that a tool called `hello-py` exists, and how to start it. Replace the path with the full path to your server file, then run it **in a terminal** from a project directory (this is a text block, not a notebook cell):

```bash
claude mcp add hello-py python /absolute/path/to/hello_mcp_server.py
```

*Absolute path* means the full path from the root of your disk, for example `/Users/you/elements-of-style-lessons/lessons/mcp-server/hello_mcp_server.py`.

**What you should see:** a short message that the server `hello-py` was added.

### Confirm it registered

Why: it is better to see the server in the list now than to wonder later why Claude cannot find it. This lists every MCP server Claude Code knows.

```bash
claude mcp list
```

**What you should see:** a list that includes a line for `hello-py` and the `python` command with your path. Servers you registered earlier are listed too. If `hello-py` is missing, run *Add the MCP server* again.

### Try the loop

Why: this is the point of the whole walkthrough. Start Claude Code in this directory. Run this **in a terminal, not in a notebook cell**, because it opens a chat that a notebook cannot drive:

```bash
claude
```

Then type this in the chat:

> Use the `hello-py` tool to greet Annie, then commit the greeting to a new file `greetings/annie.txt`, then push.

> **Check:** the last request pushes to a remote. Run Claude in a practice repository you own (for example the `hello-ci` one from [add-a-first-ci-job](../continuous-integration/add-a-first-ci-job.md)), not in the course clone, where you cannot push. Is that the intended setup?

**What you should see:** Claude asks permission to run the `hello-py` tool and calls `greet(name="Annie")`. It then writes the file and runs `git add`, `git commit` and `git push`. That is an agent driving your tools.

> **Picture to add:** the Claude Code chat after the request, showing the greet tool call and the git commands (save as assets/wiring-a-claude-code-loop-step-5.png)

### The harness is the whole point

What we have done is put together four plain parts:

1. Your command-line tools ([Reusable command-line tools](../reusable-clis/README.md)).
2. Wrapped as MCP servers ([MCP server](../mcp-server/README.md)).
3. Registered with a client (this walkthrough).
4. Driven from plain-language chat (the client).

Each part is small and can be tested alone. The "agentic" part comes from putting them together.

### If something goes wrong

- **`claude: command not found`.** Claude Code is not installed, or your terminal does not see it. Follow the [setup page](https://docs.claude.com/en/docs/claude-code/setup), then open a new terminal window. On Windows use *Git Bash*.
- **`hello-py` is not in the list, or shows as failed.** The path in *Add the MCP server* is wrong, or `python` there is not the environment that has the `mcp` package. Check the path with `ls`, and see [wrap a Typer CLI as an MCP server](../mcp-server/wrap-a-typer-cli-as-an-mcp-server.md).
- **Claude says the push failed.** The folder is not a repository you can push to. Use a repository you own, such as the practice one from the [Continuous integration](../continuous-integration/README.md) lesson.

## Next

[Publishing for agents](../publishing-for-agents/README.md): how your tools become discoverable without anyone adding them by hand.
