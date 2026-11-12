# Building a Common Workflow Language (CWL) workflow

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/building-a-cwl-workflow/)). The CWL files
are now in this repository. Part of the [nextflow-workflows](index.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`building-a-cwl-workflow.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/building-a-cwl-workflow.ipynb) — every code cell
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
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/index.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/index.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/index.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/index.md) |

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

- The two container images, `fastqc` and `multiqc`, built in
  [`building-dockerfiles.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/containers/building-dockerfiles.ipynb)
  and pushed to GHCR (see the [module preamble](../nextflow-modules/preamble.md)).
  The files below name `ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9` and
  `.../multiqc:v1.0.0`. If you pushed your own, put your address in the `dockerPull` line of each tool.
- Docker running. `cwltool` runs each tool in its container.

## Get the files

The CWL files and the Snakefile are in the lessons repository, in your fork. Work in this folder:

```bash
cd lessons/nextflow-workflows
ls cwl snakemake
```

## Install `cwltool` — the reference runner

Any terminal will do, including the one in JupyterLab.

```bash
pip install cwltool
cwltool --version
```

Check that each file is valid CWL before you run anything:

```bash
cwltool --validate cwl/fastqc.cwl
cwltool --validate cwl/multiqc.cwl
cwltool --validate cwl/fastqc_multiqc_wf.cwl
```

## Layout

```text
cwl/
  fastqc.cwl                 one tool
  multiqc.cwl                one tool
  fastqc_multiqc_wf.cwl      the workflow that stitches them
snakemake/
  Snakefile                  the same pipeline for Snakemake
```

## A CWL tool — `cwl/fastqc.cwl`

```yaml
cwlVersion: v1.0
class: CommandLineTool
id: fastqc
requirements:
  - class: ShellCommandRequirement
  - class: DockerRequirement
    dockerPull: 'ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9'
  - class: InlineJavascriptRequirement
  - class: ResourceRequirement
    ramMin: ${ return inputs.ram * 1024 }
    coresMin: $(inputs.cores)

baseCommand: [mkdir]
arguments:
  - position: 1
    shellQuote: false
    valueFrom: >-
      $(inputs.outdir)
  - position: 2
    shellQuote: false
    valueFrom: >-
      && fastqc

inputs:
  input_reads: { type: 'File[]', inputBinding: {position: 99}, doc: "Input fastq files" }
  outdir:      { type: 'string?', default: "results", inputBinding: { position: 2, prefix: "--outdir"} }
  noextract:   { type: 'boolean?', default: true, inputBinding: { position: 2, prefix: "--noextract"} }
  cores:       { type: 'int?',  default: 2, inputBinding: { position: 2, prefix: "--threads" } }
  ram:         { type: 'int?',  default: 2 }
outputs:
  fastqc_results:
    type: Directory
    outputBinding:
      glob: $(inputs.outdir)
```

Notice: **the same container image** that the Nextflow module pulls. The science container is
portable across workflow languages. `multiqc.cwl` has the same shape and is in the
[repository](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/cwl/multiqc.cwl).

## Download test data

```bash
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
```

## Test each tool independently

**fastqc alone:**

```bash
cwltool cwl/fastqc.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

Look for `INFO Final process status is success`.

**multiqc alone** (using the fastqc output as its input):

```bash
cwltool cwl/multiqc.cwl --fastqc_results results
```

## The workflow that stitches them — `cwl/fastqc_multiqc_wf.cwl`

```yaml
cwlVersion: v1.0
class: Workflow
id: fastqc_multiqc_wf
requirements:
  - class: MultipleInputFeatureRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_reads:   { type: 'File[]', doc: "Input fastq files" }
  fastqc_outdir: { type: 'string?', default: "results", doc: "FastQC output folder" }
  noextract:     { type: 'boolean?', default: true, doc: "FastQC flag" }
  flat:          { type: 'boolean?', default: true, doc: "MultiQC static images" }
  filename:      { type: 'string?', default: "report.multiqc", doc: "MultiQC output prefix" }
  cores:         { type: 'int?', default: 2 }
  ram:           { type: 'int?', default: 2 }

outputs:
  fastqc_results: { type: Directory, outputSource: fastqc/fastqc_results }
  multiqc_zip:    { type: File,      outputSource: multiqc/multiqc_zip }
  multiqc_html:   { type: File,      outputSource: multiqc/multiqc_html }

steps:
  fastqc:
    run: fastqc.cwl
    in:
      input_reads: input_reads
      outdir:      fastqc_outdir
      noextract:   noextract
      cores:       cores
      ram:         ram
    out: [fastqc_results]
  multiqc:
    run: multiqc.cwl
    in:
      fastqc_results: fastqc/fastqc_results
      flat:           flat
      filename:       filename
      cores:          cores
      ram:            ram
    out: [multiqc_zip, multiqc_html]
```

Read three things:

1. **`inputs:`** — the workflow's top-level parameters (like Nextflow's `params`).
2. **`steps:`** — the two `run:` references. Each step names the tool and wires its `in:` and `out:`.
3. **Inter-step wiring** — `fastqc/fastqc_results` says *"take the `fastqc_results` output of the `fastqc` step and feed it in here."* That is CWL's equivalent of a Nextflow channel.

## Execute the workflow

```bash
cwltool cwl/fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

## Override a default at runtime

```bash
cwltool cwl/fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz \
  --fastqc_outdir custom_results
```

## The same pipeline in Snakemake

Snakemake writes the pipeline as rules. Each rule names its input files, its output files and the command. The
order follows from the files: a rule runs when another rule has made its input. This is
`snakemake/Snakefile`:

```python
SAMPLES = ["test.20k_reads_1", "test.20k_reads_2"]

FASTQC_IMAGE  = "docker://ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9"
MULTIQC_IMAGE = "docker://ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0"

rule all:
    input:
        "multiqc/report.multiqc.html"

rule fastqc:
    input:
        "{sample}.fastq.gz"
    output:
        html="fastqc/{sample}_fastqc.html",
        zip="fastqc/{sample}_fastqc.zip"
    container:
        FASTQC_IMAGE
    threads: 2
    shell:
        "fastqc --noextract --threads {threads} --outdir fastqc {input}"

rule multiqc:
    input:
        expand("fastqc/{sample}_fastqc.zip", sample=SAMPLES)
    output:
        "multiqc/report.multiqc.html"
    container:
        MULTIQC_IMAGE
    shell:
        "multiqc --flat --filename report.multiqc --outdir multiqc fastqc"
```

Install it and ask what it would do, without running anything:

```bash
pip install snakemake
cd snakemake
cp ../test.20k_reads_*.fastq.gz .
snakemake -n
cd ..
```

A dry run lists four jobs: two `fastqc`, one `multiqc` and `all`. To run the containers, Snakemake
uses Apptainer or Singularity, which run on Linux:

```text
snakemake --cores 2 --software-deployment-method apptainer
```

## How the three compare

The container is the same in all three. What differs is the layer around it.

- **CWL is a specification.** It describes tools and workflows. To run one you need a runner, and
  `cwltool` is the reference implementation ([cwltool documentation](https://cwltool.readthedocs.io/)).
  Nextflow is the language and the engine in one system ([Nextflow and CWL, Seqera blog](https://seqera.io/blog/nextflow-and-cwl)).
- **Snakemake runs containers through Apptainer or Singularity** ([Snakemake documentation](https://snakemake.readthedocs.io/)). Nextflow
  lets you choose Docker, Apptainer, Podman and others in a configuration profile, and the same
  script runs on your laptop, on a cluster or on a cloud platform (Section 7.8).
- **Wiring.** CWL writes each connection down. Snakemake infers the order from file names. Nextflow
  passes items through channels, so one process runs once for each item that arrives, with no
  list of files to write (Section 7.6).

Check the current documentation of each before you rely on these points. The tools change.

## Key takeaways

- The **same Docker containers** back the Nextflow, CWL and Snakemake versions.
- Test each tool alone *before* composing them.
- Inter-step wiring is explicit in CWL, inferred from file names in Snakemake, and carried by channels in Nextflow. The mechanics differ. The intent is the same.
- Parameters live at the workflow level and are passed to each step.

## Where to next

→ [`shared-structure-nextflow-vs-cwl.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/shared-structure-nextflow-vs-cwl.ipynb) —
what the two languages share and how the Elements-of-Style container-level
discipline lets you switch between them.

→ Back to the [nextflow-workflows lesson](index.md).
