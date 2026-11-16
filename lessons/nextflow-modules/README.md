# Nextflow modules and features

> *In the book: Sections 7.2 and 7.5, Nextflow: a Domain-Specific Language; Processes.*

This lesson shows you how to wrap each tool and its container in a Nextflow module, the smallest reusable unit of a pipeline, and then how to use the features of Nextflow that let one workflow run unchanged on your laptop, on a cluster and on a platform.

## Start here

### Before you start

The previous lesson is [Introduction to Nextflow](../nextflow-workflows/README.md), where you wrote the same pipeline as one script. Here you split it into modules. The images you built in [containers](../containers/README.md) are optional: the first notebook starts from public images and shows where to put yours.

### Do this

1. **Clone the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/nextflow-modules/fastqc-and-multiqc-modules.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`, then open the file. You can also [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-modules/fastqc-and-multiqc-modules.ipynb). Run each cell in order, top to bottom.

### What you should see

A `results` folder with FastQC reports for each test file and one `multiqc_report.html`, made by two separate modules, each with its own container image. The second notebook then adds channels, parameters, resource settings, resume, profiles and a run report to the same project.

> **Picture to add:** the terminal after the first run, with both processes complete (save as assets/overview.png)

### Where the files are

- The lesson folder is [`lessons/nextflow-modules`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/nextflow-modules).
- The example module runners (`main-hello-py-greet.nf` and others) are in the top folder of the repository, next to `nextflow.config`.

## Steps to execute

1. [Two containers, two modules: fastqc and multiqc](fastqc-and-multiqc-modules.md) (notebook: `fastqc-and-multiqc-modules.ipynb`): one module file and one container image for each tool, joined in a short workflow.
2. [A tour of Nextflow's features](tour-of-nextflow-features.md) (notebook: `tour-of-nextflow-features.ipynb`): the same project, run again with one more feature each time: channels, parameters, resource settings, resume, profiles and run reports.

To run your own images in a module, first do [Publish your images to a registry](../containers/publish-your-images.md) in the containers lesson.

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what a Nextflow process, a channel and a module are. Use FastQC as the example: what goes in, what comes out, and where the container named in the process comes from.
```

**Ask it to build.**

```text
Write a Nextflow DSL2 module in its own file for this command: <command and its options>. Requirements: one process in capital letters, the container image taken from a parameter, a tag with the sample name, publishDir from params.outdir, inputs as a tuple of sample name and files, outputs with `emit`, and a `stub` block that makes empty output files. Then write the three lines of main.nf that include and call it.
```

**Ask it to review.**

```text
Review this Nextflow module. Check that it does one job, that nothing is read from a fixed path, that the container is a parameter, and that the outputs are named. List problems with the line number. Do not rewrite.

<paste module>
```


## Further reading

- [Nextflow documentation](https://www.nextflow.io/docs/latest/) and the [process reference](https://www.nextflow.io/docs/latest/process.html)
- [nf-core module standards](https://nf-co.re/docs/guidelines/components/modules)
- [Groovy documentation](https://groovy-lang.org/documentation.html), Nextflow's host language

## Supplementary information

A Nextflow *module* is a single process with documented inputs and outputs: one brick, the smallest reusable unit of work. A workflow is bricks snapped together. Write modules your future self, your collaborator and an AI agent can reuse without reading the insides.

### What this lesson builds

1. A clean `process` block with `input:`, `output:` and `script:`.
2. A module file (`<name>.nf`) you can `include` from any workflow.
3. A `bin/` script that holds the actual work. The `.nf` file is only the contract.
4. A short test that runs the module on a tiny input and checks the output.

### Worked example

The `geo-to-h5ad` pipeline in the book companion is two modules plus a `main.nf`:

- [`download_geo_h5.nf`](https://github.com/adeslatt/elements-of-style-workflows/blob/main/workflows/geo-to-h5ad/modules/download_geo_h5.nf)
- [`build_h5ad.nf`](https://github.com/adeslatt/elements-of-style-workflows/blob/main/workflows/geo-to-h5ad/modules/build_h5ad.nf)

Each has exactly one `process` and a `bin/` script behind it.

> **Check:** These links point to the repository `adeslatt/elements-of-style-workflows`, while the rest of the course uses `Science-and-Technology-Consulting-LLC/elements-of-style-lessons`. Is that repository still the right home, and is there a `workflows/geo-to-h5ad` folder in the lessons repository?

### The deliverable

One `.nf` module, one `bin/` script and one smoke test, reusable from any workflow that needs that step.

### Run the smallest module, three ways

::::{tab-set}

:::{tab-item} macOS / Windows (local)
:sync: local

```bash
nextflow run main-hello-py-greet.nf -profile podman --name elements-of-style
```
:::

:::{tab-item} macOS / Windows (no Podman, test profile)
:sync: test

The test profile uses no container, so the command must be installed first:

```bash
pip install -e container/hello-py/context
nextflow run main-hello-py-greet.nf -profile test --name elements-of-style
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
nextflow run main-hello-py-greet.nf -profile lifebit --name elements-of-style
```
:::

::::

## Next

[Differential analysis](../differential-analysis/README.md): a real analysis, built from the same kind of pieces.
