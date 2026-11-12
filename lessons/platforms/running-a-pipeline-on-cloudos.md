# Running a pipeline on CloudOS

*Source: [cloudos-cli README](https://github.com/lifebit-ai/cloudos-cli). Part of the [platforms](index.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`running-a-pipeline-on-cloudos.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/running-a-pipeline-on-cloudos.ipynb) — every code cell
  is a shell command executed by the Jupyter **Bash** kernel.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — register the Bash kernel

Only needed if you'll run the paired notebook in JupyterLab. Skip if
you're doing everything in a terminal.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

Restart JupyterLab; the launcher now shows a **Bash** tile.

### Every time — verify the tools this walkthrough uses

The commands below call one or more of these tools. Where a check
fails, the linked lesson has the install instructions.

| Tool | Check | If missing, see |
|---|---|---|
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/index.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/index.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/index.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/index.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/index.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s\n" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING\n" "$cmd"
  fi
done
```

## Prerequisites

- A CloudOS account ([`creating-a-cloudos-account.md`](creating-a-cloudos-account.md)).
- A configured profile ([`authenticating-on-cloudos.md`](authenticating-on-cloudos.md)).
- Your pipeline on GitHub, GitLab or Bitbucket Server. CloudOS runs Nextflow pipelines.

Test the pipeline on your own machine first, with its `-profile test` and
the small test data. Then run it on CloudOS.

## List projects and workflows

```bash
cloudos project list --profile my_profile
cloudos workflow list --profile my_profile
```

## Import a pipeline from GitHub

```bash
cloudos workflow import --profile my_profile \
  --workflow-url "https://github.com/<owner>/<repository>" \
  --workflow-name "<name>" \
  --repository-platform github
```

Importing from the command line is not available in every workspace. If
yours is not set up for it, the client says so, and the import is done in
the platform.

*To fill in: the import steps in the platform.*

## Submit a job

The worked example is `rnatoy`, a small pipeline on public data:

```bash
cloudos job run \
  --profile my_profile \
  --workflow-name rnatoy \
  --parameter reads=s3://lifebit-featured-datasets/pipelines/rnatoy-data \
  --parameter genome=s3://lifebit-featured-datasets/pipelines/rnatoy-data/ggal_1_48850000_49020000.Ggal71.500bpflank.fa \
  --parameter annot=s3://lifebit-featured-datasets/pipelines/rnatoy-data/ggal_1_48850000_49020000.bed.gff \
  --resumable
```

`--parameter` passes one named input. Only jobs started with `--resumable`
can be resumed later. For many parameters, put them in a JSON or YAML file
and pass it with `--params-file`.

## Check the job and get the results

The job ID is printed when the job is submitted.

```bash
cloudos job status --profile my_profile --job-id <JOB_ID>
cloudos job results --profile my_profile --job-id <JOB_ID>
```

`status` prints the state of the job. `results` prints the path where the
platform stores the output files, for jobs that are completed.

## Best practices

- **Daily GitHub commits** of the scripts and configuration you use. The
  worked-example scripts belong in a repository, not only on the platform.
- **Reproducible workflow steps.** Every step containerised, every container
  tagged.
- **Archive derived datasets on Zenodo** (DOI-assignable) so results can be
  cited in a manuscript.

## Where to next

→ Back to the [platforms lesson](index.md).

→ [continuous-integration](../continuous-integration/index.md) — automate
the testing of these pipelines.
