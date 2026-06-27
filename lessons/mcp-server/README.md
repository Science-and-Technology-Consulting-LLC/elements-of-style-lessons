# MCP server — the agentic AI portion

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

Annie will extend this lesson this week with how this pattern lands
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

## Where to next

→ [Publishing for agents](publishing-for-agents.md)
