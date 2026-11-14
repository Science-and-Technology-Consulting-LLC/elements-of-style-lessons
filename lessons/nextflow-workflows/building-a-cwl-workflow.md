# Building a Common Workflow Language (CWL) workflow

You will run the same two-step pipeline as in the Nextflow lesson, FastQC then MultiQC, written in the Common Workflow Language, so that you see how the same containers work with a different workflow language.

**What you will do:**

- Install `cwltool` and check that the CWL files are valid.
- Run each tool alone, then the two joined as a workflow.
- Read the same pipeline written for Snakemake.

**What you need:**

- The two images `fastqc` and `multiqc`, pushed to a registry as in the [module preamble](../nextflow-modules/preamble.md). The files below name `ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9` and `.../multiqc:v1.0.0`. If you pushed your own, put your address in the `dockerPull` line of each tool.
- [Docker Desktop](https://docs.docker.com/get-started/get-docker/), installed and running. `cwltool` runs each tool in its container. See the [containers lesson](../containers/README.md).
- [Python and pip](../conda-environments/README.md), to install [`cwltool`](https://cwltool.readthedocs.io/) and [Snakemake](https://snakemake.readthedocs.io/).
- A terminal. See [the command line and Git Bash](../command-line-and-git-bash/README.md).

> **Check:** Are the images `ghcr.io/science-and-technology-consulting-llc/fastqc:v0.11.9` and `.../multiqc:v1.0.0` public? A student who has not pushed their own needs to pull them without logging in.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`building-a-cwl-workflow.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/building-a-cwl-workflow.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Go to the lesson folder

*Why:* the CWL files and the Snakefile are in the lessons repository, in `lessons/nextflow-workflows`. All the commands below work from that folder. `ls` lists what is in it.

Run the next cell.

```bash
cd lessons/nextflow-workflows
ls cwl snakemake
```

**What you should see:** the contents of the `cwl` and `snakemake` folders:

```text
cwl:
fastqc.cwl
fastqc_multiqc_wf.cwl
multiqc.cwl

snakemake:
Snakefile
```

If the `cd` line prints `No such file or directory`, you are already inside `lessons/nextflow-workflows` (JupyterLab starts a notebook in its own folder). The `ls` line still works. The next cell shows where you are.

```bash
pwd
```

**What you should see:** a path that ends in `lessons/nextflow-workflows`.

> **Check:** When the notebook is opened in JupyterLab, does the Bash kernel start in the repository folder or in the notebook's own folder? The `cd lessons/nextflow-workflows` cell works only from the repository folder.

## Install `cwltool`, the reference runner

*Why:* CWL is a **specification**: a written description of tools and workflows. To run a description you need a program that reads it. `cwltool` is the reference one. Any terminal will do, including the one in JupyterLab.

Run the next cell.

```bash
pip install cwltool
cwltool --version
```

**What you should see:** pip installs `cwltool` and its helpers. The last line prints a path to `cwltool` and a version number.

## Check that each file is valid CWL

*Why:* it is quicker to find a typo now than after a long run. `--validate` reads a file and checks it without running anything.

Run the next cell.

```bash
cwltool --validate cwl/fastqc.cwl
cwltool --validate cwl/multiqc.cwl
cwltool --validate cwl/fastqc_multiqc_wf.cwl
```

**What you should see:** for each of the three files, a line saying the file is valid CWL. No errors.

## Look at the layout

*Why:* three CWL files do the work: two tools and one workflow that joins them.

```text
cwl/
  fastqc.cwl                 one tool
  multiqc.cwl                one tool
  fastqc_multiqc_wf.cwl      the workflow that stitches them
snakemake/
  Snakefile                  the same pipeline for Snakemake
```

## Read a CWL tool: `cwl/fastqc.cwl`

*Why:* a CWL tool says which container to use, which command to run, what goes in and what comes out. Read it; do not change it.

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

Notice: **the same container image** that the Nextflow module pulls. The science container is portable across workflow languages. `multiqc.cwl` has the same shape and is in the [repository](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/cwl/multiqc.cwl).

## Download the test data

*Why:* two tiny FASTQ files (raw sequencing reads, 20,000 reads each) give the tools something to work on.

Run the next cell.

```bash
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
```

**What you should see:** no output. Check with `ls`: the files `test.20k_reads_1.fastq.gz` and `test.20k_reads_2.fastq.gz` are in the folder.

## Test each tool on its own

*Why:* test the parts before you join them. First **fastqc alone**. The first run downloads the container image, so allow a few minutes. Docker Desktop must be running.

Run the next cell.

```bash
cwltool cwl/fastqc.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

**What you should see:** `cwltool` logs each step it takes, then a block of text in braces that describes the output, and finally the line `INFO Final process status is success`. A new folder `results` holds the FastQC reports.

> **Picture to add:** the terminal showing `INFO Final process status is success` after the fastqc run (save as assets/building-a-cwl-workflow-step-7.png)

Next, **multiqc alone**, using the fastqc output as its input.

Run the next cell.

```bash
cwltool cwl/multiqc.cwl --fastqc_results results
```

**What you should see:** the same kind of log, ending in `INFO Final process status is success`, and a MultiQC report in your folder.

## Read the workflow that joins them: `cwl/fastqc_multiqc_wf.cwl`

*Why:* a **workflow** in CWL lists steps and says how each step's output feeds the next step's input. Read it; do not change it.

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

1. **`inputs:`**: the workflow's top-level parameters (like Nextflow's `params`).
2. **`steps:`**: the two `run:` references. Each step names the tool and wires its `in:` and `out:`.
3. **Wiring between steps**: `fastqc/fastqc_results` means *take the `fastqc_results` output of the `fastqc` step and feed it in here.* That is CWL's version of a Nextflow channel.

## Run the whole workflow

*Why:* one command now runs both steps in order.

Run the next cell.

```bash
cwltool cwl/fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz
```

**What you should see:** `cwltool` runs the `fastqc` step, then the `multiqc` step, and ends with `INFO Final process status is success`. The output block lists `fastqc_results`, `multiqc_zip` and `multiqc_html`.

## Change a default when you run

*Why:* every input with a default can be overridden on the command line. Here we send the FastQC output to a folder called `custom_results`.

Run the next cell.

```bash
cwltool cwl/fastqc_multiqc_wf.cwl \
  --input_reads test.20k_reads_1.fastq.gz \
  --input_reads test.20k_reads_2.fastq.gz \
  --fastqc_outdir custom_results
```

**What you should see:** the same run, ending in `INFO Final process status is success`, with the FastQC reports in a folder named `custom_results`.

## The same pipeline in Snakemake

*Why:* [Snakemake](https://snakemake.readthedocs.io/) is a third workflow tool. It writes the pipeline as **rules**. Each rule names its input files, its output files and the command. The order follows from the files: a rule runs once another rule has made its input. This is `snakemake/Snakefile`. Read it:

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

Now install it and ask what it would do, **without running anything**. The flag `-n` means dry run.

Run the next cell.

```bash
pip install snakemake
cd snakemake
cp ../test.20k_reads_*.fastq.gz .
snakemake -n
cd ..
```

**What you should see:** a table of jobs and then a plan. A dry run lists four jobs: two `fastqc`, one `multiqc` and `all`. The last line says `This was a dry-run (flag -n).`

To run the containers, Snakemake uses Apptainer or Singularity, which run on Linux:

```text
snakemake --cores 2 --software-deployment-method apptainer
```

## How the three compare

The container is the same in all three. What differs is the layer around it.

- **CWL is a specification.** It describes tools and workflows. To run one you need a runner, and `cwltool` is the reference implementation ([cwltool documentation](https://cwltool.readthedocs.io/)). Nextflow is the language and the engine in one system ([Nextflow and CWL, Seqera blog](https://seqera.io/blog/nextflow-and-cwl)).
- **Snakemake runs containers through Apptainer or Singularity** ([Snakemake documentation](https://snakemake.readthedocs.io/)). Nextflow lets you choose Docker, Apptainer, Podman and others in a configuration profile, and the same script runs on your laptop, on a cluster or on a cloud platform (Section 7.8).
- **Wiring.** CWL writes each connection down. Snakemake infers the order from file names. Nextflow passes items through channels, so one process runs once for each item that arrives, with no list of files to write (Section 7.6).

Check the current documentation of each before you rely on these points. The tools change.

## Key takeaways

- The **same Docker containers** back the Nextflow, CWL and Snakemake versions.
- Test each tool alone *before* composing them.
- Wiring between steps is explicit in CWL, inferred from file names in Snakemake, and carried by channels in Nextflow. The mechanics differ. The intent is the same.
- Parameters live at the workflow level and are passed to each step.

## If something goes wrong

- **`cwltool: command not found`.** *Install `cwltool`, the reference runner* did not finish, or the environment is not active. Run `pip install cwltool` again in the terminal you are using.
- **`Cannot connect to the Docker daemon`, or the image cannot be pulled.** Docker Desktop is not running, or the image address in the `dockerPull` line is not one you can download. Start Docker Desktop, or put your own pushed image address in the `dockerPull` lines.
- **`wget: command not found`.** Mac and Git Bash do not include `wget`. Use `curl -L -O <the same web address>` for each file, or install it with `conda install wget`.
- **`No such file or directory` for `cwl/fastqc.cwl`.** You are in the wrong folder. Run `pwd`; the path must end in `lessons/nextflow-workflows`.

## Next

[Shared structure of Nextflow and CWL](shared-structure-nextflow-vs-cwl.md): what the two languages share, and how the container-level discipline lets you switch between them. Or go back to the [nextflow-workflows lesson](README.md).
