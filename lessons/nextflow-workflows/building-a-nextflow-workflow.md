# Building a Nextflow workflow: fastqc then multiqc

You will run a two-step pipeline, first FastQC on sequencing files and then MultiQC to combine the results, using [Nextflow](https://www.nextflow.io/docs/latest/), so that the same steps run the same way on any computer.

**What you will do:**

- Get the example files and install Nextflow.
- Learn the five parts of a Nextflow script: parameters, processes, channels, operators and configuration.
- Write a short Nextflow script and run it on two small test files.

**What you need:**

- [Docker Desktop](https://docs.docker.com/get-started/get-docker/), installed and running. See the [containers lesson](../containers/README.md).
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) and the `eos` environment from [conda environments](../conda-environments/README.md).
- [Nextflow](https://www.nextflow.io/docs/latest/install.html) (*Install Nextflow* installs it with conda).
- A terminal. See [the command line and Git Bash](../command-line-and-git-bash/README.md).
- An internet connection. The test files come from [Zenodo](https://zenodo.org/records/7025773), and Docker downloads two small tool images on the first run.

You do not need the images from the earlier lessons. The script below uses public images.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`building-a-nextflow-workflow.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/building-a-nextflow-workflow.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Get the example files

*Why:* the example repository holds a small pipeline and test data. First go to your home folder, so that the clone does not land inside the course folder.

Run the next cell.

```bash
cd ~
pwd
```

**What you should see:** your home folder.

The next cell clones the example repository from GitHub. To **clone** is to copy a repository to your computer.

Run the next cell.

```bash
git clone https://github.com/adeslatt/Building-A-Nextflow-Script.git
cd Building-A-Nextflow-Script
ls -l
```

**What you should see:** `Cloning into 'Building-A-Nextflow-Script'...`, progress lines, then a listing that includes `README.md`, `cwl_tools`, `fastqc.nf`, `fastqc_multiqc_wf.cwl`, `fastqc_multiqc_wf.nf`, `nextflow.config`, `params_reads.nf` and `testdata`.

## Install Nextflow

*Why:* Nextflow is the program that reads your script and runs the steps. The first line installs it with conda into the active environment. The other two lines show where it is and which version you have.

Start JupyterLab from a terminal where you have already run `conda activate eos`. Then the notebook uses the same environment.

Run the next cell.

```bash
conda install -c bioconda nextflow -y
which nextflow
nextflow -version
```

**What you should see:** conda installs the package (or says `All requested packages already installed`). Then a path to `nextflow` inside your `eos` environment, and a banner like this (your version number will differ):

```text
      N E X T F L O W
      version 26.10.5 build 14654
```

## Read the anatomy of a Nextflow script

*Why:* a Nextflow script has five moving parts. Learn them once and every workflow you meet becomes readable. Nothing to run in this step. The snippets show the shape; the script you run is in *Write the script and run it*.

### 1. Parameters: the workflow's inputs

```groovy
params.reads = false
println "My reads: ${params.reads}"
```

A **parameter** is a setting a user passes on the command line, such as `--reads`. Each one has a default, often `false`, to force the user to set it.

### 2. Processes: the computational steps

A **process** is one step: one input, one script, one output. The `container` line names the image the step runs inside.

```groovy
process fastqc {
    publishDir "results", mode: 'copy'
    container 'ghcr.io/<owner>/fastqc:v0.11.9'

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

> **Note.** Older Nextflow scripts are written in a style called **DSL1**, with `from` and `into` on the input and output lines. Current Nextflow uses **DSL2**, shown here. It is cleaner, it can be split into modules, and the sc-nsforest-qc-nf project uses it.

### 3. Channels: how data flows between processes

A **channel** carries items from one process to the next. For paired-end FASTQ files (two files per sample) you would use `fromFilePairs`:

```groovy
Channel
    .fromFilePairs(params.reads, checkIfExists: true)
    .set { read_pairs_ch }
```

### 4. Operators: small changes to channels

An **operator** reshapes a channel. `.collect()` gathers every output into one list. You need it before a step that works on *all* the results at once, such as `multiqc`:

```groovy
process multiqc {
    publishDir "results", mode: 'copy'
    container 'ghcr.io/<owner>/multiqc:v1.0.0'

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

### 5. Configuration: everything else, out of the script

The file `nextflow.config` is where you set the container engine, resource limits, and **profiles** (named sets of settings) for different platforms: test, docker and lifebit.

## Download two test files

*Why:* FASTQ files hold raw sequencing reads. These two are tiny (20,000 reads each) and are the same files the [CWL walkthrough](building-a-cwl-workflow.md) uses.

Run the next cell.

```bash
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
wget -q https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
```

**What you should see:** no output (`-q` means quiet). Check with `ls`: the files `test.20k_reads_1.fastq.gz` and `test.20k_reads_2.fastq.gz` are in the folder.

## Write the script and run it

*Why:* the repository's own script is written in the older DSL1 style, and its container images sit in a private registry, so it does not run with current Nextflow. The next cell writes a small DSL2 version of the same two steps to `main.nf`, using public container images, and runs it. The first run downloads the two images, so allow a few minutes.

Make sure Docker Desktop is running. Then run the next cell.

```bash
cat > main.nf <<'EOF'
nextflow.enable.dsl = 2

params.reads = false

process FASTQC {
    tag "$name"
    publishDir "results", mode: 'copy'
    container 'quay.io/biocontainers/fastqc:0.12.1--hdfd78af_0'

    input:
    tuple val(name), path(reads)

    output:
    path "*_fastqc.{zip,html}"

    script:
    """
    fastqc $reads
    """
}

process MULTIQC {
    publishDir "results", mode: 'copy'
    container 'quay.io/biocontainers/multiqc:1.25.1--pyhdfd78af_0'

    input:
    path 'fastqc/*'

    output:
    path "multiqc_report.html"
    path "multiqc_data"

    script:
    """
    multiqc . -m fastqc
    """
}

workflow {
    reads = Channel.fromFilePairs(params.reads, size: 2)
    FASTQC(reads)
    MULTIQC(FASTQC.out.collect())
}
EOF
nextflow run main.nf --reads 'test.20k_reads_{1,2}.fastq.gz' -with-docker
```

**What you should see:** Nextflow prints a header with its version and the script name, then one progress line for each step, `FASTQC` and `MULTIQC`. Each line shows a short hash such as `[ab/12cd34]` and reaches `100%`. At the end it returns to the prompt without an error message.

> **Picture to add:** the terminal output of the finished nextflow run, with both steps at 100% (save as assets/building-a-nextflow-workflow-step-5.png)

## Look at the results

*Why:* `publishDir "results"` told Nextflow to copy each step's outputs into a folder called `results`.

Run the next cell.

```bash
ls results
```

**What you should see:** the per-sample FastQC files `test.20k_reads_1_fastqc.html`, `test.20k_reads_1_fastqc.zip`, `test.20k_reads_2_fastqc.html` and `test.20k_reads_2_fastqc.zip`, one combined `multiqc_report.html`, and a folder `multiqc_data`. Open `multiqc_report.html` in your web browser to see the combined report.

> **Picture to add:** the multiqc_report.html page open in a browser (save as assets/building-a-nextflow-workflow-step-6.png)

## If something goes wrong

- **`wget: command not found`.** Mac and Git Bash do not include `wget`. Use `curl -L -O <the same web address>` for each file, or install it with `conda install wget`.
- **`Cannot connect to the Docker daemon`, or `docker: command not found`.** Docker Desktop is not running or not installed. Open it, wait until it says it is running, and run *Write the script and run it* again.
- **`nextflow: command not found`.** The environment is not active. Close JupyterLab, run `conda activate eos` in a terminal, start JupyterLab again from that terminal, and repeat *Install Nextflow*.
- **`Cannot find script file: main.nf`.** You are in the wrong folder. Run `pwd`; it must end in `Building-A-Nextflow-Script`. If it does not, run `cd ~/Building-A-Nextflow-Script` and run the *Write the script and run it* cell again.

## Next

- [Building a CWL workflow](building-a-cwl-workflow.md): the same two steps written in Common Workflow Language, for comparison.
- [Shared structure of Nextflow and CWL](shared-structure-nextflow-vs-cwl.md): what the two languages agree on, and why that makes your work portable.
- [The multiqc-workflow case study](../../case-studies/multiqc-workflow/README.md): the same pipeline reorganised into containers, modules and a workflow.
