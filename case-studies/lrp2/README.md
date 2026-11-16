# LRP2: long-read proteogenomics, reorganised for reuse

The last case study, and the one that brings every lesson together. LRP2 takes PacBio long reads through to protein isoforms and differential splicing. This page is about how it is *organised*: how a large, working pipeline was rearranged so that each piece is clear, can be run alone, and can be taken into another pipeline.

*Part of the [case studies](../README.md).*

## Start here

### The driving question

> *From long-read RNA sequencing of two groups of samples, which transcript isoforms and which protein forms (open reading frames) differ between the groups, and which of them are new?*

The pipeline runs in four stages (from the repository README):

1. **S1 PacBio Isocall:** `pbmm2` alignment, then the Isocall profile, prep, merge and call steps.
2. **S2 Transcriptome:** SQANTI3 quality control, hash ids, filtering.
3. **S3 Predicted proteome:** CPAT, CPAT filter, SQANTI3 protein, protein classification.
4. **S4 Multisample:** LeafCutter, then edgeR and DRIMSeq, one comparison for each pair of conditions.

### What you need

All the earlier lessons, and the [sc-nsforest-qc-nf case study](../sc-nsforest-qc-nf/README.md), whose layout LRP2 follows.

### Where the code is

- The repository: [Science-and-Technology-Consulting-LLC/LRP2](https://github.com/Science-and-Technology-Consulting-LLC/LRP2).
- The paths below are the ones on the `main` branch of the checkout I read.

> **Check:** this page says what was changed in the LRP2 repository to make it clearer and reusable. I took that from the repository README, from the layout of the files, and from the decisions you recorded on 2026-11-06. Please correct anything that credits you, or the original authors, wrongly. The README credits the original LRP pipeline to the Sheynkman Lab and names the LRP2 developers; this page does not repeat that list.

## Steps to execute

### How the lessons add up

| Step | Lesson | Where to see it |
|------|--------|-----------------|
| One environment for the notebooks | [conda-environments](../../lessons/conda-environments/README.md) | `lrp2.yml`: `conda env create -f lrp2.yml` |
| Scripts that take flags | [reusable-clis](../../lessons/reusable-clis/README.md) | the R and Python scripts inside `container/lrp2_lite/context/src`, called with options such as `--basename` and `--classification` |
| One container for each package | [containers](../../lessons/containers/README.md) | `container/<package>/`, each with a `Dockerfile` and a `context` folder: `lrp2_lite`, `cpat`, `leafcutter_longread`, `sqanti3_protein`, `isocall`, `fragpipe`, `metamorpheus` |
| Build and publish every image | [continuous-integration](../../lessons/continuous-integration/README.md) | `.github/workflows/docker-publish.yml`: one job for each image, started when something under `container/` changes |
| Document it | [documentation](../../lessons/documentation/README.md) | `docs/` and `.github/workflows/docs.yml` |
| One module for each step | [Nextflow modules and features](../../lessons/nextflow-modules/README.md) | `modules/<package>/<name>.nf`: one process in each file, named for the process (for example `modules/lrp2_lite/generate_hashids.nf` holds `GENERATE_HASHIDS`) |
| A workflow that only connects them | [Nextflow modules and features](../../lessons/nextflow-modules/README.md) | `main.nf`: reads the sample sheet, builds the channels and calls the modules. There is no `workflows` or `subworkflows` folder |
| Settings apart from code | [the tour of features](../../lessons/nextflow-modules/tour-of-nextflow-features.md) | `nextflow.config` and `conf/`; the image tag is a parameter |
| Look at the results | [interactive-computing](../../lessons/interactive-computing/README.md) | `ipynb/`: twelve notebooks that read the results and draw them |
| Run it on a platform | [platforms](../../lessons/platforms/README.md) | the repository README: run it on Lifebit/CloudOS or any Nextflow with a container engine |

### What was changed, and why it helps

1. **The layout follows `sc-nsforest-qc-nf`.** A reader who knows one repository can find their way in the other: `main.nf`, `modules/`, `container/`, `nextflow.config`.
2. **One process in one file, in one container.** A module names its image and calls a script inside it. Nothing is read from `projectDir`, so a module can be copied into another pipeline and still run.
3. **`main.nf` only connects things.** The sample sheet is read, the channels are built and the modules are called. All the work is in the modules.
4. **Every image is tagged by the commit that built it.** The workflow builds the images and the configuration names the tag with `--image_tag`. The README says never to use `latest`. A run can then be repeated with exactly the same software.
5. **Modes are chosen by which parameters you give.** For example, giving the custom GTF and counts files skips S1; giving the S4 files runs the multisample stage alone, from an earlier run.
6. **The sample sheet is read with Nextflow's `file()`.** A sample path can then be an `s3://` path on the platform, and a sheet saved from Excel (with a byte order mark and Windows line endings) is cleaned before it is read.
7. **The results are read, not changed.** The notebooks in `ipynb/` open the S3 and S4 files, and `ipynb/paths.json` is the one place that says where a run is. To look at another run, change that file and nothing else. `review.ipynb` collects the counts, figures and tables into a one-page review with the methods cited.

### Read it in three passes

1. **`README.md`:** the layout, the four stages, the sample sheet and one example command.
2. **`main.nf`:** the header lists the stages and the modes. The `include` lines list every module. Each module is a single `include`.
3. **`modules/lrp2_lite/generate_hashids.nf`:** a typical module. It names its image as `${params.image_registry}/lrp2_lite:${params.image_tag}`, declares inputs and outputs, runs one `Rscript` command, writes a `versions.yml` file of the software versions (25 of the 26 modules do), and has a `stub` block (all 26 do) that makes empty output files so the wiring can be tested in seconds.

## Further reading

- The repository README, for the sample sheet, the parameters, the stages and the notebook table.
- [Nextflow documentation](https://www.nextflow.io/docs/latest/), in particular on `stub` runs and on `container` directives.
- [SQANTI3](https://github.com/ConesaLab/SQANTI3), [CPAT](https://cpat.readthedocs.io/), [LeafCutter](https://davidaknowles.github.io/leafcutter/) and [DRIMSeq](https://bioconductor.org/packages/DRIMSeq/).
- The [sc-nsforest-qc-nf case study](../sc-nsforest-qc-nf/README.md), for the same layout in a second pipeline.

## Supplementary information

### What the lessons do not yet teach

LRP2 uses these practices, and the lessons mention them only briefly or not at all. They are candidates for the next edition.

| Practice | In LRP2 | In the lessons |
|----------|---------|----------------|
| Images tagged by commit, tag passed as a parameter | `docker-publish.yml`, `--image_tag` | taught in [publish an image with GitHub Actions](../../lessons/continuous-integration/publish-an-image-with-actions.md); the [tour](../../lessons/nextflow-modules/tour-of-nextflow-features.md) does not yet pin the tag |
| Many images from one repository | a matrix in `docker-publish.yml` | named in the supplementary section of the same lesson |
| `stub` blocks, to test the wiring without the data | all 26 modules | not taught |
| A `versions.yml` file from each process | 25 of the 26 modules | not taught |
| `task.ext.args` and `label` for settings outside the module | `conf/modules.config`, `label 'process_low'` | the tour shows `withName`; not `ext.args` |
| Modes chosen by parameters | S1 skipped, S4 alone | not taught |
| Reading `s3://` paths and cleaning a sample sheet | `main.nf` | not taught |
| A results viewer: notebooks that read, never write | `ipynb/`, `paths.json` | [interactive-computing](../../lessons/interactive-computing/README.md) teaches notebooks, not this pattern |
| A review notebook with cited methods | `review.ipynb` | not taught |

### How LRP2 differs from the sc-nsforest-qc-nf pattern

The modules in `sc-nsforest-qc-nf` call one `nsforest-cli` command, installed from a Python package. The modules in LRP2 call an R or Python script by its path inside the image, and each script takes its settings as options. Both are valid. The package-and-command route gives one place to document every step. The script route is quicker to start from an existing pipeline.

## References

- Schertzer MD, Lewandowski JT, et al. LRP2: a proteogenomics pipeline for long-read informed protein isoform analysis and discovery. *bioRxiv* 2026. doi: [10.64898/2026.05.27.728216](https://doi.org/10.64898/2026.05.27.728216).
- Miller RM, Jordan BT, Mehlferber MM, et al. Enhanced protein isoform characterization through long-read proteogenomics. *Genome Biology* 2022;23:69. doi: [10.1186/s13059-022-02624-y](https://doi.org/10.1186/s13059-022-02624-y).

> **Check:** both references are copied from the LRP2 README. I confirmed that the 2022 DOI resolves to the Genome Biology paper with that title. I could not confirm the title of the 2026 preprint, because the bioRxiv site refused my request.

## Next

Back to the [case studies](../README.md), or to the [introduction](../../lessons/introduction/README.md) to start again with another pipeline of your own.
