# Authenticating on CloudOS

*Source: [cloudos-cli README](https://github.com/lifebit-ai/cloudos-cli). Part of the [platforms](index.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`authenticating-on-cloudos.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/authenticating-on-cloudos.ipynb) — every code cell
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

## 1. Get an API key

The command-line client needs an API key for your account.

*To fill in: where in the platform the API key is created.*

## 2. Install the client

The client needs Python 3.9 or higher.

```bash
pip install cloudos-cli
cloudos --help
```

## 3. Configure a profile

`cloudos configure` asks for your API key, the platform URL, a project name,
the execution platform (`aws` is the default), the repository provider, a
workflow name (if any), and a session ID for interactive analysis. Run it
once and answer each prompt.

```text
cloudos configure
```

The answers are saved in your home folder, in `.cloudos/`:

```text
$HOME
└── .cloudos/
    ├── credentials     # the API key
    └── config          # all other settings
```

The first profile is called `default`. For a second one, add a name:

```text
cloudos configure --profile my_profile
```

List the profiles you have:

```bash
cloudos configure list-profiles
```

## 4. Check that it works

```bash
cloudos project list --profile my_profile
```

A table of the projects in your workspace means the key works.

## Container images

CloudOS runs the images your modules name. The lessons publish images to
GitHub's registry; see [containers](../containers/index.md) and the
[Nextflow modules preamble](../nextflow-modules/preamble.md).

## Bonus — `pushd` / `popd`

`pushd <dir>` remembers where you are, then jumps to `<dir>`. `popd` jumps
back.

```bash
pushd ~/.cloudos
ls
popd
```

## Where to next

→ [`running-a-pipeline-on-cloudos.md`](running-a-pipeline-on-cloudos.md) — now
that you are authenticated, run something.

→ Back to the [platforms lesson](index.md).
