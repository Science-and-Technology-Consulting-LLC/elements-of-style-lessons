# Authenticating on CAVATICA

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-4-workflow-development/authenticating-on-cavatica/)) — woven into
the [platforms](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your **laptop**, in **[Google Cloud Shell](https://shell.cloud.google.com/)** (a free browser-based terminal), or on **[Lifebit CloudOS](https://cloudos.lifebit.ai/)** when the work needs to scale.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`authenticating-on-cavatica.ipynb`](authenticating-on-cavatica.ipynb) — every code cell
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
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/README.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/README.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/README.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/README.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```


## 1. Command-line `docker login`

For pushing images to CAVATICA's built-in registry
`pgc-images.sbgenomics.com`:

```bash
docker login pgc-images.sbgenomics.com -u <USERNAME> -p <YOUR-AUTH-TOKEN>
```

Replace `<USERNAME>` with your CAVATICA login and `<YOUR-AUTH-TOKEN>` with
the developer token. After this, `docker push
pgc-images.sbgenomics.com/<userid>/<image>:<tag>` works from any subsequent
terminal session on the same machine.

## 2. Credential-file authentication (for scripts)

The Seven Bridges Python client and the `sb` CLI read a hidden
`.sevenbridges/credentials` file at the top of your home directory. Create
the directory:

```bash
cd ~
mkdir .sevenbridges
```

Then create `~/.sevenbridges/credentials` (with any text editor)
containing:

```ini
[cavatica]
api_endpoint = https://cavatica-api.sbgenomics.com/v2
auth_token   = <paste your AUTHENTICATION TOKEN here>
```

The `[cavatica]` header names this profile. Multiple profiles can live in
the same file (e.g., `[cavatica]` and `[bpc-sevenbridges]`) — the client
picks between them by name.

## Bonus — `pushd` / `popd`

Two shell commands that are lovely for the account-management dance:
`pushd <dir>` remembers where you are, then jumps to `<dir>`. `popd` jumps
back.

```bash
pushd ~/.sevenbridges
# do a thing…
popd
```

## Where to next

→ [`working-with-apps-on-cavatica.md`](working-with-apps-on-cavatica.md) —
now that you're authenticated, run something.

→ Back to the [platforms lesson](README.md).
