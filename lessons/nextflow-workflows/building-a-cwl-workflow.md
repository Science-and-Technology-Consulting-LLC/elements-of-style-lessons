# Building a Common Workflow Language (CWL) workflow

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/building-a-cwl-workflow/)) — woven into
the [nextflow-workflows](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`building-a-cwl-workflow.ipynb`](building-a-cwl-workflow.ipynb) — every code cell
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

- The same two container images from
  [`building-dockerfiles.ipynb`](../../containers/ipynb/building-dockerfiles.ipynb),
  published to a registry per [`preamble.ipynb`](../../nextflow-modules/ipynb/preamble.ipynb).
- Conda + `eos` environment active
  ([`creating-a-conda-environment.ipynb`](../../conda-environments/ipynb/creating-a-conda-environment.ipynb)).

## Clone the NICHD CWL repo

```bash
git clone https://github.com/NIH-NICHD/Building-A-CWL-Script.git
cd Building-A-CWL-Script
ls
```

(Origin: [`adeslatt/Building-A-CWL-Script`](https://github.com/adeslatt/Building-A-CWL-Script).)

## Install `cwltool` — the reference runner

```bash
conda install -c conda-forge cwltool -y
which cwltool
cwltool --version
```

## Repository structure

CWL tools live in a `cwl_tools/` directory — one `.cwl` file per step:

```
cwl_tools/
├── fastqc.cwl
└── multiqc.cwl
fastqc_multiqc_wf.cwl        <- the workflow that stitches them
```

## A CWL tool — `cwl_tools/fastqc.cwl`

```yaml
cwlVersion: v1.0
class: CommandLineTool
id: fastqc
requirements:
  - class: ShellCommandRequirement
  - class: DockerRequirement
    dockerPull: 'pgc-images.sbgenomics.com/deslattesmaysa2/fastqc:v1.0'
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

Notice: **the same container image** (`pgc-images.sbgenomics.com/…/fastqc:v1.0`)
that the Nextflow version pulled. That is the whole point — the science
container is portable across workflow languages.

## Download test data

```bash
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
```

## Test each tool independently

**fastqc alone:**

```bash
cwltool cwl_tools/fastqc.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

Look for `INFO Final process status is success`.

**multiqc alone** (using the fastqc output as its input):

```bash
cwltool cwl_tools/multiqc.cwl --fastqc_results results
```

## The workflow that stitches them — `fastqc_multiqc_wf.cwl`

```yaml
cwlVersion: v1.0
class: Workflow
id: fastqc_multiqc_wf
requirements:
  - class: MultipleInputFeatureRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_reads:   { type: 'File[]', doc: "Input fastq files" }
  fastqc_outdir: { type: 'string?', default: "results" }
  noextract:     { type: 'boolean?', default: true, doc: "FastQC flag" }
  flat:          { type: 'boolean?', default: true, doc: "MultiQC — static images" }
  filename:      { type: 'string?', default: "report.multiqc", doc: "MultiQC output prefix" }
  cores:         { type: 'int?', default: 2 }
  ram:           { type: 'int?', default: 2 }

outputs:
  fastqc_results: { type: Directory, outputSource: run_fastqc/fastqc_results }
  multiqc_zip:    { type: File,      outputSource: run_multiqc/multiqc_zip }
  multiqc_html:   { type: File,      outputSource: run_multiqc/multiqc_html }

steps:
  fastqc:
    run: cwl_tools/fastqc.cwl
    in:
      input_reads: input_reads
      outdir:      fastqc_outdir
      noextract:   noextract
      cores:       cores
      ram:         ram
    out: [fastqc_results]
  multiqc:
    run: cwl_tools/multiqc.cwl
    in:
      fastqc_results: [fastqc/fastqc_results]
      flat:           flat
      filename:       filename
      cores:          cores
      ram:            ram
    out: [multiqc_zip, multiqc_html]
```

Read three things:

1. **`inputs:`** — the workflow's top-level parameters (like Nextflow's `params`).
2. **`steps:`** — the two `run:`-references. Each step names the tool and
   wires its `in:`/`out:` explicitly.
3. **Inter-step wiring** — `[fastqc/fastqc_results]` says *"take the
   `fastqc_results` output of the `fastqc` step and feed it in here."* That
   is CWL's equivalent of Nextflow's channel dataflow.

## Execute the workflow

```bash
cwltool fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

## Override a default at runtime

```bash
cwltool fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz \
  --fastqc_outdir custom_results
```

## Key takeaways

- The **same Docker containers** back both the Nextflow and CWL versions.
- Testing individual tools *before* composing them is the discipline.
- Inter-step wiring is explicit in CWL (`step/output`), implicit in Nextflow
  channels — different mechanics, same intent.
- Parameters live at the workflow level and are passed to each step.

## Where to next

→ [`shared-structure-nextflow-vs-cwl.ipynb`](shared-structure-nextflow-vs-cwl.ipynb) —
what the two languages share and how the Elements-of-Style container-level
discipline lets you switch between them.

→ Back to the [nextflow-workflows lesson](README.md).
