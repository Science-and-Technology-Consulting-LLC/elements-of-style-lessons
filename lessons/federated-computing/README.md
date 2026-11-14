# Federated computing

*In the book: Section 10.2.1, Federated Computing: Compute Travels to Data.*

*Federated computing* means running the same workflow on data that lives in different places, without moving the data. This lesson gives you the picture and a small simulation you can run yourself. The compute travels to the data. The results travel back.

## Before you start

Do [continuous integration](../continuous-integration/README.md) first.

## Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/federated-computing/simulating-a-3x3-federated-run.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/federated-computing/simulating-a-3x3-federated-run.ipynb)) and run each cell in order, top to bottom. This notebook uses a Python kernel. Its first two sections make a conda environment.

## What you should see

You make three fake sites, train a simple model at each, and combine the three sets of coefficients with a median. You finish with a `global:` line of three numbers close to 1.5, -2.0 and 0.3. The raw data never leaves the site folders.

> **Picture to add:** the notebook's output after the median step, showing the three site lines and the global line (save a screenshot of the finished run) (save as assets/overview.png)

## Where the files are

- `lessons/federated-computing/simulating-a-3x3-federated-run.ipynb` and `.md`: the simulation.
- `lessons/federated-computing/sites/`: created when you run it. One folder per site, each with `train.csv` and `model.json`.
- `lessons/federated-computing/global_model.json`: the combined model.
- `lessons/federated-computing/assets/`: pictures for this lesson.
- [`case-studies/oadr-autoantibody`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/oadr-autoantibody/README.md): the full real-world version.

## Notebooks in order

1. [`simulating-a-3x3-federated-run.md`](simulating-a-3x3-federated-run.md) — simulate three sites and a median coordinator

## Next

[Federated learning](../federated-learning/README.md): the case where the per-site phase is training a model.

## Background

### Why this matters for NLM-CKN

Single-cell atlases are increasingly federated. One study's data lives at JAX, another at the Broad, a third in the All of Us Workbench. A federated workflow lets you ask one question across all three without bulk data transfers, and without breaking the data-use agreement that says the data cannot leave its institution.

### What this lesson teaches

1. A clear picture of "compute travels to data" that you can explain to a colleague in one minute.
2. How to tell when a problem fits federation and when it does not.
3. How to read a federated workflow and find the *coordinator* and the *per-site* phases.
4. The trust, audit and provenance limits that come with federation.

### The shape of a federated computation

1. **Per-site phase.** Each institution runs the same code on its own data, locally. Only small, agreed summaries leave: statistics, model parameters or non-identifying metadata.
2. **Coordinator phase.** A central process combines the per-site outputs. It can be as simple as "take the median of what each site returned".

Everything else is engineering. The hard parts are agreeing on what summary leaves each site, and trusting that each site ran the code you think it ran.

### The platform: ADAPTS on Lifebit's federated fabric

The worked example below runs on **ADAPTS** (Autoimmune Disease Analysis Platform Testing Space), an NIH initiative led by NHLBI/CC, NHLBI, NIAMS and NIAID, with NIEHS, NIDCR, NINR, NINDS and NHGRI collaborating. ADAPTS runs on **Lifebit's federated computing fabric**, the transport layer that lets each institution train on its own data and share only model parameters with a coordinator. See [platforms](../platforms/README.md).

### The worked example: `oadr-autoantibody`

[Science-and-Technology-Consulting-LLC/oadr-autoantibody](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody) predicts residual beta-cell function in Type 1 Diabetes, under federation.

> Type 1 Diabetes is an autoimmune disease in which the immune system destroys the insulin-producing beta cells of the pancreas. How many beta cells remain is read from the **C-peptide AUC** during a four-hour mixed-meal tolerance test. The autoantibody panel (GAD65, IA-2, Insulin, ICA, ZnT8) is the immune signature of the attack. The question is how well the autoantibody profile predicts the beta-cell function that survives.

Each of four cohorts (**SDY524, SDY569, SDY797, SDY1737**) comes from a different study with its own data-use rules. The data cannot move. The sites can share model parameters, and a coordinator takes the median across sites.

Three headline findings:

1. **More institutions, lower error.** Simple linear regression's error falls from 1.03 (average of the four solo runs) to 0.33 at four institutions, with no site gaining subjects.
2. **More rounds help until a plateau.** Re-running the federation, starting from the last round's combined parameters, lowers error further until the gain is small.
3. **Federation lifts the cohort-size ceiling.** The smallest cohort, SDY569 with N = 10, cannot fit a 9-feature regression alone. Stacked, the federation reaches N = 150.

Four notebooks worth opening in that repository:

- [`federated_analysis_simulation_3x3.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/federated_analysis_simulation_3x3.ipynb): the end-to-end federated story. Open it first and read the section headers and figures.
- [`LinearRegression_vs_CNN_HeadToHead.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/LinearRegression_vs_CNN_HeadToHead.ipynb): the centralised baseline.
- [`LASSO_ElasticNet_Autoantibody_CPeptide.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/LASSO_ElasticNet_Autoantibody_CPeptide.ipynb): the interpretable linear version.
- [`EffectSizes_and_PowerAnalysis_Extended.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/EffectSizes_and_PowerAnalysis_Extended.ipynb): the power argument for federation.

On Lifebit, in the oadr-autoantibody workspace, run `jupyter notebook federated_analysis_simulation_3x3.ipynb`. It takes 30 to 60 minutes from cold. Results are cached, so re-renders take seconds.

### Pairs well with

- [Nextflow](../nextflow-workflows/README.md): one pipeline, many environments.
- [Platforms](../platforms/README.md): Lifebit and others provide the federation transport.
- [Federated learning](../federated-learning/README.md): the case where the per-site phase is training a model.

### Honest constraints

1. **Trust.** You trust each site to run the agreed code on the agreed data and return only the agreed summary. This is a governance problem, not a technical one.
2. **Audit.** The provenance trail must survive across sites: which site contributed which subjects, with which code version, when.
3. **Privacy is not automatic.** "The data did not leave" is not "nothing about an individual leaked". Model parameters can leak training information in some attacks. Differential privacy and secure aggregation go further.

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. The reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [Lifebit Federated Data and Learning Fabric](https://lifebit.ai/products/federated-fabric)
- [Kairouz et al., Advances and Open Problems in Federated Learning (2019)](https://arxiv.org/abs/1912.04977)
- [oadr-autoantibody repository](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody)
- [NIH ADAPTS overview](https://www.nih.gov/)
