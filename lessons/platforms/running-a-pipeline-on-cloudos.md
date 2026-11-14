# Running a pipeline on CloudOS

You will import a pipeline, start a job on CloudOS from your terminal, and fetch the results. This matters because this is how an analysis you tested on a laptop runs on the platform's computers.

*Part of the [platforms](README.md) lesson.*

## What you will do

- List your projects and workflows.
- Import a pipeline from GitHub.
- Submit a small job, `rnatoy`, on public data.
- Check the job and find its results.

## What you need

- A CloudOS account and a signed-in profile named `my_profile`. See [creating-a-cloudos-account](creating-a-cloudos-account.md) and [authenticating-on-cloudos](authenticating-on-cloudos.md).
- The `cloudos` client installed (see the authenticating page).
- Your pipeline on GitHub, GitLab or Bitbucket Server. CloudOS runs [Nextflow](https://www.nextflow.io/) pipelines. See [nextflow-workflows](../nextflow-workflows/README.md).
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`running-a-pipeline-on-cloudos.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/running-a-pipeline-on-cloudos.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do Steps 4 and 6 of [Let's dive in](../introduction/lets-dive-in.md) first.

## Step 1. Test locally first

Why: it is much faster to fix a mistake on your own machine than on the platform. Test the pipeline on your own computer first, with its `-profile test` and the small test data. Then run it on CloudOS.

## Step 2. List your projects and workflows

Why: this confirms your profile works and shows what is already in your workspace.

```bash
cloudos project list --profile my_profile
cloudos workflow list --profile my_profile
```

**What you should see:** two tables. The first lists your projects. The second lists the workflows (pipelines) available to you. An empty second table is normal in a new workspace.

## Step 3. Import a pipeline from GitHub

Why: CloudOS needs its own copy of the pipeline's address before it can run it. Replace `<owner>`, `<repository>` and `<name>` with your own values. This cell will not run as written, because those are placeholders.

```bash
cloudos workflow import --profile my_profile \
  --workflow-url "https://github.com/<owner>/<repository>" \
  --workflow-name "<name>" \
  --repository-platform github
```

**What you should see:** a message that the workflow was imported. Importing from the command line is not available in every workspace. If yours is not set up for it, the client says so, and the import is done in the platform.

> **Check:** what are the import steps in the platform (the part the original page marks "to fill in")?

> **Picture to add:** the platform's import-workflow screen (save as assets/running-a-pipeline-on-cloudos-step-2.png)

## Step 4. Submit a job

Why: this starts the pipeline on the platform's computers. The worked example is `rnatoy`, a small pipeline on public data. `--parameter` passes one named input. `--resumable` lets you resume the job later if it stops.

```bash
cloudos job run \
  --profile my_profile \
  --workflow-name rnatoy \
  --parameter reads=s3://lifebit-featured-datasets/pipelines/rnatoy-data \
  --parameter genome=s3://lifebit-featured-datasets/pipelines/rnatoy-data/ggal_1_48850000_49020000.Ggal71.500bpflank.fa \
  --parameter annot=s3://lifebit-featured-datasets/pipelines/rnatoy-data/ggal_1_48850000_49020000.bed.gff \
  --resumable
```

**What you should see:** a message that the job was submitted, with a *job ID*, the code that names your job. Copy it. Only jobs started with `--resumable` can be resumed. For many parameters, put them in a JSON or YAML file and pass it with `--params-file`.

## Step 5. Check the job and get the results

Why: the job runs on its own. These commands ask how it is doing and where the output went. Replace `<JOB_ID>` with the ID from step 6. This cell will not run as written, because `<JOB_ID>` is a placeholder.

```bash
cloudos job status --profile my_profile --job-id <JOB_ID>
cloudos job results --profile my_profile --job-id <JOB_ID>
```

**What you should see:** `status` prints the state of the job, such as running or completed. `results` prints the path where the platform stores the output files, for jobs that are completed.

> **Picture to add:** the job's page in the platform showing its status and result files (save as assets/running-a-pipeline-on-cloudos-step-4.png)

## Step 6. Best practices

- **Daily GitHub commits** of the scripts and configuration you use. The worked-example scripts belong in a repository, not only on the platform.
- **Reproducible workflow steps.** Every step containerised, every container tagged.
- **Archive derived datasets on [Zenodo](https://zenodo.org/)** (it gives each one a DOI) so results can be cited in a manuscript.

## If something goes wrong

- **A cell fails with `<owner>` or `<JOB_ID>` in the error.** Those are placeholders. Copy the cell into a terminal and put your real values in first.
- **`cloudos: command not found`, or the profile is not found.** Do [authenticating-on-cloudos](authenticating-on-cloudos.md) first and use the same `--profile` name.
- **Import from the command line is refused.** Your workspace may not allow it. Import the pipeline in the platform instead.

## Next

[Continuous integration](../continuous-integration/README.md): automate the testing of these pipelines. Or return to the [platforms lesson](README.md).
