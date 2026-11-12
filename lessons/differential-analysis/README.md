# Differential analysis, single-cell to pseudobulk

> *In the book: Chapter 3 (the dataset) and Chapter 9 (pseudobulk and limma-voom).*

:::{admonition} What you'll learn
:class: tip

- Turn single-cell counts into one pseudobulk sample per cell type, donor and condition.
- Test for differences between endometriosis and control with limma-voom.
- Read a volcano plot, and check the result against genes you already know.
:::

The data are the public endometriosis single-cell atlas from The Jackson
Laboratory (Tan et al., 2022, *Nature Cell Biology*, PMID 35864314). Both
notebooks download what they need from the JAX Single Cell Portal, so there
is nothing to copy by hand. The first download is about 1 GB.

## Run them in order

1. [`pseudobulk_limma_voom.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/differential-analysis/pseudobulk_limma_voom.ipynb)
   (Python 3 kernel). Downloads the h5ad, sums raw counts per cell type,
   donor and condition, and writes CSVs to `pseudobulk/`.
2. [`limma_voom_de.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/differential-analysis/limma_voom_de.ipynb)
   (R kernel). Reads those CSVs, runs limma-voom for each cell type, and
   draws the volcano plots.

Run the first before the second. Use "Restart and Run All" in each.

## Why pseudobulk

Cells from one donor are not independent of each other. Testing every cell
as a separate sample overstates the evidence. Summing counts per donor makes
the donor the unit of replication, and a bulk method such as limma-voom
then applies.

## The same steps as a workflow

The five limma-voom modules in [`modules/limma-voom/`](../../modules/limma-voom/)
and the stitched [`main-bulk-de.nf`](../../main-bulk-de.nf) run this analysis
as a Nextflow workflow. See [Nextflow workflows](../nextflow-workflows/README.md).

## Where to go next

The case study that this lesson draws on is in
[`case-studies/endometriosis/`](../../case-studies/endometriosis/README.md).
