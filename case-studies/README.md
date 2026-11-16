# Case studies

Worked examples that bring *all* the lessons together on one real biological question. Each lesson taught one piece. A case study shows the pieces assembled, in a real repository, with the files you can open and the results they produced.

## Start here

### Before you start

Do the lessons first, in the order of the [introduction](../lessons/introduction/README.md). Each case study has a table, *How the lessons add up*, that names the lesson for each step and the file in the repository where you can see it.

### What you will do

Read the case studies in the order below. Each one adds something the one before did not have: a first full pipeline, then a second question on the same pattern, then a federated setting, and last a pipeline reorganised for reuse.

## Steps to execute

1. [sc-nsforest-qc-nf](sc-nsforest-qc-nf/README.md): marker genes and cluster quality at scale. Functions in a package, a command-line tool, a container, Nextflow modules, GitHub Actions and a Sphinx site, in one pipeline.
2. [endometriosis](endometriosis/README.md): GSE179640, bulk and single-cell RNA-seq on one question. Centralised.
3. [oadr-autoantibody](oadr-autoantibody/README.md): Type 1 diabetes beta-cell function across four cohorts. Federated.
4. [oadr-cpep](oadr-cpep/README.md): the same analysis carried from notebook design to a Python package.
5. [LRP2](lrp2/README.md): long-read proteogenomics, reorganised so each piece is clear and can be taken into another pipeline.

> **Check:** you described the third case study as "oadr-autoantibody clustering". The existing page describes predicting residual beta-cell function under federation. Which analysis should the page cover?

Two more pages are here and not in the order above:

- [multiqc-workflow](multiqc-workflow/README.md): the fastqc and multiqc pipeline, split into containers, modules and a workflow.
- [nlm-ckn](nlm-ckn/README.md): the NLM Cell Knowledge Network, the largest example.

## Supplementary information

### Where they fit in the book

- The endometriosis case study is the *centralised* path through the book. It touches the containers, Nextflow modules and Introduction to Nextflow lessons, and ends in the cross-validation between bulk DE and NSForest markers.
- The oadr-autoantibody case study is the *federated* path. It is the worked example for both `federated-computing` and `federated-learning`, and it sits next to the `mcp-server` and `platforms` lessons as the agentic-AI demonstration.

## Next

Back to the [introduction](../lessons/introduction/README.md), to start again with a pipeline of your own.
