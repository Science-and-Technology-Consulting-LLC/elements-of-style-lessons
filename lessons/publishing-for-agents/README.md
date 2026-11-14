# Publishing for agents

*In the book: Sections 11.5.5 and 11.5.6, Publishing for Agents; Exposing Help and Schema.*

This lesson shows you how to publish a command-line tool so AI agents (and people) can find it, understand it and use it. The earlier lessons make your work run. This one makes it findable.

## Before you start

Do [agentic-harness](../agentic-harness/README.md) first. You also need the `hello-py` tool from [typer-cli-in-fifteen-minutes](../reusable-clis/typer-cli-in-fifteen-minutes.md).

## Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/publishing-for-agents/exposing-help-and-schema.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/publishing-for-agents/exposing-help-and-schema.ipynb)) and run each cell in order, top to bottom. This notebook uses a Python kernel. Its step 1 makes a conda environment first.

## What you should see

You read the `--help` pages of `hello-py` and write a JSON schema of the `greet` input into `schemas/greet.schema.json`. The schema lists one property, `name`, with the description `Who to greet.`.

> **Picture to add:** the `schemas/greet.schema.json` file printed in a terminal (save a screenshot of the finished schema) (save as assets/overview.png)

## Where the files are

- `lessons/publishing-for-agents/exposing-help-and-schema.ipynb` and `.md`: the walkthrough.
- `schemas/greet.schema.json`: created when you follow the walkthrough.
- `lessons/publishing-for-agents/assets/`: pictures for this lesson.

## Notebooks in order

1. [`exposing-help-and-schema.md`](exposing-help-and-schema.md) — give a CLI a truthful `--help` and a JSON schema

## Next

[Platforms](../platforms/README.md): where published tools run.

## Background

A well-documented CLI is an API for AI agents. An MCP server is the politest introduction your tool can make. Every habit from the earlier lessons helps:

- A repository on **GitHub** is an address an agent can read.
- A pinned **conda environment** lets an agent reproduce your setup.
- A clean **notebook** tells the agent what the analysis does.
- A **Nextflow module** gives the agent a known input and output contract.
- A **Typer CLI** lets the agent run a step without reading the source. `--help` is the API.

### What you will be able to do

1. Publish one of your CLIs as an agent-ready package.
2. Write a README an agent can act on.
3. Tag a release that others can pin to.
4. Hand the package to the [MCP server](../mcp-server/README.md) lesson.

### The agent-ready checklist

1. **A GitHub repository at a stable URL.** Ideally under an organisation, not a personal account.
2. **A README that starts with one sentence naming inputs and outputs.** Not "this is a tool for..." but "this tool takes X and produces Y."
3. **A conda environment file** (for example `eos.yml`, see [conda-environments](../conda-environments/README.md)) that pins every dependency.
4. **One entry-point CLI** (`[project.scripts]` in `pyproject.toml`), so `pip install` gives a real command. See [Reusable CLIs](../reusable-clis/README.md).
5. **A `--help` that does not lie.** Every subcommand, flag and default is accurate.
6. **At least one test that CI runs on every push**, using the CLI the way users and agents will.
7. **A licence file.** Without one, in many places nobody may use your tool. MIT or BSD-3-Clause are common for academic work.
8. **A tagged release** with semantic versioning (`v1.0.0`).
9. **A `Dockerfile`** that runs the CLI. See [Containers](../containers/README.md).
10. **Optional: an MCP server manifest** that exposes the subcommands as tools. See [MCP server](../mcp-server/README.md).

If you can say yes to 1 to 9, your tool is agent-ready before you write the MCP server.

### A README an agent can act on

Structure beats free text. A template that works:

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

### The Company publishing path

Publishing to [`github.com/Science-and-Technology-Consulting-LLC`](https://github.com/Science-and-Technology-Consulting-LLC/) makes your tool part of the organisation's findable surface. Conventions from the existing repositories:

- Repository names are hyphen-separated and named for the topic (`sc-nsforest-qc-nf`, `cellxgene-harvester`).
- The README has a one-sentence summary above the fold.
- The default branch is `main`.
- `.github/workflows/` has a CI workflow (lint and test) and, if the tool is documented, a docs deploy workflow.
- Tagged releases use SemVer (`v1.0.0`, `v1.1.0`).

Commit often, work on a branch in a team, and merge through review and pull requests.

### Semantic versioning, briefly

When you tag a release, follow `MAJOR.MINOR.PATCH`:

- `1.0.0` to `1.0.1`: bug fix, no behaviour change. Safe upgrade.
- `1.0.1` to `1.1.0`: new feature, no behaviour change. Safe upgrade.
- `1.1.0` to `2.0.0`: breaking change. Document what broke.

Agents that pin to `~=1.0` get safe upgrades. Agents that pin to `==1.0.1` get exact reproducibility. Both work, and both depend on you tagging honestly.

### Why this matters more than it used to

A well-published tool is usable by a person who finds your README, and also by an AI agent doing literature-driven analysis, an automated pipeline run that picked your tool from a manifest, a federated workflow that needs your container at each site, and you in six months. All four want structure, honesty and a `--help` that tells the truth.

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. The reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [Python Packaging User Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [GitHub Container Registry docs](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [Zenodo](https://zenodo.org/): a citable DOI for a GitHub release
- [NIH-NLM GitHub](https://github.com/NIH-NLM)
