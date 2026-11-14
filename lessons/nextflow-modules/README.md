# Nextflow modules

> *In the book: Sections 7.2 and 7.5, Nextflow: a Domain-Specific Language; Processes.*

This lesson shows you how to publish your containers and wrap each one in a Nextflow module, the smallest reusable unit of a pipeline.

## Before you start

The previous lesson is [containers](../containers/README.md). You need the `fastqc` and `multiqc` images from it.

## Do this

1. **Clone the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook** `lessons/nextflow-modules/preamble.ipynb`. From the repository folder, start JupyterLab with `jupyter lab`, then open the file. You can also [view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/nextflow-modules/preamble.ipynb). Run each cell in order, top to bottom.

## What you should see

Both images pushed to GitHub's container registry with full, versioned addresses, such as `ghcr.io/<user>/fastqc:v0.11.9`. Push lines end with `Pushed` and a final `digest: sha256:` line.

> **Picture to add:** the pushed images listed on your GitHub Packages page (save as assets/overview.png)

## Where the files are

- The lesson folder is [`lessons/nextflow-modules`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/nextflow-modules).
- The example module runners (`main-hello-py-greet.nf` and others) are in the top folder of the repository, next to `nextflow.config`.

## Notebooks in order

1. [Preamble: publish your containers before you build the workflow](preamble.md) (notebook: `preamble.ipynb`)

## Next

[Nextflow workflows](../nextflow-workflows/README.md): compose modules into a pipeline.

## Background

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
nextflow run main-hello-py-greet.nf -profile docker --name elements-of-style
```
:::

:::{tab-item} macOS / Windows (no Docker, test profile)
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

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. The reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [Nextflow documentation](https://www.nextflow.io/docs/latest/) and the [process reference](https://www.nextflow.io/docs/latest/process.html)
- [nf-core module standards](https://nf-co.re/docs/contributing/modules)
- [Groovy documentation](https://groovy-lang.org/documentation.html), Nextflow's host language
