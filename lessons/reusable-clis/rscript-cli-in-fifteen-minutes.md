# An Rscript CLI in fifteen minutes

*Companion walkthrough to the [reusable-clis](README.md) lesson — the
R sibling of [`typer-cli-in-fifteen-minutes`](typer-cli-in-fifteen-minutes.md).*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal / RStudio** — copy each R block into `R` or an RStudio
  console; copy shell blocks into your terminal.
- **In the paired notebook** [`rscript-cli-in-fifteen-minutes.ipynb`](rscript-cli-in-fifteen-minutes.ipynb) — every R cell
  is executed by the Jupyter **R (IRkernel)** kernel. Run the shell
  blocks in a terminal FIRST to install R + IRkernel; then pick the R
  kernel when you open the notebook.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — install R and register IRkernel

```bash
conda activate eos-lessons        # or any env dedicated to R work
conda install -c conda-forge r-base r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Restart JupyterLab; the launcher now shows an **R** tile.

### Every time — verify R can see its tools

```r
for (cmd in c("R", "Rscript", "git", "docker", "conda")) {
  where <- Sys.which(cmd)
  cat(sprintf("  %-10s %s
", cmd,
              ifelse(nchar(where) > 0, where, "MISSING")))
}
```


## What we build

A single Rscript-based CLI, `hello-r`, with two verbs — `greet` and
`version` — using [`docopt`](https://github.com/docopt/docopt.R) to parse
arguments. The same shape as the Typer / Python one, applied to R.

## Create a project folder

```bash
mkdir hello-r-cli && cd hello-r-cli
```

## Install `docopt` (once)

```r
install.packages("docopt", repos = "https://cloud.r-project.org")
```

## Write the CLI — one file

Create `hello-r.R`:

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

Make it executable and run it:

```bash
chmod +x hello-r.R
./hello-r.R greet --name Annie
./hello-r.R version
./hello-r.R --help
```

## Make it installable — an R package with `inst/scripts/`

The
[`NIH-NLM/sc-nsforest-qc-nf`](https://github.com/NIH-NLM/sc-nsforest-qc-nf)
pattern splits R work into a package (`R/*.R` — pure functions, testable
from a notebook) plus an Rscript entry point (`inst/scripts/hello-r` —
parses argv with `docopt`, calls the R function).

`R/greet.R`:

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

`inst/scripts/hello-r`:

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

The function `greet()` is now importable from any R code (a notebook, a
test); the Rscript is callable from the shell, from Nextflow's `script:`
block, and from an AI agent through MCP.

## Why this shape

- Same *one job, one CLI verb* rule as the Typer/Python walkthrough.
- Same Nextflow-module wrap-shape: one `.nf` per CLI verb, container
  from [containers](../containers/README.md) supplies R + docopt +
  package.

## Where to next

→ Back to [reusable-clis](README.md).

→ [`building-an-r-dockerfile.md`](../containers/building-an-r-dockerfile.md)
— wrap this CLI in an R container.
