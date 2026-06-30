# Introduction

> *In the book: Chapter 1 — Introduction.*

:::{admonition} What you'll learn
:class: tip

- The why behind this curriculum and the lineage it came from.
- The three things this work is trying to grow: literacy, capacity, and skill.
- The good and bad uses of AI tools in this discipline.
- How to navigate the lessons.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*A screenshot will land at `assets/overview.png`. Reference it from
this README as `![overview](assets/overview.png){width=520}` once
captured.*
:::

## Why

A pragmatic, repeatable set of lessons for building biomedical workflows
that promote best practices, in the spirit of Strunk and White's English
grammar book — cleanliness, accuracy, and brevity. Kernighan and Ritchie
applied the same spirit to *The C Programming Language*. Kernighan and
Plauger codified it for code in *The Elements of Programming Style*.

The need is sharper now. In the era of agentic AI, prompt engineering
asks the same things of you that Strunk and White asked: be focused,
clear, intentional. Be brief. Be precise.

When speaking to a computer, one must often remind it that it is
precisely that. A computer. Not capable of reasoning or judgement. You
as the human must maintain that, and now must even be more sure of
your correctness.

## Lineage

This curriculum has been taught seven times:

- Dec 2020 — Jackson Laboratory, 5 days, co-taught with Christina
  Chatzipiantzou and the Lifebit team on the Lifebit Data Analysis
  platform.
- Fall 2021 — ISCB Academy, 3 hours, with the Lifebit team.
- Mar 2022 — NICHD Scholar, 3 hours, INCLUDE platform with Seven
  Bridges CAVATICA.
- Aug 2022 — NICHD Scholar, 5 days, Kids First with Seven Bridges
  CAVATICA.
- Mar 2023 — NICHD Scholar, Kids First and INCLUDE with Velsera.
- 2024 — Lifebit Federated Data and Learning Fabric.

## Literacy, capacity, skill

**Literacy** — the vocabulary, the mental models, the names of the
tools. Reading a Dockerfile, a Nextflow process, a Typer CLI, a
federated workflow, even before writing one.

**Capacity** — the infrastructure that lets you actually run the
work: local terminal, conda env, container runtime, GitHub repo,
platform account. The curriculum lowers this threshold deliberately,
deck by deck.

**Skill** — the doing. Writing the CLI, the module, the workflow.
Wrapping the CLI as an MCP server. Skill compounds; it shows up in
how much science you can do per unit of time.

A fourth — *understanding* — emerges when all three are in place: the
ability to reason about why a pipeline produced what it produced.

## AI tools — good and bad uses

| Good uses of AI | Pitfalls to avoid |
|-----------------|-------------------|
| Learning proper syntax | Letting AI design your architecture |
| Initial code scaffolding | Accepting code without understanding |
| Understanding error messages | No review or testing |
| Creating test data | Overcomplicating simple tasks |
| Documentation generation | Losing design principles |

One must have a simple design idea in one's head — or one will be led
astray. Without clear direction, AI generates code that is hard to
maintain, hard to understand, and unnecessarily complex.

A well-built CLI with an honest `--help`, paired with an MCP server,
is the discipline that turns AI from hazard into collaborator. See
[MCP server](mcp-server.md) and
[Publishing for agents](publishing-for-agents.md).

## How to use the lessons

- In order, for the natural arc.
- Drop in anywhere — each lesson is self-contained.
- Use just the artefacts — every container ships a CLI, every Nextflow
  module wraps that CLI, every workflow composes the modules.

## Where to next

→ [The Rules](elements-of-style-rules.md)
