# Elements of Style in Creating Workflows for Biomedical Research in the Era of Agentic AI

A pragmatic, repeatable set of lessons for building biomedical workflows
that survive — collaborators, future-self readers, and the AI agents
that are quickly becoming part of the team.

:::{admonition} The philosophy
:class: tip

**Educate without disrupting.** The lessons add gentle, practical
tools you can reach for *when the opportunity arises* — so that the
right thing becomes a little easier each time.
:::

## Who this is for

- Working biomedical scientists at any career stage — from summer
  researchers in their first terminal session to PIs already shipping
  Nextflow pipelines.
- Anyone whose work has to live somewhere other than a laptop — on the
  All of Us Researcher Workbench, in CAVATICA, on Biowulf, in
  containers, or as a Nextflow pipeline someone else can rerun next
  year.

If you're moving between Windows, macOS, and remote Linux environments
and the terminal feels different every time you sit down, you're in
the right place.

## How the lessons fit together

| Position | Lesson | What you take away |
|----------|--------|--------------------|
| Set the stage | [Introduction](lessons/introduction.md) | The why |
| Set the stage | [The Rules](lessons/elements-of-style-rules.md) | Pithy phrases that summarise the discipline |
| Foundation | [Command line, with Git Bash](lessons/command-line-and-git-bash.md) | A terminal that's the same on Mac, Windows, and Lifebit |
| Foundation | [Version control with Git](lessons/version-control.md) | A repo your code survives in |
| Foundation | [Reproducible environments with Conda](lessons/conda-environments.md) | An env you (and a collaborator) can recreate |
| Foundation | [Interactive computing with Jupyter](lessons/interactive-computing.md) | Notebooks demystified |
| Build | [Building reusable command-line tools](lessons/reusable-clis.md) | Typer (Python) + Rscript (R) |
| Build | [Containers](lessons/containers.md) | One container, one job, one CLI |
| Build | [Nextflow modules](lessons/nextflow-modules.md) | One `.nf` per CLI verb |
| Build | [Nextflow workflows](lessons/nextflow-workflows.md) | Compose modules into a pipeline |
| Scale | [Federated computing](lessons/federated-computing.md) | Compute travels to data |
| Scale | [Federated learning](lessons/federated-learning.md) | Model parameters travel; data stays put |
| Agent | [MCP server](lessons/mcp-server.md) | An AI agent can drive your CLI |
| Agent | [Publishing for agents](lessons/publishing-for-agents.md) | Findable, callable, agent-ready |
| Run | [Platforms](lessons/platforms.md) | A transport-layer protocol for science as a service |

## What's special about this site

This is the *opening of a door* for the era of agentic AI in biomedical
research. Every tool taught — the command line, version control,
reproducible environments, well-documented CLIs — is also a tool that
makes the work legible to AI agents like Claude and ChatGPT. The same
habits that make code easy for a collaborator to rerun next year make
it easy for an agent to use it on the researcher's behalf next week.

That connection is made explicit in
[MCP server](lessons/mcp-server.md) and
[Publishing for agents](lessons/publishing-for-agents.md).

## Working in a constrained environment?

If the platform (e.g., the **All of Us Researcher Workbench**) doesn't
allow direct `git pull`, the work isn't stuck. See
[Bridge patterns](bridges/index.md) for practical, reproducible ways to
keep work versioned even when copy/paste is the only road across.

```{toctree}
:hidden:
:caption: Lessons

lessons/introduction
lessons/elements-of-style-rules
lessons/command-line-and-git-bash
lessons/version-control
lessons/git-survival-guide
lessons/conda-environments
lessons/interactive-computing
lessons/reusable-clis
lessons/containers
lessons/nextflow-modules
lessons/nextflow-workflows
lessons/federated-computing
lessons/federated-learning
lessons/mcp-server
lessons/publishing-for-agents
lessons/platforms
```

```{toctree}
:hidden:
:caption: Bridge patterns

bridges/index
```

```{toctree}
:hidden:
:caption: Book chapter mapping

chapters/index
```

```{toctree}
:hidden:
:caption: About

about/audience
about/how-this-site-was-made
```
