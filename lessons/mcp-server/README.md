# MCP server — the agentic AI portion


> *In the book: Chapter 15 — MCP server — the agentic AI portion.*

:::{admonition} What you'll learn
:class: tip

- Wrap any CLI in an MCP server so an AI agent can drive it.
- Register an MCP server with Claude Code on Mac and Windows.
- Run the nsforest-cli + MCP worked example end-to-end.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

This lesson is where everything from the earlier lessons becomes
*agent-callable*. The Model Context Protocol (MCP) is a small,
standardized way to tell an AI agent (Claude, ChatGPT, …) what your tool
can do, what it needs as input, and what it produces as output.

Wrap any of your CLIs with an MCP server and the agent can now drive
that CLI on your behalf in natural language.

:::{admonition} The worked example
:class: tip

The headline worked example is **`nsforest-cli` from the NIH-NLM
`sc-nsforest-qc-nf` workflow, wrapped as an MCP server**, with the
researcher talking to the agent in natural language:

> "Run NSForest on the kidney atlas, organ=kidney, output to my Lifebit
> workspace."

The agent reads the MCP-exposed `--help`, asks any clarifying questions,
and runs the workflow on Lifebit. The researcher never types a Nextflow
command. *That's* the agentic AI portion of the book.

TBD: will extend this lesson this week with how this pattern lands
inside enterprise settings (auth, audit, data-residency).
:::

## What this lesson builds

1. A minimal MCP server in Python that wraps a Typer CLI.
2. The MCP manifest that tells the agent what tools exist.
3. A registration path so Claude Code / Claude.ai / ChatGPT can find
   your server.
4. The end-to-end chat → agent → MCP → CLI → result demo.

## Why this matters

Every CLI you've built in the earlier lessons is, the moment you wrap it
with MCP, **available to an AI agent**. The work doesn't change. The
*reach* of the work multiplies.

## The natural pairing

MCP + [Platforms](platforms.md) (especially Lifebit) is the combination
that delivers on the agentic-AI-for-science promise: agents drive CLIs,
CLIs run on the transport-layer, results come back. See
[Platforms](platforms.md) for the framing.

## The deliverable

A working MCP server that exposes `nsforest-cli` (or any of your topic
CLIs) to Claude Code, with a recorded conversation showing the agent
correctly inferring inputs and running the workflow.

## Register the MCP server with Claude Code

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Claude Code reads ~/.claude/config.json
# Add (or merge) the mcp-nsforest-server entry:
cat ~/.claude/config.json
```
:::

:::{tab-item} Windows
:sync: win

```bash
# Claude Code on Windows reads %USERPROFILE%\.claude\config.json
# Same JSON shape; just the file lives at a Windows path.
cat ~/.claude/config.json
```
:::

:::{tab-item} Lifebit
:sync: lifebit

The Lifebit pattern: the MCP server runs *inside* a Lifebit workspace
exposing nsforest-cli; the agent (Claude / ChatGPT) connects to that
workspace's URL with the appropriate auth. TBD:  enterprise-settings
discussion will land here.*
:::

::::

## Further reading

- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- [Anthropic MCP quickstart](https://modelcontextprotocol.io/quickstart)
- [Official MCP server registry](https://github.com/modelcontextprotocol/servers)
- [Claude Code MCP integration](https://docs.claude.com/en/docs/claude-code/mcp)
- [nsforest-cli](https://github.com/Science-and-Technology-Consulting-LLC/sc-nsforest-qc-nf) — the CLI wrapped in this lesson's example


## Where to next

→ [Agentic harness](agentic-harness.md) — configure the agent that will call your MCP server.
