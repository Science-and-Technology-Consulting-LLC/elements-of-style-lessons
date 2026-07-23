# Nextflow and CWL — shared structure, shared elements

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/NextflowCommonWorkFlowLanguageSharedStructureSharedElements/)) — woven into
the [nextflow-workflows](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`shared-structure-nextflow-vs-cwl.ipynb`](shared-structure-nextflow-vs-cwl.ipynb) — every code cell
  is a shell command executed by the Jupyter **Bash** kernel.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — register the Bash kernel

Only needed if you'll run the paired notebook in JupyterLab. Skip if
you're doing everything in a terminal.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

Restart JupyterLab; the launcher now shows a **Bash** tile.

### Every time — verify the tools this walkthrough uses

The commands below call one or more of these tools. Where a check
fails, the linked lesson has the install instructions.

| Tool | Check | If missing, see |
|---|---|---|
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/README.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/README.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/README.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/README.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```


## The goal

Make our science *as platform-independent and workflow-independent as
possible*, in service of open, reproducible science.

## The strategy

**Containerise at the logical, single-purpose level.** One container, one
job, one CLI. Do that, and the same container drops into a Nextflow module,
a CWL step, a Snakemake rule, or an `docker run` on your laptop. The
computation stays identical; only the composition language changes.

That is what the Elements of Style calls the *fan-in* organisational shape:
many workflow languages, all consuming the same container-level building
blocks.

## What Nextflow and CWL share

Both languages describe the same three primitives:

- **Inputs** — the parameters and files the step consumes.
- **Outputs** — the files or values the step produces.
- **Scripts / commands** — what the step actually runs (inside a container).

They differ only in *syntax* and *how dataflow between steps is expressed*
(Nextflow channels vs. CWL explicit step-output wiring). The scientific
containers are identical.

## Side-by-side — one fastqc step

**Nextflow (DSL2):**

```groovy
process fastqc {
    container 'pgc-images.sbgenomics.com/<userid>/fastqc:v0.11.9'
    input:
      path reads
    output:
      path "*_fastqc.{zip,html}"
    script:
      """
      fastqc $reads
      """
}
```

**CWL:**

```yaml
class: CommandLineTool
id: fastqc
requirements:
  - class: DockerRequirement
    dockerPull: 'pgc-images.sbgenomics.com/<userid>/fastqc:v0.11.9'
baseCommand: fastqc
inputs:
  input_reads: { type: 'File[]', inputBinding: { position: 99 } }
outputs:
  fastqc_results:
    type: Directory
    outputBinding:
      glob: results
```

Different syntax. **Same container. Same command. Same intent.**

## Benefits of this discipline

- **Reproducible science.** The container fixes the tool version; the
  workflow language just orchestrates.
- **Cleaner, testable components.** Each container can be `--help`'d and
  smoke-tested independent of any workflow engine.
- **Reusable in other workflows.** The container you built for a Nextflow
  step drops straight into someone else's CWL pipeline — or the CAVATICA
  Common Workflow Language runner, or Snakemake, or a plain shell script.

This is why the elements-of-style curriculum spends so much time on the
**containers** and **reusable-clis** lessons before ever touching a `.nf`
file: those are the *load-bearing* pieces. Workflow syntax is a thin
composition layer on top.

## Where to next

→ Back to the [nextflow-workflows lesson](README.md) for the framework's
own graduation from monolithic scripts to `modules/` + `main-*.nf`.

→ [`case-studies/multiqc-workflow/`](../../case-studies/multiqc-workflow/README.md)
— the fastqc → multiqc pipeline in the graduated container / module /
workflow structure, with Nextflow-first orchestration.
