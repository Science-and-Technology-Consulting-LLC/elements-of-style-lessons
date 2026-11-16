# Introduction to Nextflow

> *In the book: Sections 6.2 and 7.3, Introduction to Workflow Languages; Building a Nextflow Script.*

This lesson shows you how to run a two-step pipeline in Nextflow and in CWL, and how a notebook grows into a workflow you can rerun on any machine.

## Start here

### Before you start

The previous lesson is [documentation](../documentation/README.md). This is the first of two Nextflow lessons. Here you write a whole pipeline in one script and see the same pipeline in CWL. In [Nextflow modules and features](../nextflow-modules/README.md) you then split it into modules.

### Do this

1. **Clone the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/nextflow-workflows/building-a-nextflow-workflow.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`, then open the file. You can also [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-workflows/building-a-nextflow-workflow.ipynb). Run each cell in order, top to bottom.

### What you should see

A finished `fastqc` then `multiqc` run: a `results` folder with FastQC reports for each test file and one `multiqc_report.html`. The CWL walkthrough repeats the run and ends with `INFO Final process status is success`.

> **Picture to add:** the MultiQC report open in a browser (save as assets/overview.png)

### Where the files are

- The lesson folder is [`lessons/nextflow-workflows`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/nextflow-workflows).
- The CWL tool and workflow files are in its `cwl/` folder. The Snakemake version is in `snakemake/Snakefile`.
- The Nextflow walkthrough clones its example into `~/Building-A-Nextflow-Script` and writes `main.nf` and `results/` there.

## Steps to execute

1. [Building a Nextflow workflow](building-a-nextflow-workflow.md) (notebook: `building-a-nextflow-workflow.ipynb`). The classic `fastqc` then `multiqc` pipeline as one Nextflow script. Source repository: [`adeslatt/Building-A-Nextflow-Script`](https://github.com/adeslatt/Building-A-Nextflow-Script). The same pipeline, split into containers, modules and `main-*.nf`, is the [multiqc-workflow case study](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/multiqc-workflow/README.md).
2. [Building a CWL workflow](building-a-cwl-workflow.md) (notebook: `building-a-cwl-workflow.ipynb`). The same pipeline in CWL, run with `cwltool`. Same containers, different language. Source repository: [`adeslatt/Building-A-CWL-Script`](https://github.com/adeslatt/Building-A-CWL-Script).
3. [Shared structure of Nextflow and CWL](shared-structure-nextflow-vs-cwl.md) (notebook: `shared-structure-nextflow-vs-cwl.ipynb`). What the two languages share, and why container discipline lets you switch between them.

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what `-resume` does, why it did not re-run a step, and what would make it re-run. Use the FastQC and MultiQC workflow as the example.
```

**Ask it to build.**

```text
I have these two Nextflow modules: <paste the include lines>. Write main.nf that runs the first on every sample and the second on all the results together. Add a nextflow.config with a podman profile and a docker profile, and show me the command to run it with `-profile podman -resume`. Explain what each channel carries.
```

**Ask it to review.**

```text
Review this main.nf. Is anything in it that belongs in a module or in the config? Are there steps that would run in the wrong order, or channels that are consumed twice? List problems with line numbers; do not rewrite.

<paste main.nf>
```


## Further reading

- [Nextflow documentation](https://www.nextflow.io/docs/latest/)
- [Nextflow patterns](https://nextflow-io.github.io/patterns/)
- [nf-core pipelines](https://nf-co.re/pipelines)
- [Seqera Platform](https://cloud.seqera.io/)

## Supplementary information

A notebook is a *thinking* tool. A Nextflow workflow is a *doing* tool: you, a teammate, CI or an AI agent can rerun it identically a year from now on a different machine.

**The rule:** you earn the right to write a workflow by having a notebook that works from start to finish. The notebook is your spec.

### The progression

1. One R or Python script that works on your machine.
2. The same script in RStudio or Jupyter, easy to share.
3. Break the notebook into functions, each doing one thing.
4. Move the functions into a small package.
5. Expose each function as a CLI step ([reusable CLIs](../reusable-clis/README.md)).
6. Wire the CLI steps together as Nextflow modules ([Nextflow modules and features](../nextflow-modules/README.md)).
7. Connect the modules into a workflow: `main.nf` runs them, with provenance, on whatever compute you choose.

You do not do all seven at once. Know which step you are on and what comes next. Most working scientists stay at step 2, and that is fine until the analysis matters enough to rerun.

### The worked example, `workflows/geo-to-h5ad/`

[`workflows/geo-to-h5ad/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/workflows/geo-to-h5ad) has the shape we aim for:

```text
workflows/geo-to-h5ad/
├── main.nf              # orchestrator: declares the workflow
├── nextflow.config      # profiles, defaults, container declarations
├── modules/
│   ├── download_geo_h5.nf      # one process: download
│   └── build_h5ad.nf           # one process: convert
├── bin/
│   └── build_h5ad.py    # the actual Python work
└── samplesheet.csv      # example input
```

> **Check:** The `workflows/geo-to-h5ad` folder is not in the lessons repository I have. Does it exist, and at which address?

Notice three things: `main.nf` is short; each module is one file with one process; and the real code lives in `bin/`, not in the `.nf` file.

### The anatomy of a Nextflow process

```groovy
process BUILD_H5AD {
    container "ghcr.io/adeslatt/scanpy-qc:1.0.0"

    input:
    tuple val(sample_id), path(h5)

    output:
    tuple val(sample_id), path("${sample_id}.h5ad")

    script:
    """
    build_h5ad.py \\
        --input  ${h5} \\
        --sample ${sample_id} \\
        --output ${sample_id}.h5ad
    """
}
```

`container` names the image. `input:` and `output:` declare the data in the shape channels deliver it. `script:` is what runs, and it should call a script in `bin/` rather than hold inline code. A bug in a `bin/` script can be reproduced from your terminal in seconds, linted by your editor and imported by tests. A bug inside a `.nf` text block can only be reproduced by running the whole pipeline. **Put the work in `bin/`. Put the contract in the `.nf`.**

### Channels

A channel is a pipe that carries items, one at a time, between processes.

```groovy
workflow {
    // Read a samplesheet into a channel of tuples
    samples = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.sample_id, file(row.h5_path)) }

    // Feed each tuple through the BUILD_H5AD process
    BUILD_H5AD(samples)
}
```

Channels are lazy (nothing runs until something downstream pulls), and reusable (one channel can fan out to two processes, and their outputs can be joined by a third).

### Running it

```bash
# 1. Local laptop, test data, default profile
nextflow run main.nf -profile test

# 2. Local laptop, real data, Podman profile
nextflow run main.nf -profile podman \
    --samplesheet data/my_samplesheet.csv \
    --outdir      results/

# 3. On a platform (Lifebit, AWS), with a platform-specific config
nextflow run main.nf -profile podman \
    -c configs/lifebit.config \
    --samplesheet s3://my-bucket/samplesheet.csv \
    --outdir      s3://my-bucket/results/
```

The same `main.nf` runs in all three. The config changes, not the workflow.

### Run the stitched workflow, three ways

::::{tab-set}

:::{tab-item} macOS / Windows (local + Podman)
:sync: local

```bash
nextflow run main-bulk-de.nf -profile podman \
    --samplesheet data/test-data/bulk-de-samplesheet.csv \
    --contrast 'EuE-Ctrl'
```
:::

:::{tab-item} macOS / Windows (test profile)
:sync: test

The test profile uses no container, so install the R package first. The test data are synthetic: two cell types, four control and four case donors each, with 20 genes raised on purpose. A working pipeline finds those 20 genes (`scripts/make_synthetic_test_data.py` makes them).

```bash
R CMD INSTALL container/limma-voom/context
export PATH="$(Rscript -e 'cat(system.file("scripts", package="limmaVoomCLI"))'):$PATH"
nextflow run main-bulk-de.nf -profile test
```

To run the same workflow on real cells (stromal and lymphocytes from the endometriosis atlas, cut down to a laptop size), add the samplesheet:

```bash
nextflow run main-bulk-de.nf -profile test \
    --samplesheet data/test-data/endometriosis/samplesheet.csv
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# On Lifebit, dispatch to AWS Batch via the lifebit profile.
# Same command, different config.
nextflow run main-bulk-de.nf -profile lifebit \
    --samplesheet s3://my-bucket/bulk-de-samplesheet.csv \
    --contrast 'EuE-Ctrl'
```
:::

::::

### When not to use Nextflow

- Your analysis is one notebook that runs in 10 minutes on your laptop. "Restart and Run All" is enough.
- You have one data file. Nextflow pays off when the *same* code runs on *many* inputs in parallel.
- You are still changing the analysis logic. Nextflow rewards stable steps.

## Next

[Nextflow modules and features](../nextflow-modules/README.md): split this script into one module for each tool, then use the features that let it run on any computer.
