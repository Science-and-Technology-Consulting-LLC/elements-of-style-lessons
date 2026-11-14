# The add–commit–push routine

You will make one change to a file and send it to GitHub, then offer it to the original project. This is the loop you will repeat every working day.

**What you will do:**

- Copy a project to your computer.
- Edit a file and check what changed with `git status`.
- Save the change with `git add`, `git commit` and `git push`.
- Open a pull request on GitHub.

**What you need:**

- A free [GitHub account](https://github.com/signup), with Git told who you are: [why-git-and-setup.md](why-git-and-setup.md).
- The GitHub CLI signed in: [github-authenticate.md](github-authenticate.md).

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`the-add-push-git-routine.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/version-control/the-add-push-git-routine.ipynb) and run each cell in order, top to bottom.

## Steps

### Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

### Go to your practice folder

You keep practice work in `~/eos-practice`, away from the course files. `~` means your home folder. `mkdir -p` makes the folder if it is not there yet.

```bash
mkdir -p ~/eos-practice
cd ~/eos-practice
pwd
```

**What you should see:** one line ending in `eos-practice`.

### Make a folder with your GitHub user name

This is your own place, so file names never collide with another student's. **Edit the next cell first.** Replace `<your-github-username>`, including the angle brackets, with your real GitHub user name. Run it as written and the shell reports a syntax error.

```bash
mkdir <your-github-username>
cd <your-github-username>
```

**What you should see:** nothing, if it worked. `pwd` should now end with your user name.

### Fork the practice project

A **fork** is your own copy of someone else's project on GitHub. You can change your fork freely. You do this in the browser.

1. Open [NIH-NICHD/exampleVolcanoPlotNotebook](https://github.com/NIH-NICHD/exampleVolcanoPlotNotebook).
2. Click **Fork** at the top right.
3. Choose your own account as the owner, then click **Create fork**.

> **Picture to add:** the Fork button at the top right of the repository page (save as assets/the-add-push-git-routine-step-3.png)

**What you should see:** the page changes to `<your-github-username>/exampleVolcanoPlotNotebook`, with a line "forked from NIH-NICHD/exampleVolcanoPlotNotebook". There is more about forks in [keeping-your-repository-fork-in-sync.md](keeping-your-repository-fork-in-sync.md).

### Clone your fork

To **clone** is to copy a GitHub project onto your computer. **Edit the next cell first**: replace `<your-github-username>` in the web address with your own.

```bash
git clone https://github.com/<your-github-username>/exampleVolcanoPlotNotebook.git
cd exampleVolcanoPlotNotebook
```

**What you should see:** lines such as `Cloning into 'exampleVolcanoPlotNotebook'...` and `Receiving objects: 100%`, ending with `done.`. List the files with `ls` if you like: you should find `README.md`, `Reading-data-and-plotting-in-R.ipynb` and `install_dependencies.R`.

### Run `git status`

`git status` tells you what changed in your local copy since the last commit (the last saved snapshot). You will use it every day.

```bash
git status
```

**What you should see:** when nothing has changed:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Edit a file

Add one line to `README.md`: `Learn about Zenodo here: https://zenodo.org`. Use one of these two ways.

- **In a terminal:** run `nano README.md`, type the line, press `Ctrl-O` then `Enter` to save, and `Ctrl-X` to exit.
- **In a notebook:** run the next cell. It adds the same line to the end of the file.

```bash
echo "Learn about Zenodo here: https://zenodo.org" >> README.md
```

Check that the file has the change. `head` shows the top of the file. `tail` shows the end, where the notebook cell put the new line.

```bash
head README.md
```

```bash
tail -n 3 README.md
```

**What you should see:** the line `Learn about Zenodo here: https://zenodo.org` in one of the two outputs, depending on where you put it.

### Run `git status` again

```bash
git status
```

**What you should see:** Git now lists the file as changed:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   README.md

no changes added to commit (use "git add" to update)
```

### Stage the change with `git add`

`git add` moves the change from "unstaged" to "staged", which means it is chosen for the next commit.

```bash
git add README.md
```

**What you should see:** nothing. Run `git status` and the file now appears under "Changes to be committed".

### Save it locally with `git commit`

A **commit message** is a note to your future self about what changed and why. Write it in the present tense, short and specific.

```bash
git commit -m 'added Zenodo pointer to README'
```

**What you should see:** a line with a short code and your message, then a count of changes:

```
[main 1a2b3c4] added Zenodo pointer to README
 1 file changed, 1 insertion(+)
```

(The short code will differ.)

### Send it to GitHub with `git push`

`git push` uploads your commits from your computer to your fork on GitHub. It uses the sign-in you made in [github-authenticate.md](github-authenticate.md).

```bash
git push
```

**What you should see:** lines about counting and writing objects, ending with `main -> main`. Refresh your fork's page on GitHub: it shows your commit message next to `README.md`.

### Confirm all is quiet

```bash
git status
```

**What you should see:**

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Open a pull request

A **pull request** (PR) asks the owner of the original project to take your change. You do this in the browser.

1. Open your fork's page on GitHub.
2. GitHub shows a banner that says your branch is "1 commit ahead of" the original.
3. Click **Contribute**, then **Open pull request**.
4. Write a short description of what you changed.
5. Click **Create pull request**.

> **Picture to add:** the Contribute menu with Open pull request, on your fork's page (save as assets/the-add-push-git-routine-step-12.png)

**What you should see:** a new page for your pull request. The original owner can now accept it, comment, or ask for changes.

## Recap

You walked the whole loop:

- Cloned a fork.
- Edited a file.
- Inspected with `git status`.
- Staged with `git add`.
- Saved a snapshot with `git commit`.
- Sent it up with `git push`.
- Offered it to the original project as a pull request.

## If something goes wrong

- **`Author identity unknown` when you commit.** Git does not know your name yet. Set it as in [why-git-and-setup.md](why-git-and-setup.md) (the *Tell Git who you are* section), then commit again.
- **`Permission denied` or "could not read Username" when you push.** Either you cloned the original project instead of your fork, or you are not signed in. Check the clone address has your user name in it, and run `gh auth status`.
- **`syntax error near unexpected token` in the commands that contain `<your-github-username>`.** You left `<your-github-username>` as it was. Replace it with your user name, angle brackets included.
- **`destination path already exists` when you clone.** You already cloned it. Run `cd exampleVolcanoPlotNotebook` instead.

## Next

[keeping-your-repository-fork-in-sync.md](keeping-your-repository-fork-in-sync.md): catch your fork up when the original moves ahead.
