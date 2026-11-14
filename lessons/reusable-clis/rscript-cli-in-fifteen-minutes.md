# An Rscript CLI in fifteen minutes

You will build a small command-line tool in R that prints its own help screen, so that you, a teammate or a workflow can run your R code without opening R. This is the R version of the [Typer walkthrough](typer-cli-in-fifteen-minutes.md).

**What you will do:**

- Set up R and its Jupyter kernel.
- Write a two-command tool, `hello-r`, that reads its options with [docopt](https://github.com/docopt/docopt.R).
- See how the same tool splits into a testable R function and a thin command-line script.

**What you need:**

- A terminal. See [the command line and Git Bash](../command-line-and-git-bash/README.md).
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) and the `eos` environment from [conda environments](../conda-environments/README.md).
- [R](https://www.r-project.org/) (*Install R and register the R kernel (once)* installs it with conda) and [JupyterLab](https://jupyter.org/install).
- A plain text editor. JupyterLab has one: choose *File*, then *New*, then *Text File*.

You do not need an account for this lesson.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`rscript-cli-in-fifteen-minutes.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/reusable-clis/rscript-cli-in-fifteen-minutes.ipynb) and run each cell in order, top to bottom.

> **Where to type the commands.** The command boxes marked `bash` run in your **terminal**. The boxes with a *Run the next cell* instruction are notebook cells that use the R kernel. Keep your terminal open next to this page.

## Install R and register the R kernel (once)

*Why:* a **kernel** is the program that runs the code in a notebook cell. JupyterLab needs the R kernel, called IRkernel, before it can run R cells.

In your terminal, run:

```bash
conda activate eos        # or any env dedicated to R work
conda install -c conda-forge r-base r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

**What you should see:** conda installs `r-base` and `r-irkernel` without an error. The last command prints a line that ends with `Installed kernelspec ir`.

Restart JupyterLab. The Launcher now shows an **R** tile. Open this notebook with the R kernel.

> **Picture to add:** the JupyterLab Launcher with the R tile visible (save as assets/rscript-cli-step-1.png)

## Check that R can see its tools

*Why:* this cell finds each program and prints where it lives, or `MISSING`. `docker` and `conda` are not used in the steps below, so `MISSING` for them is fine today.

Run the next cell.

```r
for (cmd in c("R", "Rscript", "git", "docker", "conda")) {
  where <- Sys.which(cmd)
  cat(sprintf("  %-10s %s
", cmd,
              ifelse(nchar(where) > 0, where, "MISSING")))
}
```

**What you should see:** one line per program, each with a path, for example:

```text
  R          /.../envs/eos/bin/R
  Rscript    /.../envs/eos/bin/Rscript
  git        /.../envs/eos/bin/git
  docker     /usr/local/bin/docker
  conda      /Users/you/miniforge3/bin/conda
```

`R` and `Rscript` must not say `MISSING`.

## What we build

A single R command, `hello-r`, with two commands, `greet` and `version`. It uses [`docopt`](https://github.com/docopt/docopt.R) to read what you type. The shape matches the Typer tool in the Python walkthrough.

## Create a project folder

*Why:* all the files for this tool should live together in one new folder.

In your terminal, run:

```bash
mkdir hello-r-cli && cd hello-r-cli
pwd
```

**What you should see:** a path that ends in `hello-r-cli`. Keep this terminal open. You will use it again in *Write the tool as one script*.

## Install `docopt` (once)

*Why:* `docopt` reads a usage message written in plain text and turns it into the options your script receives. It saves you writing argument-parsing code. `install.packages` is R's installer for packages.

Run the next cell.

```r
install.packages("docopt", repos = "https://cloud.r-project.org")
```

**What you should see:** R downloads and installs the package. The output ends with lines like `Updating HTML index of packages in '.Library'`, `Making 'packages.html' ... done`. If `docopt` is already installed, R reinstalls it and prints the same lines.

## Write the tool as one script

*Why:* the usage message at the top is the help screen and the instructions for `docopt` at the same time. A **script** is a plain text file of R code that you can run from the terminal.

Create a file named `hello-r.R` inside the `hello-r-cli` folder. In JupyterLab, open the `hello-r-cli` folder in the file browser, choose *New*, then *Text File*, and rename it `hello-r.R`. Or run `nano hello-r.R` in your terminal. Paste this text into the file. This is a file, not a notebook cell: do not run it in the notebook.

```r
#!/usr/bin/env Rscript
"hello-r — a tiny R CLI.

Usage:
  hello-r greet [--name=<name>]
  hello-r version

Options:
  --name=<name>  Who to greet [default: world].
" -> doc

library(docopt)
args <- docopt(doc)

if (isTRUE(args$greet)) {
  cat(sprintf("Hello, %s!\n", args[["--name"]]))
} else if (isTRUE(args$version)) {
  cat("hello-r 0.1.0\n")
}
```

Save the file. Then, in your terminal (inside `hello-r-cli`), make it executable and run it. **Executable** means the system may run the file as a program.

```bash
chmod +x hello-r.R
./hello-r.R greet --name Annie
./hello-r.R version
./hello-r.R --help
```

**What you should see:** `Hello, Annie!`, then `hello-r 0.1.0`, then a help screen that shows the usage text you wrote: the `greet` and `version` lines and the `--name=<name>` option with `[default: world]`.

> **Picture to add:** the terminal showing the three commands and their output (save as assets/rscript-cli-step-5.png)

## Put the logic in an R function

*Why:* a function in its own file can be tested from a notebook, and the command-line script only has to call it. The
[`NIH-NLM/sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf)
project splits R work this way: a package of pure functions in `R/*.R`, plus an Rscript entry point in `inst/scripts/hello-r` that reads the command line with `docopt` and calls the function.

This is the content of `R/greet.R`. Run the next cell to define the function in your notebook session.

```r
#' Greet someone by name
#'
#' @param name Character. Who to greet.
#' @return Character.
#' @export
greet <- function(name = "world") {
  sprintf("Hello, %s!", name)
}
```

Now call it. Run the next cell.

```r
greet("Annie")
```

**What you should see:**

```text
[1] "Hello, Annie!"
```

The cell that defined `greet` prints nothing. That is normal: it only stores the function.

## Read the thin command-line script

*Why:* this is what `inst/scripts/hello-r` looks like once the logic lives in a package. Read it; do not run it yet.

```r
#!/usr/bin/env Rscript
"hello-r — a tiny R CLI.

Usage:
  hello-r greet [--name=<name>]
  hello-r version

Options:
  --name=<name>  Who to greet [default: world].
" -> doc

library(docopt)
library(hello.r)      # your package

args <- docopt(doc)
if (isTRUE(args$greet))   cat(greet(args[["--name"]]), "\n")
if (isTRUE(args$version)) cat("hello-r 0.1.0\n")
```

> **Check:** This script calls `library(hello.r)`, but the walkthrough never builds the `hello.r` package (there is no `DESCRIPTION` or `NAMESPACE` file). Should the lesson add those steps, or point to the `sc-nsforest-qc-nf` package as the model to copy?

The function `greet()` can now be used from any R code (a notebook, a test). The script runs from the shell, from a Nextflow `script:` block, and from an AI agent through MCP.

## Why this shape

- It follows the same *one job, one CLI command* rule as the Typer walkthrough.
- It wraps into a Nextflow module the same way: one `.nf` file per CLI command, with a container from [containers](../containers/README.md) that supplies R, `docopt` and your package.

## If something goes wrong

- **`Rscript: command not found`, or `R` shows `MISSING` in *Check that R can see its tools*.** The environment with R is not active. Run `conda activate eos`, start JupyterLab again from that terminal, and repeat *Check that R can see its tools*.
- **`Permission denied` when you run `./hello-r.R`.** Run `chmod +x hello-r.R` first. On Windows Git Bash, if the script still will not start, run `Rscript hello-r.R greet --name Annie` instead.
- **`there is no package called 'docopt'`.** *Install `docopt` (once)* did not finish. Run the *Install `docopt` (once)* cell again and read its last lines for an error. You also need an internet connection.

## Next

Put this tool in a container: [building an R Dockerfile](../containers/building-an-r-dockerfile.md). Or go back to the [reusable CLIs lesson](README.md).
