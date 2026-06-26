# Elements of Style in Biomedical Workflow Creation in the Era of Agentic AI

*A companion training site for the NLM-CKN intramural team.*

Welcome. This site is here to help you — whether you joined last week as a summer
researcher or have been writing biomedical pipelines for a decade — work a little
more confidently with the tools that make modern biomedical research reproducible,
shareable, and ready for the AI agents that are quickly becoming our collaborators.

:::{admonition} Our philosophy
:class: tip

**Educate without disrupting.** Your director, your platform, and your deadlines
already shape how you work. We're not here to change any of that. We're here to
add gentle, practical tools you can reach for *when the opportunity arises* — so
that the right thing becomes a little easier each time.
:::

## Who this is for

- **NLM-CKN team members** at any career stage.
- **Summer researchers** with short timeframes and big ambitions.
- Anyone whose work has to live somewhere other than a laptop — on the
  All of Us Researcher Workbench, in CAVATICA, on Biowulf, in containers,
  or as a Nextflow pipeline someone else can rerun next year.

If you're moving between Windows, macOS, and remote Linux environments and the
terminal feels different every time you sit down, you're in the right place.

## Two ways to use this site

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 🧭 Follow the lessons
:link: lessons/index
:link-type: doc

A structured set of lessons from the command line to publishing AI-agent-ready
tools. Each lesson assumes you've done the one before, but you can drop in
anywhere.
:::

:::{grid-item-card} 📚 Jump into a book chapter
:link: chapters/index
:link-type: doc

Real worked examples from Anne's Springer book
*Elements of Style in Creating Workflows for Biomedical Research.*
Bulk RNA-seq, single-cell, the lot — running code, not just slides.
:::

::::

## What's special about this site

This site is the *opening of a door* for the era of agentic AI in biomedical
research. Every tool we teach — the command line, version control,
reproducible environments, well-documented CLIs — is also a tool that makes
your work legible to AI agents like Claude and ChatGPT. The same habits that
make code easy for your collaborator to rerun next year make it easy for an
agent to use it on your behalf next week.

We call out that connection where it matters, in
[Publishing for agents](lessons/publishing-for-agents.md) and made it
the headline of [MCP server](lessons/mcp-server.md).

## Working in a constrained environment?

If your platform (e.g., the **All of Us Researcher Workbench**) doesn't let you
`git pull` directly, you're not stuck. See
[Bridge patterns](bridges/index.md) for practical, reproducible ways to keep your
work versioned even when copy/paste is the only road across.

```{toctree}
:hidden:
:caption: Lessons

lessons/index
```

```{toctree}
:hidden:
:caption: Bridge patterns

bridges/index
```

```{toctree}
:hidden:
:caption: Book chapters (reference)

chapters/index
```

```{toctree}
:hidden:
:caption: About

about/audience
about/how-this-site-was-made
```
