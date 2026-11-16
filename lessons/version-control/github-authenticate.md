# GitHub authentication

You will prove to GitHub who you are, from the terminal. This matters because GitHub accepts your changes only from a signed-in user.

**What you will do:**

- Create a Personal Access Token on the GitHub website.
- Sign in with the [GitHub CLI](https://cli.github.com/) (`gh auth login`).
- Check that you are signed in.

**What you need:**

- A free [GitHub account](https://github.com/signup).
- The `gh` program. Install it with [why-git-and-setup.md](why-git-and-setup.md) (the *Install the GitHub CLI* section).

## Start here

### Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`github-authenticate.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/version-control/github-authenticate.ipynb) and run each cell in order, top to bottom.


### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the six setup steps on the [Introduction page](../introduction/README.md) and the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md) first.

## Steps to execute

### Know why you sign in

To contribute to any GitHub repository, even one you own, you first prove who you are. `gh` does this in one step, but it needs a **Personal Access Token (PAT)**. A PAT is a private secret key that tells GitHub that this computer is acting for you. Treat it like a password: never paste it into a notebook cell, an email or a chat.

`gh` came from the [conda-forge package channel](https://conda-forge.org/), the same source used by `conda install` in the [conda-environments lesson](../conda-environments/README.md). **CLI** means *command-line interface*, a program you control by typing.

**What you should see:** nothing. This step is reading only.

### Create a Personal Access Token

You do this in a web browser, on GitHub's [token page](https://github.com/settings/tokens).

1. Click your **profile picture** (top right), then **Settings**.
2. Scroll to the bottom of the left sidebar and click **Developer settings**.
3. Click **Personal access tokens**, then **Tokens (classic)**.
4. Click **Generate new token**, then **Generate new token (classic)**. In the *Note* box, type a name such as `eos`.
5. Tick the boxes `repo`, `read:org` and `gist`. These are the smallest set that `gh` needs, according to the [gh manual](https://cli.github.com/manual/gh_auth_login).
6. Scroll down and click **Generate token**. **Copy the token now.** GitHub never shows it again. If you lose it, make a new one.

> **Check:** The original steps said "select all the scope options" and "third item from the top". GitHub's menu has changed. Please confirm the current wording and the scopes you want students to tick.

> **Picture to add:** the "New personal access token (classic)" page with the Note box and the three ticked scopes (save as assets/github-authenticate-step-2.png)

**What you should see:** a green banner with a long string that starts with `ghp_`. That string is your token.

### Sign in with `gh auth login`

`gh auth login` asks you questions and waits for your answers, so a notebook cell cannot run it. **Open a terminal and type the command there** (item 2 of Before you begin). The cell below is the same command, for reference.

```bash
gh auth login
```

Answer the questions like this:

1. **What account do you want to log into?** Choose *GitHub.com*. This is usually the default.
2. **What is your preferred protocol for Git operations?** Choose *HTTPS*.
3. **Authenticate Git with your GitHub credentials?** Choose *Yes*.
4. **How would you like to authenticate GitHub CLI?** Choose *Paste an authentication token*, then paste the token you copied.

**What you should see:** a line with a check mark that says you are logged in as your GitHub user name.

> **Picture to add:** the terminal after a successful `gh auth login`, with the check mark line (save as assets/github-authenticate-step-3.png)

### Check that you are signed in

This command reports who `gh` thinks you are. It changes nothing.

```bash
gh auth status
```

**What you should see:** `Logged in to github.com` followed by your user name. If it says you are not logged in, repeat the last step in a terminal.

### If something goes wrong

- **`gh: command not found`.** Activate the environment where you installed it: `conda activate eos`. If `gh` is still missing, run `conda install -c conda-forge gh -y`.
- **The command seems to hang in a notebook cell.** It is waiting for answers you cannot type there. Stop the cell (the square Stop button) and run `gh auth login` in a terminal.
- **"Bad credentials" or a rejected token.** The token was copied wrongly or expired. Make a new token and try again.

## Next

[the-add-push-git-routine.md](the-add-push-git-routine.md): the daily add, commit and push loop.
