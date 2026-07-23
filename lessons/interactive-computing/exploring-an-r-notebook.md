# Exploring an R notebook

*Companion walkthrough to the [interactive-computing](README.md)
lesson — an R-kernel version of the JupyterLab walkthroughs.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal / RStudio** — copy each R block into `R` or an RStudio
  console; copy shell blocks into your terminal.
- **In the paired notebook** [`exploring-an-r-notebook.ipynb`](../ipynb/exploring-an-r-notebook.ipynb) — every R cell
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


## What this walkthrough is

The other interactive-computing walkthroughs get JupyterLab running with
a Python kernel. This one gets you into an *R* kernel and runs a small
worked example end-to-end.

## Install the R kernel (once)

```bash
conda activate eos-lessons
conda install -c conda-forge r-base r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

`IRkernel::installspec` registers R with Jupyter so the launcher shows
an "R" tile next to "Python 3".

## Open this notebook's R half

In the JupyterLab file browser, open
[`ipynb/exploring-an-r-notebook.ipynb`](exploring-an-r-notebook.ipynb)
(the file you're reading was generated from).

## A tiny worked example

Read a small CSV, summarise, plot:

```r
df <- data.frame(
  sample_id       = c("S01","S02","S03","S04","S05"),
  condition       = c("control","control","treated","treated","treated"),
  reads_millions  = c(42.1, 39.8, 44.6, 41.0, 38.2)
)
df
```

Group means:

```r
aggregate(reads_millions ~ condition, data = df, FUN = mean)
```

A bar chart:

```r
means <- aggregate(reads_millions ~ condition, data = df, FUN = mean)
barplot(means$reads_millions,
        names.arg = means$condition,
        ylab      = "reads (millions)",
        main      = "Mean reads per condition")
```

## Inspect the environment (paste into a bug report)

```r
cat("R:      ", R.version.string, "\n")
cat("Wd:     ", getwd(), "\n")
cat("Sys.locale: ", Sys.getlocale(), "\n")

for (pkg in c("dplyr","ggplot2","DESeq2","edgeR","limma")) {
  ok <- suppressWarnings(requireNamespace(pkg, quietly = TRUE))
  cat(sprintf("%-10s %s\n", pkg,
              if (ok) as.character(packageVersion(pkg)) else "(not installed)"))
}
```

## Try it yourself

Add a sixth sample to `df`, re-run the two summary cells, then do
**Kernel → Restart Kernel and Run All Cells**. If the output is the
same, you have a reproducible R notebook.

## Where to next

→ Back to [interactive-computing](README.md).

→ [`running-a-jupyterlab-notebook.md`](running-a-jupyterlab-notebook.md)
— walking a real R notebook (Wellstein lab's volcano plot).
