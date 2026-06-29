# Elements of Style for Biomedical Workflow Creation in the Era of Agentic AI

A pragmatic, repeatable set of lessons for building biomedical workflows
that promote best practices.  In the spirit of [Strunk and White's English Grammar Book](https://en.wikipedia.org/wiki/The_Elements_of_Style).  White studied writing under Strunk in 1919, he described "the little book" as a "forty-three-page summation of the case for cleanliness, accuracy, and brevity in the use of English".  

Similarly, Kernighan and Ritchie wrote [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language).  In it Brian W. Kernighan and Dennis M. Ritchie embraced the spirit of that book in the execution of their book covering the core elements of programming style in C.  With keen focus on clarity, simplicity, maintainability, and predictable execution, closely aligning with the classic design philosophy pioneered by Brian Kernighan and P.J. Plauger in [The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style). 

The need for cleanliness, accuracy and brevity are even more important now in our Era of Agentic AI.  In [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) you must be very focused, clear and intentional about the desired outcomes.  Doing all of this in such a way that you can find your work again, being kind to your future self, is the focus of this work.  Clarity in an environment where many do not have English as their primary language, it calls for even more brevity, to avoid confusion, more clarity, to ensure precision and absolute accuracy.  

When speaking to a computer, one must often remind it that it is precisely that.  A computer.  Not capable of reasoning or judgement.  You as the human must maintain that, and now must even be more sure of your correctness.

:::{admonition} The philosophy
:class: tip

**Clean, Accurate and Brief** The lessons add gentle, practical
tools for immediate use so the practioner becomes immediately capable.
:::

## Dry Workbench

We must think of our work on the computer, the scratching of the pen to paper so to speak, as similar to the biologists' wet bench.  The area must be kept clean, free of contaminents.  The researcher must be sure the experiment being run is repeatable.  

The outcome must be indeed the outcome you planned and that anyone can repeat and achieve the same.   

- Each step must be clear.
- Each environment clear.
- We do not reinvent the wheel.  We can explicitly use the work of others.
- Find that working code.
- Add, if required, command line interfaces so each step is clear.
- Assemble the steps into a repeatable standard operating proceedure, a SOP.
- Test and iterate.
- Automate and store.

Each step clear, brief, clean and accurate.  Understanding this philosphically first will help the reader on their way.

## Audience

- Everyone.  From the working scientists at any career stage — from summer
  researchers in their first terminal session to PIs already shipping
  Nextflow pipelines.  From the wet-bench scientist needing now to have full control of their research and stepping into the fray for the first time.  These lessons will help you make very professional, very flexible, very reusable components that capture your steps in a repeatable manner.

- Anyone whose work has to live somewhere other than a laptop — on the
  All of Us Researcher Workbench, in CAVATICA, on Biowulf, in
  containers, or as a Nextflow pipeline someone else can rerun next
  year.

  Nextflow is one of many workflow languages, in the opinion of this author, for our field of biomedical research, it is the best workflow language.  Written in Groovy it is a Domain Specific language which understands our filetypes.  Important when looking for best practices in their approach to solving a problem.
  

If you're moving between Windows, macOS, and remote Linux environments
and the terminal feels different every time you sit down, you're in
the right place.

## How the lessons fit together

| Position | Lesson | What you take away |
|----------|--------|--------------------|
| Set the stage | [Introduction](lessons/introduction.md) | The why |
| Set the stage | [The Rules](lessons/elements-of-style-rules.md) | A few Pithy phrases |
| Foundation | [Command line, with Git Bash](lessons/command-line-and-git-bash.md) | A terminal that's the same on Mac, Windows, and Lifebit |
| Foundation | [Version control with Git](lessons/version-control.md) | A repo your code survives in |
| Foundation | [Reproducible environments with Conda](lessons/conda-environments.md) | The clean dry workbench |
| Foundation | [Interactive computing with Jupyter](lessons/interactive-computing.md) | Notebooks demystified and a way to work out the specification of your workflow |
| Build | [Building reusable command-line tools](lessons/reusable-clis.md) | Typer (Python) + Rscript (R) |
| Build | [Containers](lessons/containers.md) | One container, one set of CLIs |
| Build | [Nextflow modules](lessons/nextflow-modules.md) | One `.nf` per CLI verb |
| Build | [Nextflow workflows](lessons/nextflow-workflows.md) | Compose modules into a pipeline |
| Scale | [Federated computing](lessons/federated-computing.md) | Compute travels to data |
| Scale | [Federated learning](lessons/federated-learning.md) | Model parameters travel; data stays put |
| Agent | [MCP server](lessons/mcp-server.md) | An AI agent can drive your CLI |
| Agent | [Publishing for agents](lessons/publishing-for-agents.md) | Findable, callable, agent-ready |
| Run | [Platforms](lessons/platforms.md) | A transport-layer protocol for science as a service |

## What's special about this site

We want to empower the researcher to have the ability to build their work in a pattern that is amenable to publication.  That is repeatable and reusable.  That is open source and that is clean.  The pattern lends itself to scale and federation.  And it lends itself to being accessible and available to the Agents who we will use to converse with our programs and our data.  This is the *opening of a door* for the era of agentic AI in biomedical
research. 

Every tool taught — the command line, version control,
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
