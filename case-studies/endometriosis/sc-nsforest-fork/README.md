# Chapter 9 — Forking sc-nsforest-qc-nf

This folder documents the fork of the NIH-NLM workflow
used in Chapter 9. The actual forked workflow lives at:

**https://github.com/adeslatt/sc-nsforest-qc-nf**
(to be created — see instructions below)

The original lives at:

**https://github.com/NIH-NLM/sc-nsforest-qc-nf**

## What changed in the fork

One line. That is it.

```nextflow
// Original (NIH-NLM nextflow.config)
params {
    outdir = 's3://nlm-results-bucket/sc-qc/'
}

// Fork (our nextflow.config)
params {
    outdir = './results'
}
```

The entire workflow — all processes, all containers,
all ~50 artifact-generating steps — is unchanged.
Only the destination of the outputs moved.

This is the point: separation of concerns means you can
adapt a workflow to your environment by changing one parameter,
not by rewriting the science.

## How to create the fork (Chapter 4 walkthrough)

```bash
# 1. Go to github.com/NIH-NLM/sc-nsforest-qc-nf
#    Click Fork → your account → Create fork

# 2. Clone your fork
git clone https://github.com/adeslatt/sc-nsforest-qc-nf.git
cd sc-nsforest-qc-nf

# 3. Add upstream remote (stay in sync with NIH-NLM)
git remote add upstream https://github.com/NIH-NLM/sc-nsforest-qc-nf.git

# 4. Create a branch for our change
git checkout -b redirect-publish-to-local

# 5. Edit nextflow.config — change outdir
# 6. Commit and push
git add nextflow.config
git commit -m "config: redirect publishDir to ./results for book example"
git push origin redirect-publish-to-local

# 7. Open a pull request to NIH-NLM (optional but illustrative)
```

## Running on PRJEB80304

```bash
cd sc-nsforest-qc-nf

nextflow run . \
  --input path/to/prjeb80304_processed.h5ad \
  --outdir ./results \
  -profile docker \
  -resume
```

## The ~50 artifacts

When the workflow completes, `./results` will contain
approximately 50 artifacts split between:

- NSForest outputs (marker genes, F-scores, binary heatmaps)
- scsilhouette outputs (silhouette scores, UMAP visualizations)
- Combined QC report

All HTML artifacts are self-contained Plotly files suitable
for GitHub Pages hosting — no server required.

## GitHub Pages publication

See `.github/workflows/ci.yml` in this repository for the
GitHub Actions workflow that publishes results to GitHub Pages
after every successful run.

Results will be browsable at:
https://adeslatt.github.io/sc-nsforest-qc-nf/
