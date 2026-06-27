# Chapter 9 — DESeq2 / limma-voom R Pages

This folder holds the R-based differential expression analysis
for Chapter 9. Format is TBD — candidates are:

- **R Markdown (.Rmd)** rendered to HTML — static, version-controlled
- **Quarto (.qmd)** — modern R Markdown, renders to GitHub Pages
- **JupyterLab notebook (R kernel)** — interactive, exploratory

The decision depends on what the PRJEB80304 metadata reveals
about matched bulk + single-cell samples.

## Planned contents

```
deseq2-rmd/
├── README.md                      ← this file
├── 01_bulk_deseq2_all_samples.Rmd ← full bulk DE (all samples)
├── 02_pseudobulk_limma_voom.Rmd   ← pseudobulk from scRNA-seq
├── 03_cross_validation.Rmd        ← compare bulk vs pseudobulk
└── figures/                       ← output figures for the book
```

## The scientific question

Chapter 3 showed us: *there is signal*.
Chapter 9 asks: *what exactly is it, and in which cell types?*

The three notebooks here address this progressively:

1. **Bulk DE** — use all bulk RNA-seq samples from PRJEB80304
   with proper DESeq2 or limma-voom (not the 6-sample teaser)

2. **Pseudobulk** — aggregate scRNA-seq by cell type × patient,
   run limma-voom, identify cell-type-specific DE genes
   (the Squair et al. correct approach)

3. **Cross-validation** — do the bulk and pseudobulk analyses
   agree? Genes found by both have stronger evidence.
   Genes found only by pseudobulk reveal cell-type effects
   hidden in bulk data.

## Connection to the Squair et al. paper

The Wilcoxon rank-sum test on individual cells would give us
hundreds of false positives here. We know this from Squair et al.
(2021) Nature Communications 12:5692, benchmarked on 18 datasets.

Pseudobulk with limma-voom is the correct approach.
The cross-validation notebook makes this concrete and visible.

## Status

⏳ Awaiting confirmation of PRJEB80304 metadata before writing
   biological content. Repository structure is ready.
