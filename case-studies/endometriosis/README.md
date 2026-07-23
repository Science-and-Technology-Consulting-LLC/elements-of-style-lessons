# Endometriosis — the threaded worked example

The book is built around one dataset that follows the reader from
metadata exploration through bulk DE to single-cell case study:

**GSE179640 / PRJNA744463** — *Single-cell analysis of endometriosis
reveals a coordinated transcriptional programme driving immunotolerance
and angiogenesis across eutopic and ectopic tissues.*
([Tan et al., *Nature Cell Biology* 2022](https://pubmed.ncbi.nlm.nih.gov/35864314/))

This case study is the *applied* counterpart to the topical lessons.
Where each lesson teaches one tool or pattern, this directory shows the
tools and patterns *applied to one real biological question* end-to-end.

## What's here

```
endometriosis/
├── README.md                              (this page)
├── notebooks/
│   ├── 01_explore_metadata.ipynb          Python — metadata exploration (ENA API)
│   └── deseq2-rmd/                        R notebooks — pseudobulk DE + cross-validation
├── eye-candy/
│   └── 01_volcano_teaser.ipynb            R — DESeq2 volcano plot
├── data/
│   └── sra_explorer_metadata.tsv          61-sample export from sra-explorer.info
└── sc-nsforest-fork/                      Fork of NIH-NLM/sc-nsforest-qc-nf used in the case study
```

## Which lessons this case study uses

| Step | Uses lesson | Demonstrates |
|------|-------------|--------------|
| Pull metadata | [interactive-computing](../../lessons/interactive-computing/README.md) | Python notebook calling ENA API |
| Bulk volcano teaser | [interactive-computing](../../lessons/interactive-computing/README.md) | R notebook with DESeq2 |
| Pseudobulk DE | [containers](../../lessons/containers/README.md) + [nextflow-workflows](../../lessons/nextflow-workflows/README.md) | `container/limma-voom/` (5 CLI verbs) + `main-bulk-de.nf` |
| Single-cell markers | [nextflow-workflows](../../lessons/nextflow-workflows/README.md) | `sc-nsforest-fork/` |
| Cross-validation | (Annie's chapter — to-be-written) | Bulk DE genes vs. NSForest markers |

## The driving question

> *Which cell types in the eutopic endometrium are molecularly distinct
> in women with endometriosis — and do bulk RNA-seq and single-cell
> RNA-seq tell the same story?*

Nine patients have **both modalities** (P3, P5, P7, P9, P10, P13, P14,
P16, P17), which enables the cross-validation between bulk DE genes and
NSForest cell-type markers that is the case study's payoff.

## Data scale and where to run it

- **Bulk** (24 samples, ~10 GB) — runs on a laptop.
- **Single cell** (380 GB SRA) — needs the cloud. See the
  [platforms](../../lessons/platforms/README.md) lesson for the
  Lifebit-as-transport-layer story; free credits are listed there.

## See also

The other case study, [`oadr-autoantibody/`](../oadr-autoantibody/), is
the federated worked example used by the
[federated-computing](../../lessons/federated-computing/README.md) and
[federated-learning](../../lessons/federated-learning/README.md) lessons.
