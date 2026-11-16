# sc-nsforest-qc-nf: marker genes and cluster quality, at scale

The first case study. It shows every lesson of the course at work in one real pipeline: functions in a Python package, a command-line tool, a container, Nextflow modules, a workflow that runs the same code on a laptop and on the Lifebit platform, GitHub Actions that publish the image and the documentation, and a Sphinx site.

*Part of the [case studies](../README.md).*

## Start here

### The driving question

> *Given single-cell RNA-seq data for an organ from many published studies, which small sets of genes mark each cell type, and how well does each published cluster hold together?*

The pipeline finds marker genes with [NSForest](https://github.com/JCVenterInstitute/NSForest) (Aevermann et al. 2021) and scores each cluster with the silhouette method (Rousseeuw 1987), through the [scsilhouette](https://github.com/NIH-NLM/scsilhouette) package. It runs the same steps for every dataset in a table, so one run covers many studies.

### What you need

The lessons below, in this order. Each step in *How the lessons add up* names the lesson and the file in the repository where you can see it.

### Where the code is

- The repository: [NIH-NLM/sc-nsforest-qc-nf](https://github.com/NIH-NLM/sc-nsforest-qc-nf).
- The paths below are the ones at the tag `v1.0` of the repository, as it appears in the checkout I read.
- The documentation site: <https://nih-nlm.github.io/sc-nsforest-qc-nf/>.

> **Check:** which commit should this page pin? The local tag `v1.0` points to `d1fae1b`, but your close-out notes of 2026-10-18 give `05c4306`. A DOI or commit hash in this page would settle it.

## Steps to execute

### How the lessons add up

| Step | Lesson | Where to see it |
|------|--------|-----------------|
| Work at a Bash prompt, with the paths of a real project | [command-line-and-git-bash](../../lessons/command-line-and-git-bash/README.md) | the `nextflow run main.nf --datasets_csv … --organ …` line in the repository README |
| Keep every change in Git, in your own fork | [version-control](../../lessons/version-control/README.md) | the repository's branches and the tag `v1.0` |
| One clean environment per tool | [conda-environments](../../lessons/conda-environments/README.md) | `container/nsforest/context/nsforest.yml` |
| One function per step, in a package | [reusable-clis](../../lessons/reusable-clis/README.md) | `container/nsforest/context/src/nsforest_cli/`: one Python file for each step (`cluster_stats.py`, `dendrogram.py`, `filter_adata.py`, `prep_medians.py`, `run_nsforest.py`, and others) |
| Call each function from the command line | [reusable-clis](../../lessons/reusable-clis/README.md) | `nsforest_cli/main.py`: a [Typer](https://typer.tiangolo.com/) app with one command for each verb, installed as `nsforest-cli` by `setup.py` |
| One container for the package | [containers](../../lessons/containers/README.md) | `container/nsforest/Dockerfile`: a micromamba base, the environment file, the package source, and NSForest cloned from its repository |
| Publish the image, tagged by the commit | [continuous-integration](../../lessons/continuous-integration/README.md) | `.github/workflows/docker-publish.yml`: builds `./container/nsforest/` on every push to `main` and pushes it to the GitHub Container Registry |
| Document it and publish the pages | [documentation](../../lessons/documentation/README.md) | `.github/workflows/docs.yml` and `docs/source/` (a Sphinx site) |
| One module for each command | [Nextflow modules and features](../../lessons/nextflow-modules/README.md) | `modules/nsforest/`, `modules/scsilhouette/` and `modules/publish/`: one process in each file, each calling one `nsforest-cli` command or a scsilhouette command |
| Join the modules in a workflow | [Nextflow modules and features](../../lessons/nextflow-modules/README.md) | `main.nf`: reads the datasets table, runs the filter and the per-dataset steps, scatters NSForest over batches of clusters and gathers the results |
| Settings apart from code | [the tour of features](../../lessons/nextflow-modules/tour-of-nextflow-features.md) | `nextflow.config`, the parameters in `main.nf`, and the memory settings described in the repository README under *Memory budgets for large datasets* |
| Run it on a platform | [platforms](../../lessons/platforms/README.md) | the repository README: `--github_token` is passed as a platform secret |

### Read the pipeline in three passes

1. **Read `main.nf` from the top.** The header says what the workflow does. The `include` lines list every module. The `workflow` block reads the datasets CSV with `splitCsv`, skips rows whose `reference` column marks them as excluded, and builds one `meta` map of settings for each dataset.
2. **Open one module.** `modules/nsforest/cluster_stats.nf` is typical. A comment block says what goes in and what comes out. The process has a `label`, a `publishDir` and a script of one `nsforest-cli cluster-stats …` command. Nothing else is in it.
3. **Open the command it calls.** In `nsforest_cli/main.py`, the `cluster-stats` command takes the same options that the module passes, and calls the function in `cluster_stats.py`.

The same name appears three times (the function, the command, the module) and does one job each time. That is the pattern the course teaches.

## Further reading

- The repository README, for the parameters, the output folders and the memory budgets for large datasets.
- [NSForest](https://github.com/JCVenterInstitute/NSForest), from the J. Craig Venter Institute.
- [scsilhouette](https://github.com/NIH-NLM/scsilhouette), the silhouette package.
- [cellxgene-harvester](https://github.com/NIH-NLM/cellxgene-harvester), which prepares the datasets table.
- [Typer](https://typer.tiangolo.com/) and [Nextflow](https://www.nextflow.io/docs/latest/).

## Supplementary information

### What it produced

> **Check:** these figures come from your run notes, not from the repository. Please confirm them and the revision before they go in print. A run of the `neocortex-run` branch on Lifebit on 2026-10-23, on the downsampled human neocortex atlas of Jorstad et al. 2023, reproduced the published NSForest results: 24 of 24 subclasses and 153 of 153 clusters with the same markers in the same order. The published tables are on Zenodo, DOI [10.5281/zenodo.13172641](https://doi.org/10.5281/zenodo.13172641).

### Scale

Large datasets need more memory. The repository README sorts the processes into three tiers: those that densify the matrix (768 GB for a dataset of more than a million cells), those that load the file without densifying it (384 GB), and small utility steps that keep their defaults. It explains why not to give everything the largest size: cost, and the memory caps on the platform.

### Choices worth noticing

- The scatter and gather: NSForest runs in batches of clusters in parallel, and `merge_nsforest_results` joins the pieces.
- At the tag `v1.0`, `nextflow.config` names the image as `ghcr.io/nih-nlm/sc-nsforest-qc-nf/nsforest:latest`. A tag called `latest` moves when the image is rebuilt, so the same code can run a different image later. The [LRP2 case study](../lrp2/README.md) shows the other pattern: tag every image with the commit that built it, and pass the tag as a parameter.

## References

- Aevermann B, Zhang Y, Novotny M, et al. A machine learning method for the discovery of minimum marker gene combinations for cell type identification from single-cell RNA sequencing. *Genome Research* 2021. doi: [10.1101/gr.275569.121](https://doi.org/10.1101/gr.275569.121).
- Rousseeuw PJ. Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics* 1987;20:53-65. doi: [10.1016/0377-0427(87)90125-7](https://doi.org/10.1016/0377-0427(87)90125-7).
- NSForest results for the human neocortex cross-areal atlas. Zenodo, 2024. doi: [10.5281/zenodo.13172641](https://doi.org/10.5281/zenodo.13172641).

## Next

[Endometriosis](../endometriosis/README.md): the same pattern on a different question, with bulk and single-cell data side by side.
