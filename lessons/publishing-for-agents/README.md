# Publishing for agents


> *In the book: Chapter 14 — Publishing for agents.*

:::{admonition} What you'll learn
:class: tip

- The ten-item agent-ready checklist (and what each item buys you).
- Write a README an agent can act on, not just read.
- Tag a SemVer release and publish under NIH-NLM / Scitechcon-LLC conventions.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

This is where the discipline of every earlier lesson pays off. The
lessons up to this point are about making your work **runnable** — by
you, by a teammate, by CI, by Nextflow. This lesson is about making
your work **findable and usable by AI agents** — Claude, ChatGPT, and
the generation that's already coming.

:::{admonition} The headline
:class: tip

A well-documented CLI is an API for AI agents. An MCP server is the
politest introduction your tool can make.

If you've been doing the lessons in order, every habit you've already
formed contributes:

- A repo on **GitHub** is an address an agent can read.
- A pinned **conda env** lets an agent reproduce your setup.
- A clean **notebook** tells the agent what the analysis does.
- A **Nextflow module** gives the agent a known I/O contract.
- A **Typer CLI** lets the agent invoke a step without reading the
  source — `--help` is the API.

This lesson is the checklist that turns those individual habits into a
published, agent-ready tool.
:::

## What this lesson teaches

By the end you'll be able to:

1. Take one of your CLIs and publish it as an agent-ready package.
2. Write a README that an agent can act on — not just a human.
3. Tag a release that downstream agents can pin against.
4. Hand the resulting package to the [MCP server](mcp-server.md) lesson
   for the agent-driving demo.

## The agent-ready checklist

When you're about to publish a tool, walk this list. It's the same
list a thoughtful agent will (implicitly) walk when it discovers your
tool.

1. **GitHub repo at a stable URL.** Ideally under an organisation
   (your lab, your school, your company) rather than a personal account.
2. **README starts with one sentence that names the inputs and outputs.**
   Not "this is a tool for..." but "this tool takes X and produces Y."
   An agent's first scan is for I/O shape.
3. **`environment.yml`** that pins every dependency. An agent has to
   reproduce your environment to call your tool.
4. **A single entry-point CLI** (`pyproject.toml` `[project.scripts]`
   entry), so `pip install` produces a real command. See
   [Reusable CLIs](reusable-clis.md).
5. **`--help` that doesn't lie.** Every subcommand, every flag, every
   default — accurate and self-explanatory.
6. **At least one test that the CI runs on every push.** The test
   should exercise the CLI the way users (and agents) will.
7. **A licence file.** Without one, in many legal regimes nobody is
   allowed to use your tool. MIT or BSD-3-Clause are reasonable
   defaults for academic work.
8. **A tagged release** with semantic versioning (`v1.0.0`). An agent
   that finds your tool a year from now should be able to pin to a
   specific version that still works.
9. **A `Dockerfile` or `Containerfile`** (see
   [Containers](containers.md)) that runs the CLI. Many agents will
   prefer to invoke through a container than to install dependencies.
10. **Optional but powerful: an MCP server manifest** that exposes the
    CLI's subcommands as MCP tools. See [MCP server](mcp-server.md)
    for the worked example.

If you can answer "yes" to 1–9, your tool is agent-ready *before* you
even write the MCP server.

## Writing a README an agent can act on

The single most-leveraged thing you can do is write a README that's
structured rather than free-text. Agents do well with predictable
shape; humans do too.

A template that works:

```markdown
# my-tool

> One sentence: my-tool takes X (file format) and produces Y (file format).

## Install

    pip install my-tool

## Usage

    my-tool subcommand --input X.csv --output Y.csv

## Subcommands

- `subcommand` — one-line description.
- `other-subcommand` — one-line description.

## Inputs

- `--input` — path to X.csv. Must contain columns: `a`, `b`, `c`.

## Outputs

- `--output` — path where Y.csv will be written. Contains columns: `d`, `e`.

## Example end-to-end

    pip install my-tool
    my-tool subcommand --input examples/in.csv --output /tmp/out.csv

## Tests

    pytest tests/

## License

MIT.
```

That structure isn't beautiful prose. It's *parseable*. An agent (or a
new teammate) reading it can answer "what does this do, how do I run
it, what does it produce?" in under a minute.

## The Company publishing path

For team work, publishing to **[`github.com/Science-and-Technology-Consulting-LLC`](https://github.com/Science-and-Technology-Consulting-LLC/)**
makes your tool part of the organisation's discoverable surface.

A couple of conventions worth borrowing from the existing repos:

- Repo names are hyphen-separated and topic-named (e.g.,
  `sc-nsforest-qc-nf`, `cellxgene-harvester`).
- The README has a one-sentence summary visible above the fold.
- The default branch is `main`.
- `.github/workflows/` has at least a CI workflow (lint + test) and,
  if the tool is documented, a docs deploy workflow.
- Tagged releases are SemVer (`v1.0.0`, `v1.1.0`).

Even if your tool is mature, commit it regularly to the repository.  Working in a team environment - to a branch - and manage merging through review and pull requests. 

## Semantic versioning, briefly

When you are ready to release, this is when you tag a release, follow `MAJOR.MINOR.PATCH`:

- `1.0.0 → 1.0.1` — bug fix, no behaviour change. Safe upgrade.
- `1.0.1 → 1.1.0` — new feature, no behaviour change. Safe upgrade.
- `1.1.0 → 2.0.0` — breaking change. Document what broke.

Agents that pin to `~=1.0` get safe upgrades automatically. Agents
that pin to `==1.0.1` get exact reproducibility. Both patterns are
common; both work; both depend on you tagging *honestly*.

## Why this matters more than it used to

A year ago, "publishing" a tool meant making it usable by a person who
might find your README. That's still true — but it's no longer the
ceiling.

A well-published tool today is *also* usable by:

- An AI agent doing literature-driven analysis on a researcher's behalf.
- An autonomous pipeline run that selected your tool from a manifest.
- A federated workflow that needs your container at each site.
- A future you who, six months from now, has forgotten the details and
  re-discovers your tool through search.

All four of those readers want the same thing: structure, honesty, and
a `--help` that tells the truth.

## What you'll have at the end

One of your CLIs, published under your name or your org, with a
structured README, a tagged release, a CI badge that's green, and a
container image you (or an agent) can pull. From there,
[MCP server](mcp-server.md) is the final step that lets an agent
discover it and run it on a [platform](platforms.md).

## Where to next

→ [Platforms — a transport-layer protocol for science](platforms.md)

← Back to the [Lessons overview](index.md), or jump to the
[book companion](../chapters/index.md) for full worked examples.
