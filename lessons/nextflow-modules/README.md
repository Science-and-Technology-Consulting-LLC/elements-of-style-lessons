# Nextflow modules


> *In the book: Chapter 9 — Nextflow modules.*

:::{admonition} What you'll learn
:class: tip

- Write a `.nf` module that wraps exactly one CLI verb.
- Test the module standalone with its `main-*.nf` runner.
- Why `bin/` scripts (or installed CLIs) beat inline `script:` blocks.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

A Nextflow *module* is a single process with documented inputs and
outputs. Think of it as one LEGO brick — the smallest reusable unit of
work in your pipeline. A workflow is a *snap-together* of modules.

This deeper-dive sub-section is where you learn to write modules
your future self (and your collaborator, and an AI agent) can reuse
without reading their internals.

## What this lesson builds

1. A clean `process` block with `input:`, `output:`, and `script:`.
2. A module file (`<name>.nf`) you can `include` from any workflow.
3. A `bin/` script that holds the *actual work* — the `.nf` file is
   just the contract.
4. A short test that runs the module on a tiny input and asserts the
   output shape.

## Worked example in the book companion

The `geo-to-h5ad` pipeline in the book companion repo is two modules
plus a `main.nf` orchestrator:

- [`workflows/geo-to-h5ad/modules/download_geo_h5.nf`](https://github.com/adeslatt/elements-of-style-workflows/blob/main/workflows/geo-to-h5ad/modules/download_geo_h5.nf)
- [`workflows/geo-to-h5ad/modules/build_h5ad.nf`](https://github.com/adeslatt/elements-of-style-workflows/blob/main/workflows/geo-to-h5ad/modules/build_h5ad.nf)

Read both. Note how each has exactly one `process` and a `bin/` script
backing it.

## The deliverable

One `.nf` module + one `bin/` script + one smoke test. Reusable from
any workflow that needs that step.

## Run the smallest module — three ways

::::{tab-set}

:::{tab-item} macOS / Windows (local)
:sync: local

```bash
nextflow run main-hello-py-greet.nf -profile docker --name elements-of-style
```
:::

:::{tab-item} macOS / Windows (no Docker — test profile)
:sync: test

```bash
nextflow run main-hello-py-greet.nf -profile test --name elements-of-style
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
nextflow run main-hello-py-greet.nf -profile lifebit --name elements-of-style
# (Lifebit may require the file to be named main.nf — copy or symlink
#  at deploy time. TBD:  confirming.)
```
:::

::::

## Further reading

- [Nextflow documentation](https://www.nextflow.io/docs/latest/)
- [nf-core module standards](https://nf-co.re/docs/contributing/modules) — community conventions
- [Nextflow process reference](https://www.nextflow.io/docs/latest/process.html)
- [Groovy documentation](https://groovy-lang.org/documentation.html) — Nextflow's host language


## Where to next

→ [Nextflow workflows](nextflow-workflows.md) — compose modules into a pipeline.
