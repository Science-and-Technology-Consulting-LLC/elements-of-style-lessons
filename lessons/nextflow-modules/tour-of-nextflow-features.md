# A tour of Nextflow's features

You will run the same FastQC and MultiQC workflow again and again, each time using one more feature of Nextflow: channels, parameters, resource settings, resume, profiles and run reports. This matters because these are the features that let one workflow run unchanged on your laptop, on a cluster and on the Lifebit platform.

*Part of the [Nextflow modules and features](README.md) lesson.*

## Start here

### What you will do

- Print what flows through a channel.
- Change a setting from the command line and from a file.
- Give a process more cores in the configuration, not in the code.
- Re-run the workflow and see that Nextflow skips finished steps, and re-runs only the step you changed.
- Choose where the containers run with a profile.
- Write a report, a timeline and a diagram of the run.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous page, [Two containers, two modules](fastqc-and-multiqc-modules.md), is done. This walkthrough continues that project: the folder `~/eos-practice/qc-modules` with its `data`, `modules`, `main.nf` and `nextflow.config`.
- [Podman](https://podman.io/docs/installation), installed. On a Mac or Windows computer its machine must be running (`podman machine start`). See [Containers](../containers/README.md).
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

> **Check:** I ran these cells with Podman 6.2.0 and Nextflow 26.10 on an Apple-silicon Mac on 2026-11-16, and they passed. The lines Nextflow prints can differ between its versions. I have not run them on Windows or Linux.

## Steps to execute

### Go to the project

Why: every command below runs in the folder from the last lesson.

```bash
cd ~/eos-practice/qc-modules
ls
```

**What you should see:** `data`, `main.nf`, `modules` and `nextflow.config`, and also `results` and `work` if you ran the workflow. If `main.nf` is missing, do [two containers, two modules](fastqc-and-multiqc-modules.md) first.

### See what flows through a channel

Why: when a step does not do what you expect, the first thing to check is what is in its channel ([Introduction to Nextflow](../nextflow-workflows/building-a-nextflow-workflow.md)). `.view` prints each item as it passes. This cell rewrites `main.nf` with one extra line that prints each sample and its two files.

```bash
cat > main.nf <<'EOF'
include { FASTQC  } from './modules/fastqc.nf'
include { MULTIQC } from './modules/multiqc.nf'

workflow {
    reads = channel.fromFilePairs(params.reads)
    reads.view { id, files -> "sample ${id}: ${files*.name}" }

    FASTQC(reads)
    MULTIQC(FASTQC.out.reports.collect())
}
EOF
nextflow run main.nf -with-podman -resume
```

**What you should see:** a line that starts with `sample test.20k_reads:` and names the two read files. The processes show as cached or complete. `-resume` is explained in *Run it again and watch it skip work*.

### Change a setting from the command line

Why: a parameter belongs to the run, not to the code. Anything in the `params` block of `nextflow.config` can be changed with `--name value`. Here you send the reports to a different folder.

```bash
nextflow run main.nf -with-podman -resume --outdir results-two
ls results-two
```

**What you should see:** the folders `fastqc` and `multiqc` inside `results-two`. The tasks did not run again. Nextflow reused the earlier results, because the output folder is not part of what a task depends on.

### Keep settings in a file

Why: a run with many settings is hard to repeat from memory. A *parameters file* holds them. It is also the record you share with a colleague.

```bash
cat > params.json <<'EOF'
{
  "outdir": "results-json"
}
EOF
nextflow run main.nf -with-podman -resume -params-file params.json
ls results-json
```

**What you should see:** `fastqc` and `multiqc` inside `results-json`. A setting you type on the command line wins over the same setting in the file.

### Give a process more cores in the configuration

Why: how much computer a step needs is a property of the computer you run on, not of the tool. So it goes in the configuration, where you can change it without touching the module. The `withName` line picks the process by its name. This cell rewrites `nextflow.config` with that line and with two *profiles* (named sets of settings), which the next steps use.

```bash
cat > nextflow.config <<'EOF'
params {
    reads         = 'data/*_{1,2}.fastq.gz'
    outdir        = 'results'
    fastqc_image  = 'quay.io/biocontainers/fastqc:0.12.1--hdfd78af_0'
    multiqc_image = 'quay.io/biocontainers/multiqc:1.25.1--pyhdfd78af_0'
}

process {
    withName: FASTQC { cpus = 2 }
}

profiles {
    podman { podman.enabled = true }
    docker { docker.enabled = true }
}
EOF
cat nextflow.config
```

**What you should see:** the file you just wrote. The module is untouched: it still says `${task.cpus}`. The next task that runs uses `--threads 2`.

### Run it again and watch it skip work

Why: *resume* is what makes a long pipeline bearable. Nextflow keeps the result of each finished step in the `work` folder. With `-resume` it runs only the steps whose inputs or code changed. Cores are a setting of the computer, not part of what a step computes, so the change you just made does not count: both steps are reused. The new setting applies to the next task that actually runs. Note `-profile podman`: it is the same as `-with-podman`, but now the choice lives in the configuration.

```bash
nextflow run main.nf -profile podman -resume
```

**What you should see:** both `FASTQC` and `MULTIQC` shown as cached, and the run finishes in seconds.

> **Picture to add:** the terminal after this run, with the processes marked cached (save as assets/tour-of-nextflow-features-step-6.png)

Now change the code of one step. This cell rewrites the MultiQC module so that the report carries a comment. FastQC is untouched.

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
    multiqc --comment "Test reads" .
    """
}
EOF
nextflow run main.nf -profile podman -resume
```

**What you should see:** `FASTQC` cached and `MULTIQC` run again. Only the step whose code changed ran. In a pipeline that takes hours, that is the difference between waiting minutes and waiting a day.

### List your runs

Why: Nextflow remembers every run. `nextflow log` lists them, and you can ask it for details of one.

```bash
nextflow log
```

**What you should see:** a table with one row for each run: the time, how long it took, the run name, its status and the command. The names are two random words joined by an underscore. A failed run shows `ERR` in the status column.

### Write a report, a timeline and a diagram

Why: these three files show what happened. The *report* lists each task with its time and memory. The *timeline* shows which tasks ran when. The *diagram* shows how the steps connect. The `-with-trace` file is the same table as plain text, for a spreadsheet. `-resume` keeps this run fast.

```bash
nextflow run main.nf -profile podman -resume \
  -with-report report.html \
  -with-timeline timeline.html \
  -with-dag dag.html \
  -with-trace
ls *.html trace*
```

**What you should see:** `dag.html`, `report.html`, `timeline.html` and a trace file whose name starts with `trace`. Open `report.html` in a browser.

> **Picture to add:** the top of `report.html` with the task table (save as assets/tour-of-nextflow-features-step-8.png)

### Clean up

Why: the `work` folder keeps every step of every run, and it grows. `nextflow clean` removes the work of earlier runs. `-f` means do it without asking.

```bash
nextflow clean -f
ls
```

**What you should see:** the `work` folder is gone or smaller, and the folders `results`, `results-two` and `results-json` stay. Your results are copies made by `publishDir`, so cleaning does not lose them.

### If something goes wrong

- **`nextflow: command not found`.** Run `conda activate eos` in the terminal, start JupyterLab from there, and run the cell again.
- **`Cannot connect to Podman`, or `podman: command not found`.** Podman is not installed, or its machine is not running. On a Mac or Windows computer, run `podman machine start`, wait for it to finish, and run the cell again.
- **`Unknown profile`, or `Unknown config attribute podman.enabled`.** You ran a `-profile` step before *Give a process more cores in the configuration*. Run that cell, which writes the profiles, and try again.
- **Everything runs again although you used `-resume`.** You are in a different folder from the earlier run, or you removed `work`. Nextflow only resumes from the `work` folder next to `main.nf`.
- **`-with-dag` fails with a message about `dot`.** Ask for the diagram as a web page, `-with-dag dag.html`, as in the cell above. Other file types need the Graphviz program.

## Supplementary information

### Profiles for other computers

A profile can also choose where the work runs. The course repository's `configs/lifebit.config` sets the executor to AWS Batch for the Lifebit platform, and `configs/podman.config` runs everything on your own computer. The workflow files are the same for both. See [platforms](../platforms/README.md).

### Describing parameters for others

A workflow that other people run should say which parameters it has, their types and their defaults. Nextflow projects do this in a file called `nextflow_schema.json`. The `LRP2` repository has one, and it is the model to copy.

> **Check:** I did not build a schema in this lesson. Do you want one added, with the `nf-schema` plugin that checks parameters at the start of a run?

## Next

[Differential analysis](../differential-analysis/README.md): the same kind of pieces run a real analysis.
