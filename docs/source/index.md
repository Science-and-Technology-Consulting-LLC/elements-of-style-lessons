# Elements of Style for Biomedical Workflow Creation in the Era of Agentic AI

:::{admonition} The philosophy
:class: tip

**Clean, Accurate and Brief** The lessons add gentle, practical
tools for immediate use so the practioner becomes immediately capable.
:::

## Audience


## How the lessons fit together

| Position | Lesson | What you take away |
|----------|--------|--------------------|
| Set the stage | [Introduction](lessons/introduction/index.md) | The why |
| Set the stage | [The Rules](lessons/elements-of-style-rules/index.md) | A few Pithy phrases |
| Foundation | [Command line, with Git Bash](lessons/command-line-and-git-bash/index.md) | A terminal that's the same on Mac, Windows, and Lifebit |
| Foundation | [Version control with Git](lessons/version-control/index.md) | A repo your code survives in |
| Foundation | [Reproducible environments with Conda](lessons/conda-environments/index.md) | The clean dry workbench |
| Foundation | [Interactive computing with Jupyter](lessons/interactive-computing/index.md) | Notebooks demystified and a way to work out the specification of your workflow |
| Build | [Building reusable command-line tools](lessons/reusable-clis/index.md) | Typer (Python) + Rscript (R) |
| Build | [Containers](lessons/containers/index.md) | One container, one set of CLIs |
| Build | [Nextflow modules](lessons/nextflow-modules/index.md) | One `.nf` per CLI verb |
| Build | [Nextflow workflows](lessons/nextflow-workflows/index.md) | Compose modules into a pipeline |
| Build | [Differential analysis](lessons/differential-analysis/index.md) | Single cell to pseudobulk, limma-voom |
| Durable | [Documentation](lessons/documentation/index.md) | Sphinx + MyST; this site is the worked example |
| Durable | [Continuous integration](lessons/continuous-integration/index.md) | GitHub Actions guards every commit |
| Scale | [Federated computing](lessons/federated-computing/index.md) | Compute travels to data |
| Scale | [Federated learning](lessons/federated-learning/index.md) | Model parameters travel; data stays put |
| Agent | [MCP server](lessons/mcp-server/index.md) | An AI agent can drive your CLI |
| Agent | [Agentic harness](lessons/agentic-harness/index.md) | Configure the agent to work with your repo |
| Agent | [Publishing for agents](lessons/publishing-for-agents/index.md) | Findable, callable, agent-ready |
| Run | [Platforms](lessons/platforms/index.md) | A transport-layer protocol for science as a service |

## What's special about this site

We want to empower the researcher to have the ability to build their work in a pattern that is amenable to publication.  That is repeatable and reusable.  That is open source and that is clean.  The pattern lends itself to scale and federation.  And it lends itself to being accessible and available to the Agents who we will use to converse with our programs and our data.  This is the *opening of a door* for the era of agentic AI in biomedical
research. 

Every tool taught — the command line, version control,
reproducible environments, well-documented CLIs — is also a tool that
makes the work legible to AI agents like Claude and ChatGPT. The same
habits that make code easy for a collaborator to rerun next year make
it easy for an agent to use it on the researcher's behalf next week.

That connection is made explicit in
[MCP server](lessons/mcp-server/index.md) and
[Publishing for agents](lessons/publishing-for-agents/index.md).

## Working in a constrained environment?

If the platform (e.g., the **All of Us Researcher Workbench**) doesn't
allow direct `git pull`, the work isn't stuck. See
[Bridge patterns](bridges/index.md) for practical, reproducible ways to
keep work versioned even when copy/paste is the only road across.

```{toctree}
:hidden:
:caption: Lessons

lessons/introduction/index
lessons/elements-of-style-rules/index
lessons/command-line-and-git-bash/index
lessons/version-control/index
lessons/git-survival-guide
lessons/conda-environments/index
lessons/interactive-computing/index
lessons/reusable-clis/index
lessons/containers/index
lessons/nextflow-modules/index
lessons/nextflow-workflows/index
lessons/differential-analysis/index
lessons/documentation/index
lessons/continuous-integration/index
lessons/federated-computing/index
lessons/federated-learning/index
lessons/mcp-server/index
lessons/agentic-harness/index
lessons/publishing-for-agents/index
lessons/platforms/index
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
