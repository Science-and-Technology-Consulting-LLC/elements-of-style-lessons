# Platforms: a transport layer for science as a service

*In the book: Section 6.6, Workflows on Cloud Platforms.*

Pipelines have to run somewhere. This lesson covers where, and walks you through creating accounts on CloudOS (Lifebit) and the Kids First and INCLUDE data hubs, then running a pipeline from a terminal.

## Before you start

Do [publishing-for-agents](../publishing-for-agents/README.md) first. The accounts pages need no earlier lesson.

## Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/platforms/creating-a-cloudos-account.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/creating-a-cloudos-account.ipynb)) and run each cell in order, top to bottom. The first page needs no kernel. The later ones are Bash notebooks (each has a *Check your setup* section for it).

## What you should see

You sign up for CloudOS with your institutional login, sign in, create a workspace, open JupyterLab, save an API key with `cloudos configure` and submit a small job. Each page says what the screen or output should look like.

> **Picture to add:** the CloudOS home page after the first sign-in (save a screenshot of the signed-in page) (save as assets/overview.png)

## Where the files are

- `lessons/platforms/pre-training-creating-kids-first-and-other-accounts.ipynb` and `.md`: Kids First and INCLUDE accounts.
- `lessons/platforms/creating-a-cloudos-account.ipynb` and `.md`: sign up.
- `lessons/platforms/logging-into-cloudos.ipynb` and `.md`: sign in and open JupyterLab.
- `lessons/platforms/authenticating-on-cloudos.ipynb` and `.md`: API key and `cloudos configure`.
- `lessons/platforms/running-a-pipeline-on-cloudos.ipynb` and `.md`: import, submit, check, get results.
- `lessons/platforms/assets/`: pictures for this lesson.

## Notebooks in order

1. [`pre-training-creating-kids-first-and-other-accounts.md`](pre-training-creating-kids-first-and-other-accounts.md) — create Kids First and INCLUDE accounts (before the course starts)
2. [`creating-a-cloudos-account.md`](creating-a-cloudos-account.md) — sign up for CloudOS with institutional login
3. [`logging-into-cloudos.md`](logging-into-cloudos.md) — sign in, create a workspace and open JupyterLab
4. [`authenticating-on-cloudos.md`](authenticating-on-cloudos.md) — get an API key and run `cloudos configure`
5. [`running-a-pipeline-on-cloudos.md`](running-a-pipeline-on-cloudos.md) — import a pipeline from GitHub, submit a job, check it and get results
6. [`pre-training-creating-kids-first-and-other-accounts.md`](pre-training-creating-kids-first-and-other-accounts.md) — create Kids First and INCLUDE accounts (extra: do it before the course starts)

## Next

[Introduction](../introduction/README.md): back to the start of the course, or browse the book chapters for full worked examples.

## Background

### The framing

**Lifebit offers a transport-layer protocol for science as a service.** The internet has HTTP. Science is converging on a similar layer that delivers compute, data and provenance on demand, with institutional login. Combined with the [MCP server](../mcp-server/README.md) pattern, an assistant drives the CLI, the CLI runs on the transport layer, and results return to the researcher's chat.

### The platforms covered

**Lifebit, the open-science transport layer (headline).**

- Free with **institutional login**, a real on-ramp for academic and research labs.
- Runs Nextflow natively, so your `nextflow/` lessons work as they are.
- Provides federated execution. Your [federated-computing](../federated-computing/README.md) lesson lands here.

**All of Us Researcher Workbench.**

- About a million participants' population data lives here.
- R and Nextflow are supported. A direct `git pull` is not.
- The bridge patterns section of the book is written for that limit.

> **Check:** the earlier page linked to `../../bridges/index.md`, which does not exist in this repository. Where should the bridge patterns link go?

**NIH HPC (Biowulf), a different category.** Biowulf is a SLURM-managed high-performance computing cluster. You log in with SSH, write batch scripts and submit them to the queue. It suits very large or GPU-heavy jobs. It has no built-in data federation or agent surface, so do not group it with the cloud platforms.

### Get on Lifebit

- Sign up: <https://cloudos.lifebit.ai/register>
- Sign in: <https://cloudos.lifebit.ai/login>
- Institutional access requests: <https://lifebit.ai/contact> (if your institution's sign-in is not listed)

From a browser: sign up, choose *Sign in with institutional login*, pick your institution, create a workspace with the *biomedical analysis* template and open its JupyterLab. From your laptop's terminal:

```bash
pip install cloudos-cli
cloudos configure   # asks for your API key; see authenticating-on-cloudos.md
```

### Pairs well with

Platforms close the loop. Every CLI, container and Nextflow module you built runs on one of these platforms, and the [MCP server](../mcp-server/README.md) lesson makes them drivable by an assistant.

### Further reading

- Scheuermann RH, Deslattes Mays A, Diller M, LeClair R, Spear W, Zhang Y. *A trustworthy data-driven biomedical knowledge base of cell phenotypes for the National Library of Medicine.* In **Knowledge Graphs in U.S. Government Agencies**. Springer, forthcoming. The reference frame for the [NLM-CKN](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/nlm-ckn/README.md) case study.
- [Lifebit](https://lifebit.ai/): federated computing platform
- [All of Us Researcher Workbench](https://www.researchallofus.org/data-tools/workbench/)
- [Biowulf](https://hpc.nih.gov/): NIH high-performance computing
- [Terra](https://terra.bio/): Broad Institute genomics platform
- [DNAnexus](https://www.dnanexus.com/): commercial platform
