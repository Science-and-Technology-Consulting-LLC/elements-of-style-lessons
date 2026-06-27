# Nextflow modules

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

## Where to next

→ [Federated computing](federated-computing.md)
