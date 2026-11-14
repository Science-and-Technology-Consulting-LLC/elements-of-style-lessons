# Authenticating on CloudOS

You will install the CloudOS command-line client and sign it in with an API key. This matters because it lets you start and check pipeline jobs from a terminal instead of clicking in the browser.

*Part of the [platforms](README.md) lesson. The client is documented in the [cloudos-cli README](https://github.com/lifebit-ai/cloudos-cli).*

## What you will do

- Get an API key from your CloudOS account.
- Install the `cloudos` client.
- Save your key and settings in a profile with `cloudos configure`.
- Check that the key works by listing your projects.

## What you need

- A CloudOS account and a workspace. See [creating-a-cloudos-account](creating-a-cloudos-account.md) and [logging-into-cloudos](logging-into-cloudos.md).
- [Python](https://www.python.org/) 3.9 or higher, with `pip`. See [conda-environments](../conda-environments/README.md).
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).
- [JupyterLab](https://jupyter.org/) with a Bash kernel. The "Check your setup" section below covers the kernel.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`authenticating-on-cloudos.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/authenticating-on-cloudos.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do Steps 4 and 6 of [Let's dive in](../introduction/lets-dive-in.md) first.

## Step 1. Get an API key

Why: an *API key* is a long secret code that works like a password for programs. The command-line client sends it with every request to prove it is you. Treat it like a password. Never paste it into a notebook cell, a file in a repository or a chat.

> **Check:** where in the platform is the API key created? The step is not written yet. Which menu or page makes it, and does the key show only once?

> **Picture to add:** the CloudOS page where the API key is created (save as assets/authenticating-on-cloudos-step-2.png)

## Step 2. Install the client

Why: `cloudos` is the program you will type. It needs Python 3.9 or higher. `pip` downloads and installs it. The second line asks it for its help page, which proves it is installed.

```bash
pip install cloudos-cli
cloudos --help
```

**What you should see:** `pip` prints lines about downloading and installing, ending in `Successfully installed` with `cloudos-cli` in the list. Then `cloudos --help` prints a usage message and a list of commands such as `configure`, `project`, `workflow` and `job`. If you see `command not found`, see below.

## Step 3. Configure a profile

Why: a *profile* is a saved set of settings. You enter them once and every later command reuses them.

`cloudos configure` asks for your API key, the platform URL, a project name, the execution platform (`aws` is the default), the repository provider, a workflow name (if any) and a session ID for interactive analysis. Run it **in a terminal** (it asks questions, so it cannot run as a notebook cell). Answer each prompt.

The later cells in this page use a profile named `my_profile`, so give your profile that name:

```text
cloudos configure --profile my_profile
```

The answers are saved in your home folder, in `.cloudos/`:

```text
$HOME
└── .cloudos/
    ├── credentials     # the API key
    └── config          # all other settings
```

If you run `cloudos configure` with no name, the profile is called `default`. A name after `--profile` makes a second, named profile.

> **Check:** the original page ran `cloudos configure` first (profile `default`) and only then showed a second, named profile, but every later command uses `--profile my_profile`. Should students create `my_profile` directly, as written here?

**What you should see:** a prompt for each setting, one after the other, with no error at the end.

List the profiles you have:

```bash
cloudos configure list-profiles
```

**What you should see:** a list of profile names that includes `my_profile`.

## Step 4. Check that it works

Why: a table of your projects proves the key is valid and that the client can reach the platform.

```bash
cloudos project list --profile my_profile
```

**What you should see:** a table of the projects in your workspace. That means the key works. An error about authentication or an invalid key means the key or URL in the profile is wrong (see below).

## Step 5. Container images

CloudOS runs the images your modules name. The lessons publish images to GitHub's registry. See [containers](../containers/README.md) and the [Nextflow modules preamble](../nextflow-modules/preamble.md).

## Step 6. Bonus: `pushd` and `popd`

Why: two small shell tools you will use again. `pushd <dir>` remembers where you are, then jumps to `<dir>`. `popd` jumps back. This cell visits the `.cloudos` folder, lists it and returns.

```bash
pushd ~/.cloudos
ls
popd
```

**What you should see:** a list of the files in `.cloudos`, which should include `config` and `credentials`. Then you are back where you started.

## If something goes wrong

- **`pip: command not found`, or `cloudos: command not found` after install.** Run `python3 -m pip install cloudos-cli`, then open a new terminal. Check that your Python is 3.9 or higher with `python3 --version`.
- **`cloudos project list` says the key is invalid or asks for configuration.** The profile name must match. Run `cloudos configure list-profiles` and use that name after `--profile`. If needed, run `cloudos configure --profile my_profile` again.
- **On Windows, `cloudos` is not found.** Use *Git Bash*, and open a new window after installing so the path is refreshed.

## Next

[Running a pipeline on CloudOS](running-a-pipeline-on-cloudos.md): now that you are signed in, run something. Or return to the [platforms lesson](README.md).
