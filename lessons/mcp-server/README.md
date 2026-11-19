# MCP server: the agentic AI portion

*In the book: Sections 11.5.1 and 11.5.2, The MCP Server; Wrapping a Typer Command-Line Interface as an MCP Server.*

This lesson shows you how to wrap a command-line tool in a small *MCP server* so an AI assistant can call it. The Model Context Protocol (MCP) is a standard way to tell an assistant (Claude, ChatGPT and others) what your tool does, what it needs and what it returns.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Federated learning](../federated-learning/README.md), is done.
- The `hello-py` tool from [A Typer CLI in fifteen minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md) (lesson 7).
- An assistant that understands MCP, such as [Claude Desktop](https://claude.ai/download) or [Claude Code](https://docs.claude.com/en/docs/claude-code), for the last step.

Open `lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb)) and run each cell in order, top to bottom. This notebook uses a Python kernel, and its first section makes a conda environment for it.

### What you should see

We write `hello_mcp_server.py`, run it, and ask an MCP-aware assistant such as Claude Desktop to use the `greet` tool. The assistant replies `Hello, Annie!`.

> **Picture to add:** the assistant's chat showing the greet tool call and its reply (save a screenshot of the finished demo) (save as assets/overview.png)

### Where the files are

- `lessons/mcp-server/wrap-a-typer-cli-as-an-mcp-server.ipynb` and `.md`: the walkthrough.
- `hello_mcp_server.py`: the file you create in the lesson folder.
- `lessons/mcp-server/assets/`: pictures for this lesson.

## Steps to execute

1. [`wrap-a-typer-cli-as-an-mcp-server.md`](wrap-a-typer-cli-as-an-mcp-server.md) — wrap the `greet` command as an MCP tool and call it from an assistant

## Ask an AI assistant

*Optional.* How to use these prompts is explained in [Using the AI prompts](../introduction/README.md).

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

Every tool you built in the earlier lessons becomes available to an AI assistant once you wrap it with MCP. The work does not change, but its reach grows. The [Platforms](../platforms/README.md) lesson shows where such servers run, especially Lifebit.

### The worked example

The headline example is `nsforest-cli` from the NIH-NLM `sc-nsforest-qc-nf` workflow, wrapped as an MCP server, with the researcher talking to the assistant in plain language:

> "Run NSForest on the kidney atlas, organ=kidney, output to my Lifebit workspace."

The assistant reads the MCP-exposed `--help`, asks any clarifying questions and runs the workflow on Lifebit. The researcher never types a Nextflow command.

The deliverable is a working MCP server that exposes `nsforest-cli` (or any of your CLIs) to Claude Code, with a recorded conversation showing the assistant working out the inputs and running the workflow.

### Register the server with Claude Code

On macOS, Claude Code reads `~/.claude/config.json`. Add or merge the `mcp-nsforest-server` entry. On Windows it reads `%USERPROFILE%\.claude\config.json`, with the same JSON shape. To look at the file:

```bash
cat ~/.claude/config.json
```

On Lifebit, the MCP server runs inside a Lifebit workspace and exposes `nsforest-cli`. The assistant connects to that workspace's URL with the right authentication.

> **Check:** the lesson says Claude Code reads `~/.claude/config.json`. The [agentic-harness](../agentic-harness/README.md) walkthrough registers servers with `claude mcp add` instead. Which is right?

## Next

[Agentic harness](../agentic-harness/README.md): set up the assistant that will call your MCP server.
