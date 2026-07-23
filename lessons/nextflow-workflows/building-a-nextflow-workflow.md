# Building a Nextflow workflow — fastqc → multiqc

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/building-a-nextflow-workflow/)) — woven into
the [nextflow-workflows](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`building-a-nextflow-workflow.ipynb`](building-a-nextflow-workflow.ipynb) — every code cell
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


## Prerequisites

- Two container images from
  [`building-dockerfiles.ipynb`](../../containers/ipynb/building-dockerfiles.ipynb),
  published per [`preamble.ipynb`](../../nextflow-modules/ipynb/preamble.ipynb).
- Conda from
  [`creating-a-conda-environment.ipynb`](../../conda-environments/ipynb/creating-a-conda-environment.ipynb),
  active as `eos`.
- Docker on your PATH (see [containers](../containers/README.md)).

## Clone the NICHD example

You have two equally-valid clone sources:

```bash
# The NICHD teaching fork (unchanged for the course):
git clone https://github.com/NIH-NICHD/Building-A-Nextflow-Script.git

# The upstream origin (where fixes land first):
git clone https://github.com/adeslatt/Building-A-Nextflow-Script.git
```

Either works — the two are typically in sync during the training week.

```bash
git clone https://github.com/adeslatt/Building-A-Nextflow-Script.git
cd Building-A-Nextflow-Script
ls -l
```

## Install Nextflow

Inside the `eos` conda environment:

```bash
conda install -c bioconda nextflow -y
which nextflow
nextflow -version
```

## Anatomy of a Nextflow script

A Nextflow script has five moving parts. Learn them once, and every workflow
you meet becomes readable.

### 1. Parameters — the workflow's inputs

```groovy
params.reads = false
println "My reads: ${params.reads}"
```

Parameters are the `--reads` etc. flags a user passes on the command line.
Every parameter has a default (often `false`, to force the user to set it).

### 2. Processes — the computational steps

A `process` is one step: one input, one script, one output. The container
directive names the image *from the registry* the step will run inside.

```groovy
process fastqc {
    publishDir "results", mode: 'copy'
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

:::{note}
The NICHD version was written in **DSL1** (with `from` and `into` on the
input/output lines). Nextflow's current default is **DSL2**, which is what
you see here — cleaner, composable via modules, and required by the
sc-nsforest-qc-nf pattern.
:::

### 3. Channels — how data flows between processes

Channels connect the output of one process to the input of the next. For
paired-end FASTQs you'd typically use `fromFilePairs`:

```groovy
Channel
    .fromFilePairs(params.reads, checkIfExists: true)
    .set { read_pairs_ch }
```

### 4. Operators — small transformations on channels

`.collect()` gathers every output into a single list — you need this before
a step that operates on *all* the results at once (like `multiqc`):

```groovy
process multiqc {
    publishDir "results", mode: 'copy'
    container 'pgc-images.sbgenomics.com/<userid>/multiqc:v1.0dev0'

    input:
      path fastqc_results
    output:
      path "multiqc_report.html"
    script:
      """
      multiqc .
      """
}

workflow {
    Channel.fromFilePairs(params.reads) | fastqc | collect | multiqc
}
```

### 5. Configuration — everything else, out of the script

`nextflow.config` is where you set container engines, resource limits, and
profiles for different platforms (test / docker / lifebit).

## Run it

Give Nextflow some FASTQs to work on (the same tiny test files the
[CWL walkthrough](building-a-cwl-workflow.ipynb) uses):

```bash
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
```

Then run the pipeline (adjust the script name to match the repo's
actual entry-point — often `main.nf`):

```bash
nextflow run main.nf --reads 'test.20k_reads_{1,2}.fastq.gz' -with-docker
```

On success, `results/` contains per-sample fastqc HTML/ZIP files
and one aggregated `multiqc_report.html`.

## Where to next

→ [`building-a-cwl-workflow.ipynb`](building-a-cwl-workflow.ipynb) — the
same two steps written in Common Workflow Language for comparison.

→ [`shared-structure-nextflow-vs-cwl.ipynb`](shared-structure-nextflow-vs-cwl.ipynb) —
what the two languages agree on and why that matters for platform independence.

→ [`case-studies/multiqc-workflow/`](../../case-studies/multiqc-workflow/README.md)
— the same pipeline reorganised into the container / module / workflow
graduation structure.
