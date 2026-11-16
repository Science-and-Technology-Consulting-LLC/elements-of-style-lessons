# MCP server: the agentic AI portion

*In the book: Sections 11.5.1 and 11.5.2, The MCP Server; Wrapping a Typer Command-Line Interface as an MCP Server.*

This lesson shows you how to wrap a command-line tool in a small *MCP server* so an AI assistant can call it. The Model Context Protocol (MCP) is a standard way to tell an assistant (Claude, ChatGPT and others) what your tool does, what it needs and what it returns.

## Start here

### Before you start

The previous lesson is [Federated learning](../federated-learning/README.md). You also need the `hello-py` tool from [A Typer CLI in fifteen minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md).

### Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb)) and run each cell in order, top to bottom. This notebook uses a Python kernel. Its first section makes a conda environment.

### What you should see

You write `hello_mcp_server.py`, run it, and ask an MCP-aware assistant such as Claude Desktop to use the `greet` tool. The assistant replies `Hello, Annie!`.

> **Picture to add:** the assistant's chat showing the greet tool call and its reply (save a screenshot of the finished demo) (save as assets/overview.png)

### Where the files are

- `lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb` and `.md`: the walkthrough.
- `hello_mcp_server.py`: the file you create in the lesson folder.
- `lessons/mcp-server/assets/`: pictures for this lesson.

## Steps to execute

1. [`wrap-a-typer-cli-as-an-mcp-server.md`](wrap-a-typer-cli-as-an-mcp-server.md) — wrap the `greet` command as an MCP tool and call it from an assistant

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what the Model Context Protocol is, what a tool is, and what happens between my question to an assistant and the answer from my program. Keep it to ten lines.
```

**Ask it to build.**

```text
Here is a Python command-line function: <paste function>. Wrap it as a tool in a Model Context Protocol server using the official Python SDK, with typed arguments and a clear description for each. Tell me the exact steps to register it with <my assistant> and what to type to test it.
```

**Ask it to review.**

```text
Review this MCP server. Check that each tool has a clear name and description, typed inputs, and a useful error message, and that no tool can delete or overwrite files without being asked. List problems.

<paste server>
```


## Further reading

- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- [MCP quickstart](https://modelcontextprotocol.io/quickstart)
- [Official MCP server registry](https://github.com/modelcontextprotocol/servers)
- [Claude Code MCP integration](https://docs.claude.com/en/docs/claude-code/mcp)
- [nsforest-cli](https://github.com/NIH-NLM/sc-nsforest-qc-nf): the CLI wrapped in this lesson's example

## Supplementary information

Every tool you built in the earlier lessons becomes available to an AI assistant once you wrap it with MCP. The work does not change. Its reach grows.

### The worked example

The headline example is `nsforest-cli` from the NIH-NLM `sc-nsforest-qc-nf` workflow, wrapped as an MCP server, with the researcher talking to the assistant in plain language:

> "Run NSForest on the kidney atlas, organ=kidney, output to my Lifebit workspace."

The assistant reads the MCP-exposed `--help`, asks any clarifying questions and runs the workflow on Lifebit. The researcher never types a Nextflow command.

### What this lesson builds

1. A minimal MCP server in Python that wraps a Typer CLI.
2. The MCP manifest that tells the assistant what tools exist.
3. A way to register it so Claude Code, Claude.ai or ChatGPT can find it.
4. The end-to-end flow: chat, assistant, MCP, CLI, result.

The deliverable is a working MCP server that exposes `nsforest-cli` (or any of your CLIs) to Claude Code, with a recorded conversation showing the assistant working out the inputs and running the workflow.

### Pairs well with

MCP plus [Platforms](../platforms/README.md) (especially Lifebit): assistants drive CLIs, CLIs run on the transport layer, results come back.

### Register the server with Claude Code

On macOS, Claude Code reads `~/.claude/config.json`. Add or merge the `mcp-nsforest-server` entry. On Windows it reads `%USERPROFILE%\.claude\config.json`, with the same JSON shape. To look at the file:

```bash
cat ~/.claude/config.json
```

On Lifebit, the MCP server runs inside a Lifebit workspace and exposes `nsforest-cli`. The assistant connects to that workspace's URL with the right authentication.

> **Check:** the lesson says Claude Code reads `~/.claude/config.json`. The [agentic-harness](../agentic-harness/README.md) walkthrough registers servers with `claude mcp add` instead. Which is right?

## Next

[Agentic harness](../agentic-harness/README.md): set up the assistant that will call your MCP server.
