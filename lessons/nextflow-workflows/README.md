# From notebooks toward Nextflow


> *In the book: Chapter 10 — Nextflow workflows.*

:::{admonition} What you'll learn
:class: tip

- Compose modules into a runnable pipeline (`main-bulk-de.nf` as the model).
- Use channels to connect step outputs to the next step's inputs.
- Run the same workflow locally, in Docker, and on Lifebit.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

A notebook is a *thinking* tool. A Nextflow workflow is a *doing*
tool — something you (or a teammate, or CI, or an AI agent) can rerun
identically a year from now on a different machine. This lesson is the
arc between the two.

:::{admonition} The rule
:class: tip

You earn the right to write a workflow by having a notebook that *works
end-to-end* first. Don't reach for Nextflow before you have the
single-step version running. The notebook is your spec.
:::

## The progression

The arc from "I have a working analysis" to "I have a reusable pipeline
anyone can run" tends to look like this:

1. **One R script** (or one Python script) — works on your machine, lives
   in a folder.
2. **The same script inside RStudio or Jupyter** — interactive, easy to
   share as a notebook.
3. **Break the notebook into functions** — each function does one thing
   well.
4. **Move those functions into a small package** — install once, import
   everywhere.
5. **Expose each package function as a CLI step** — see
   [Reusable CLIs](reusable-clis.md).
6. **Wire the CLI steps together as Nextflow modules** — see
   [Nextflow modules](nextflow-modules.md). Each module is one process
   with documented inputs and outputs.
7. **Connect the modules into a workflow** — `main.nf` orchestrates the
   modules and runs them, with provenance, on whatever compute you point
   it at.

The point isn't to do all seven at once. The point is to *know which
step you're on* and *what the next step is*. Most working scientists
live in step 2 forever. You only have to climb the ladder when the
analysis matters enough to need to be rerun.

## The worked example — `workflows/geo-to-h5ad/`

Open this in another tab right now:
**[`workflows/geo-to-h5ad/`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/workflows/geo-to-h5ad)**

It has the shape we're aiming for. Everything in this lesson refers
back to it.

```
workflows/geo-to-h5ad/
├── main.nf              # orchestrator: declares the workflow
├── nextflow.config      # profiles, defaults, container declarations
├── modules/
│   ├── download_geo_h5.nf      # one process — download
│   └── build_h5ad.nf           # one process — convert
├── bin/
│   └── build_h5ad.py    # the actual Python work
└── samplesheet.csv      # example input
```

Three things to notice before you read any code:

1. **`main.nf` is short.** The orchestrator does almost nothing
   itself — it imports modules and connects channels.
2. **Each module is one file with one process.** That isn't an
   accident — that's the rule from [containers](containers.md) applied
   to workflow steps.
3. **The actual Python lives in `bin/build_h5ad.py`.** Not inside the
   `.nf` file. That separation is the most important thing to internalize
   in this lesson.

## The anatomy of a Nextflow process

A `.nf` module is, in its bones, this:

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

Four things going on:

- **`container`** — the image to run this process in. Single-purpose
  image from the [containers](containers.md) lesson. The container
  carries the dependencies; the `.nf` carries the contract.
- **`input:`** — the data this process needs, declared in the same
  shape Nextflow channels will deliver it.
- **`output:`** — the data this process *produces*, declared in the
  same shape the next process will consume.
- **`script:`** — what to actually run. **Always call a script in
  `bin/`** rather than writing inline code. The next section explains
  why.

## Why `bin/` scripts beat inline `script:` blocks

Imagine you find a bug in your QC code. Compare:

**Inline script.** The bug lives inside a triple-quoted Bash block
inside a `.nf` file. You can't test it without running the whole
Nextflow pipeline. You can't lint it. Your editor doesn't syntax-
highlight it. You can't import its functions into a notebook.

**`bin/` script.** The bug lives in `bin/build_h5ad.py`. You can
`python bin/build_h5ad.py --input test.h5 --sample S01 --output
/tmp/out.h5ad` from your terminal and reproduce the bug in seconds.
Your editor lints it. Your test suite imports it. The Nextflow process
is just *one of several callers* of the script.

Workflows you can test are workflows that survive. **Put the work in
`bin/`. Put the contract in the `.nf`.**

## Channels — the one Nextflow concept that takes a minute to click

A Nextflow channel is a pipe that carries items, one at a time, between
processes. The orchestrator's job is to set up channels and connect
process inputs to channel outputs.

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

Two cells of intuition that pay off forever:

1. **Channels are lazy.** They don't compute anything until something
   downstream pulls on them.
2. **Channels are reusable.** The *same* channel can fan out to two
   processes that run in parallel; their outputs can be joined back
   together by a third.

## Running it

In the worked example, three runs you'll do in this lesson:

```bash
# 1. Local laptop, test data, default profile
nextflow run main.nf -profile test

# 2. Local laptop, real data, Docker profile
nextflow run main.nf -profile docker \
    --samplesheet data/my_samplesheet.csv \
    --outdir      results/

# 3. On a platform (Lifebit, AWS), with a platform-specific config
nextflow run main.nf -profile docker \
    -c configs/lifebit.config \
    --samplesheet s3://my-bucket/samplesheet.csv \
    --outdir      s3://my-bucket/results/
```

The same `main.nf` runs on all three. The *config* changes, not the
workflow. That's the payoff.

## Run the stitched workflow — three ways

::::{tab-set}

:::{tab-item} macOS / Windows (local + Docker)
:sync: local

```bash
nextflow run main-bulk-de.nf -profile docker \
    --samplesheet data/test-data/bulk-de-samplesheet.csv \
    --contrast 'CF-Control'
```
:::

:::{tab-item} macOS / Windows (test profile)
:sync: test

```bash
nextflow run main-bulk-de.nf -profile test
```
:::

:::{tab-item} Lifebit
:sync: lifebit

```bash
# On Lifebit, dispatch to AWS Batch via the lifebit profile.
# Same command, different config — that's the payoff.
nextflow run main-bulk-de.nf -profile lifebit \
    --samplesheet s3://my-bucket/bulk-de-samplesheet.csv \
    --contrast 'CF-Control'
```
:::

::::

## When NOT to use Nextflow

Be honest about the cost. Don't reach for Nextflow when:

- Your analysis is one notebook that runs in 10 minutes on your
  laptop. A notebook with a clear "Restart and Run All" is already
  enough.
- You have one data file. Nextflow's value comes from running the
  *same* code against *many* inputs in parallel; one input doesn't
  pay back the setup cost.
- You're still actively changing the analysis logic. Nextflow rewards
  stable steps; if the science is unsettled, stay in the notebook.

## What you'll have at the end

A `main.nf` you wrote yourself, with one or two modules and one or two
`bin/` scripts, running on test data on your laptop. From there you can
add modules, swap in real data, and graduate to running on a
[platform](platforms.md) — but the muscle is built.

## In-depth walkthroughs

Three walkthroughs adapted from the NICHD Kids First / INCLUDE course:

- [`building-a-nextflow-workflow.md`](building-a-nextflow-workflow.md) —
  the classic `fastqc → multiqc` pipeline as one monolithic Nextflow script,
  with a graduation note pointing at the containers / modules / `main-*.nf`
  refactor used in the [`multiqc-workflow`](../../case-studies/multiqc-workflow/README.md)
  case study. Origin: [`adeslatt/Building-A-Nextflow-Script`](https://github.com/adeslatt/Building-A-Nextflow-Script).
- [`building-a-cwl-workflow.md`](building-a-cwl-workflow.md) —
  the exact same pipeline in CWL, running under `cwltool`. Same containers,
  different composition language. Origin: [`adeslatt/Building-A-CWL-Script`](https://github.com/adeslatt/Building-A-CWL-Script).
- [`shared-structure-nextflow-vs-cwl.md`](shared-structure-nextflow-vs-cwl.md) —
  the *why* — what Nextflow and CWL share, and how the container-level
  discipline lets you switch between them.

## Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. — the reference frame for the [NLM-CKN](../../case-studies/nlm-ckn/README.md) case study.
- [Nextflow documentation](https://www.nextflow.io/docs/latest/)
- [Nextflow patterns](https://nextflow-io.github.io/patterns/) — common workflow idioms
- [nf-core pipelines](https://nf-co.re/pipelines) — production examples
- [Nextflow Tower / Seqera Platform](https://cloud.seqera.io/) — orchestration and monitoring


## Where to next

→ [Documentation](documentation.md) — write a Sphinx site for the workflow you just built.
