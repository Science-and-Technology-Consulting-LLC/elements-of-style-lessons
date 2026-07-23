# multiqc-workflow — the FastQC / MultiQC worked example

The two-step sequencing-QC pipeline (per-sample **FastQC** aggregated by
**MultiQC**) lives in its own repository at the LLC:

**[Science-and-Technology-Consulting-LLC/multiqc-workflow](https://github.com/Science-and-Technology-Consulting-LLC/multiqc-workflow)**

This case study is the *applied* counterpart to the topical lessons on
containers and workflow composition. Every step is one of the containers
you already built in the [containers](../../lessons/containers/README.md)
walkthrough.

## What it shows

- A minimal but real Nextflow DSL2 pipeline that composes two
  single-purpose containers (`fastqc` → `multiqc`).
- The graduation from the *"one big `.nf` file"* pattern shown in the
  [`building-a-nextflow-workflow`](../../lessons/nextflow-workflows/walkthroughs/building-a-nextflow-workflow.md)
  walkthrough to the **`container/` + `modules/` + `main-*.nf`** structure
  used by [`NIH-NLM/sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf).
- The same computation runnable identically on your laptop, on Lifebit, on
  CAVATICA, and inside a GitHub Actions CI job.

## The two containers behind the workflow

Both were built in the
[`building-dockerfiles`](../../lessons/containers/walkthroughs/building-dockerfiles.md)
walkthrough:

- **[`adeslatt/fastqc-docker`](https://github.com/adeslatt/fastqc-docker)** —
  the `fastqc` image (bioconda-based, `continuumio/miniconda3` base).
- **[`adeslatt/multiqc-docker`](https://github.com/adeslatt/multiqc-docker)** —
  the `multiqc` image (same base, adds `multiqc`).

## Which lessons this case study uses

| Step | Uses lesson | Demonstrates |
|------|-------------|--------------|
| Build the two container images | [containers](../../lessons/containers/README.md) | `container/fastqc/` + `container/multiqc/` (Dockerfile + `environment.yml`) |
| Wrap each container as a Nextflow module | [nextflow-modules](../../lessons/nextflow-modules/README.md) | `modules/fastqc.nf` + `modules/multiqc.nf` |
| Compose the two modules | [nextflow-workflows](../../lessons/nextflow-workflows/README.md) | `main-multiqc-workflow.nf` |
| Publish images to a registry | [continuous-integration](../../lessons/continuous-integration/README.md) | `.github/workflows/docker-publish.yml` |
| Smoke-test on every push | [continuous-integration](../../lessons/continuous-integration/README.md) | `.github/workflows/ci.yml` — `nextflow run main-multiqc-workflow.nf -profile test` |

## The driving question

> *How do you take two published community tools (FastQC, MultiQC) and
> compose them into a reproducible, cross-platform pipeline that a
> collaborator, a CI runner, or an AI agent can run without any local
> setup other than Nextflow and Docker?*

## Data scale and where to run it

- **Test dataset** (2 x 20 k reads from Zenodo record 7025773, ~2 MB) —
  runs on any laptop in under a minute; used by the CI smoke test.
- **Real dataset** (any FASTQ collection) — bounded by the compute you
  have; a typical bulk-RNA-seq study runs in minutes on a laptop, seconds
  per sample under Lifebit's per-sample parallelism.

## See also

- The design walkthroughs in
  [`building-a-nextflow-workflow`](../../lessons/nextflow-workflows/walkthroughs/building-a-nextflow-workflow.md),
  [`building-a-cwl-workflow`](../../lessons/nextflow-workflows/walkthroughs/building-a-cwl-workflow.md),
  and
  [`shared-structure-nextflow-vs-cwl`](../../lessons/nextflow-workflows/walkthroughs/shared-structure-nextflow-vs-cwl.md).
- The [`endometriosis/`](../endometriosis/README.md) case study — same
  pattern, real biology.
- The [`oadr-autoantibody/`](../oadr-autoantibody/README.md) case study —
  same pattern, federated setting.
