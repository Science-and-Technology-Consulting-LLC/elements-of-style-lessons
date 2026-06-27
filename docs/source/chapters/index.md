# Worked examples in the book companion

The lessons on this site are the *teaching layer*. The full, runnable
worked examples — real data, real notebooks, real Nextflow pipelines —
live in the sibling **book companion** repository:

**[adeslatt/elements-of-style-workflows](https://github.com/adeslatt/elements-of-style-workflows)**

That repo is organized topically too. Each topic corresponds to a chapter
of Anne's Springer book *Elements of Style in Creating Workflows for
Biomedical Research,* with the code, notebooks, containers, and Nextflow
modules used in that chapter.

## The threaded dataset

All examples in the book companion work with a single dataset —
**GSE179640 / PRJNA744463** (endometriosis scRNA-seq + bulk RNA-seq) —
so you can watch the same data move from FASTQ through QC, expression
matrices, differential expression, and single-cell annotation.

## Topics you can dive into

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Reasoning from metadata
:link: https://github.com/adeslatt/elements-of-style-workflows/tree/main/chapters/reasoning-from-metadata

The first place you touch real data. Pull the study metadata from the ENA
API, subset thoughtfully, and produce the volcano plot that motivates
everything that follows.

Best paired with the [Interactive computing](../lessons/interactive-computing.md) lesson.
:::

:::{grid-item-card} Version control as survival
:link: https://github.com/adeslatt/elements-of-style-workflows/tree/main/chapters/version-control-as-survival

The Git survival guide for multi-remote biomedical workflows, including
fork patterns and the "params file" pattern for safely customizing
upstream pipelines.

Best paired with the [Version control](../lessons/version-control.md) lesson.
:::

:::{grid-item-card} Single-cell case study
:link: https://github.com/adeslatt/elements-of-style-workflows/tree/main/chapters/single-cell-case-study

The end-to-end single-cell analysis on the same dataset. Pseudobulk DE in
R (limma-voom), cross-validation notebooks, and the
`sc-nsforest-fork/` worked example for cell-type marker discovery.

Best paired with the [Toward Nextflow](../lessons/nextflow-workflows.md) and
[Reusable CLIs](../lessons/reusable-clis.md) lessons.
:::

:::{grid-item-card} Containerization, deployment, Nextflow
:link: https://github.com/adeslatt/elements-of-style-workflows/tree/main/chapters

Containerization, workflow deployment, and Nextflow development chapters
are scaffolded and being drafted. As they mature they'll get their own
cards on this page.
:::

::::

## How the topics map to the lessons

| Lesson | Best companion topic in the book repo |
|--------|----------------------------------------|
| [Version control with Git](../lessons/version-control.md) | `chapters/version-control-as-survival/` (Git survival guide) |
| [Interactive computing with Jupyter](../lessons/interactive-computing.md) | `chapters/reasoning-from-metadata/` (metadata + volcano) |
| [From notebooks toward Nextflow](../lessons/nextflow-workflows.md) | `workflows/geo-to-h5ad/` + (eventually) `chapters/nextflow-development/` |
| [Building reusable command-line tools](../lessons/reusable-clis.md) | `containers/scanpy-qc/` (the conversion target) |
