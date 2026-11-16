# Two containers, two modules: fastqc and multiqc

**This walkthrough needs [Nextflow](https://www.nextflow.io/) and [Podman](https://podman.io/docs/installation) on your computer, and an internet connection.**

You will put each tool in its own module, one file for FastQC and one for MultiQC, each with its own container image, and join them in a short workflow. This matters because a module that does one job can be tested alone, swapped for another tool, and reused in the next pipeline without editing it.

*Part of the [nextflow-modules](README.md) lesson.*

## Start here

### What you will do

- Download two small test sequencing files.
- Write a Nextflow *module* for FastQC and another for MultiQC. A module is one process in its own file.
- Write a short `main.nf` that includes both modules and runs FastQC on every sample, then MultiQC on all the reports together.
- Run it with Podman and open the report.
- Swap in a container image of your own with one option.

### What you need

- [Nextflow](https://www.nextflow.io/docs/latest/install.html), installed. Check with `nextflow -version`. It needs Java, which the `eos` environment from [conda-environments](../conda-environments/README.md) provides.
- [Podman](https://podman.io/docs/installation), installed. On a Mac or Windows computer its machine must be running (`podman machine start`). See [containers](../containers/README.md).
- The idea of one container, one job from [building container images](../containers/building-dockerfiles.md). You do not need the images you built there. This walkthrough starts from public images and shows where to put yours.
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`fastqc-and-multiqc-modules.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-modules/fastqc-and-multiqc-modules.ipynb) and run each cell in order, top to bottom.

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `nextflow` and `podman`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

> **Check:** I ran every step except the last one with Podman 6.2.0 and Nextflow 26.10 on an Apple-silicon Mac on 2026-11-16, and they passed. The last step needs an image of your own in a registry. I have not run these steps on Windows or Linux.

## Steps to execute

### Make a project folder and get the test data

Why: the project gets a folder of its own in `~/eos-practice`. The test data are two small files of sequencing reads, about 2 MB each, from [Zenodo](https://zenodo.org/records/7025773). `curl -L -O` downloads a file and follows redirects. Mac and Git Bash have `curl`; they do not have `wget`.

```bash
mkdir -p ~/eos-practice/qc-modules/data ~/eos-practice/qc-modules/modules
cd ~/eos-practice/qc-modules/data
curl -L -O https://zenodo.org/record/7025773/files/test.20k_reads_1.fastq.gz
curl -L -O https://zenodo.org/record/7025773/files/test.20k_reads_2.fastq.gz
cd ..
ls -l data
```

**What you should see:** two files, `test.20k_reads_1.fastq.gz` and `test.20k_reads_2.fastq.gz`, each about 2 MB.

### Write the FastQC module

Why: [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) checks the quality of sequencing reads. A Nextflow *process* is one step. It declares the container it runs in, what goes in, what comes out, and the command. This one runs FastQC on one sample's read files.

- `container params.fastqc_image` names the image. The name comes from a *parameter*, so you can change it without editing the module.
- `tag` labels each run in the log with the sample name.
- `publishDir` copies the reports into your results folder. Everything else stays in Nextflow's `work` folder.
- `${task.cpus}` is the number of cores Nextflow gives the task.

```bash
cat > modules/fastqc.nf <<'EOF'
process FASTQC {
    tag "${sample}"
    container params.fastqc_image
    publishDir "${params.outdir}/fastqc", mode: 'copy'

    input:
    tuple val(sample), path(reads)

    output:
    path "*_fastqc.{zip,html}", emit: reports

    script:
    """
    fastqc --quiet --threads ${task.cpus} ${reads}
    """
}
EOF
```

**What you should see:** nothing. Check with `ls modules`: you should see `fastqc.nf`.

### Write the MultiQC module

Why: [MultiQC](https://multiqc.info/) reads many tool reports and makes one summary page. This module takes all the FastQC reports together, so its input is a list of files, not one tuple.

```bash
cat > modules/multiqc.nf <<'EOF'
process MULTIQC {
    container params.multiqc_image
    publishDir "${params.outdir}/multiqc", mode: 'copy'

    input:
    path reports

    output:
    path "multiqc_report.html", emit: report
    path "multiqc_data",        emit: data

    script:
    """
    multiqc .
    """
}
EOF
```

**What you should see:** nothing. `ls modules` now shows `fastqc.nf` and `multiqc.nf`.

### Set the parameters

Why: a *parameter* is a setting you can change from the command line. The defaults live in `nextflow.config`, next to the workflow. The two images are public ones from [BioContainers](https://biocontainers.pro/). Each version is written out, so the run does not change under you.

```bash
cat > nextflow.config <<'EOF'
params {
    reads         = 'data/*_{1,2}.fastq.gz'
    outdir        = 'results'
    fastqc_image  = 'quay.io/biocontainers/fastqc:0.12.1--hdfd78af_0'
    multiqc_image = 'quay.io/biocontainers/multiqc:1.25.1--pyhdfd78af_0'
}
EOF
```

**What you should see:** nothing.

### Write the workflow

Why: the workflow joins the modules. `include` brings a process in from its file. `channel.fromFilePairs` finds the two read files of each sample and groups them under the sample name. A *channel* is a queue that carries data from one step to the next. `.collect()` waits for every FastQC report and hands them to MultiQC as one list.

```bash
cat > main.nf <<'EOF'
include { FASTQC  } from './modules/fastqc.nf'
include { MULTIQC } from './modules/multiqc.nf'

workflow {
    reads = channel.fromFilePairs(params.reads)
    FASTQC(reads)
    MULTIQC(FASTQC.out.reports.collect())
}
EOF
```

**What you should see:** nothing. `ls` now shows `data`, `main.nf`, `modules` and `nextflow.config`.

### Run it

Why: this is the payoff. The first run downloads the two images, so allow a few minutes. On a Mac or Windows computer, Podman must be running: run `podman machine start` first.

```bash
nextflow run main.nf -with-podman
```

**What you should see:** a Nextflow banner, then one line for `FASTQC (test.20k_reads)` and one for `MULTIQC`. Each ends with a tick, or reads `1 of 1`. The run finishes in under a minute after the images are downloaded.

> **Picture to add:** the terminal after the run, with both process lines complete (save as assets/fastqc-and-multiqc-modules-step-6.png)

### Look at the results

Why: the reports are in the `results` folder, because `publishDir` copied them there.

```bash
ls results/fastqc results/multiqc
```

**What you should see:** under `results/fastqc`, an `.html` and a `.zip` file for each of the two read files. Under `results/multiqc`, `multiqc_report.html` and a folder `multiqc_data`. Open `results/multiqc/multiqc_report.html` in your browser to see the summary.

> **Picture to add:** the MultiQC report open in a browser (save as assets/fastqc-and-multiqc-modules-step-7.png)

### Use an image of your own

Why: the module takes its image from a parameter, so you can run your own build with one option and no edit. The `fastqc` image you built in [building container images](../containers/building-dockerfiles.md) and published in the [publish your images](../containers/publish-your-images.md) works here. Replace `<owner>` with the name of the account that holds it. Skip this step if you did not publish an image.

```bash
nextflow run main.nf -with-podman -resume \
  --fastqc_image ghcr.io/<owner>/fastqc:v0.11.9
```

**What you should see:** the `FASTQC` line runs again, because its image changed. `MULTIQC` runs again too, because its input changed.

> **Check:** I did not run this step. The images from *Publish your images to a registry* are private until you make them public, and the commands inside them may differ from the BioContainers images. Please try it and tell me what happens.

### If something goes wrong

- **`nextflow: command not found`.** Run `conda activate eos` in the terminal, start JupyterLab from there, and run the cell again. See [conda-environments](../conda-environments/README.md).
- **`Cannot connect to Podman`, or `podman: command not found`.** Podman is not installed, or its machine is not running. On a Mac or Windows computer, run `podman machine start`, wait for it to finish, and run the cell again.
- **`curl: command not found`, or the downloaded files are tiny.** The download failed. Check your internet connection, delete the two files in `data`, and run the first cell again.
- **`No such file or directory: data/...` or `No input files`.** You are not in `~/eos-practice/qc-modules`. Run `cd ~/eos-practice/qc-modules` and run the cell again.
- **An `Error ... Script compilation failed` message.** One of the files has a typo. The message names the file and the line. Run the cell that writes that file again.
- **The run stops at `MULTIQC` with `Process requirement exceeds available memory`.** Podman's machine has too little memory. Stop it with `podman machine stop`, then run `podman machine set --memory 4096`, start it again, and rerun with `-resume`.

## Supplementary information

### One container, one module

Each module names one container and runs one command. The FastQC module does not know that MultiQC exists. That is why the `LRP2` and `sc-nsforest-qc-nf` repositories keep one file per command-line verb in a `modules` folder. A new pipeline `include`s the module it needs.

### Where the images come from

The module's `container` line is a parameter, so the image is decided at run time. The BioContainers images are built by the community from [Bioconda](https://bioconda.github.io/) recipes. Your own images, built as in [building container images](../containers/building-dockerfiles.md) and published as in [publish an image with GitHub Actions](../continuous-integration/publish-an-image-with-actions.md), come from your registry.

## Next

[A tour of Nextflow's features](tour-of-nextflow-features.md): use this same project to see channels, profiles, resume and reports.
