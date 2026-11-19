# Exploring an R notebook

You will run a small R notebook that builds a table, summarises it and draws a bar chart. This matters because it proves your R kernel works before you try real data.

**What you will do:**

- Make sure R is registered with Jupyter.
- Check which tools this notebook can see.
- Build a small table, summarise it, plot it.
- Print your environment so you can paste it into a bug report.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Reproducible environments with Conda](../conda-environments/README.md), is done.
- JupyterLab is running: [starting-a-jupyter-lab-notebook.md](starting-a-jupyter-lab-notebook.md).
- The kernel name at the top right of this notebook says **R**. If it does not, click the name and choose **R**.

This is the R companion to the other [interactive-computing](README.md) walkthroughs. A kernel is the engine that runs your code, as [Let's dive in](../introduction/lets-dive-in.md) shows.

## Steps to execute

### Register the R kernel (only if there is no R tile)

[IRkernel](https://irkernel.github.io/) lets Jupyter run R. The Introduction already installed R in the `eos` environment and registered it (step 4). If the Launcher shows an *R* tile, skip this step.

If it does not, run these three lines in a **terminal**, not in a notebook cell. The first turns on the `eos` environment (or use any environment you keep for R). The second installs R and IRkernel from [conda-forge](https://conda-forge.org/). The third registers R with Jupyter.

```bash
conda activate eos        # or any env dedicated to R work
conda install -c conda-forge r-base=4.4 r-irkernel -y
R -e 'IRkernel::installspec(name="ir", displayname="R")'
```

Restart JupyterLab, then reopen this notebook and choose the *R* kernel.

**What you should see:** conda ends with `Executing transaction: done`. The last command prints a line that says the kernel spec was installed. After a restart, the Launcher has an *R* tile.

> **Picture to add:** the JupyterLab Launcher with the Python 3, Bash and R tiles (save as assets/exploring-an-r-notebook-step-1.png)

### Check which tools this notebook can see

This R cell asks the computer where each of five programs lives. It prints the location, or `MISSING`.

```r
for (cmd in c("R", "Rscript", "git", "podman", "conda")) {
  where <- Sys.which(cmd)
  cat(sprintf("  %-10s %s\n", cmd,
              ifelse(nchar(where) > 0, where, "MISSING")))
}
```

**What you should see:** one line per tool. The paths on your computer will differ:

```
  R          /Users/you/miniforge3/envs/eos/bin/R
  Rscript    /Users/you/miniforge3/envs/eos/bin/Rscript
  git        /usr/bin/git
  podman     /usr/local/bin/podman
  conda      /Users/you/miniforge3/bin/conda
```

`MISSING` is fine for `podman` at this stage. This notebook needs only `R`.

### Build a small table

A **data frame** is a table with rows and columns. The next cell makes one by hand. It holds five samples, their condition, and the millions of sequence reads each produced. Writing the last line, `df`, makes the notebook show the table.

```r
df <- data.frame(
  sample_id       = c("S01","S02","S03","S04","S05"),
  condition       = c("control","control","treated","treated","treated"),
  reads_millions  = c(42.1, 39.8, 44.6, 41.0, 38.2)
)
df
```

**What you should see:** a table with three columns, `sample_id`, `condition` and `reads_millions`, and five rows `S01` to `S05`:

```
  sample_id condition reads_millions
1 S01       control   42.1
2 S02       control   39.8
3 S03       treated   44.6
4 S04       treated   41.0
5 S05       treated   38.2
```

### Average the reads for each condition

`aggregate` splits the table by `condition` and takes the mean of `reads_millions` in each group.

```r
aggregate(reads_millions ~ condition, data = df, FUN = mean)
```

**What you should see:**

```
  condition reads_millions
1   control       40.95000
2   treated       41.26667
```

### Draw a bar chart

`barplot` draws one bar for each condition.

```r
means <- aggregate(reads_millions ~ condition, data = df, FUN = mean)
barplot(means$reads_millions,
        names.arg = means$condition,
        ylab      = "reads (millions)",
        main      = "Mean reads per condition")
```

**What you should see:** a small chart titled "Mean reads per condition", with two bars labelled `control` and `treated` and the vertical axis labelled "reads (millions)". The bars are nearly the same height, about 41.

> **Picture to add:** the bar chart under the cell, with two bars (save as assets/exploring-an-r-notebook-step-5.png)

### Print your environment

When a notebook stops working months from now, the first thing you will want is the answer to "what was I running?" This cell prints R's version, your folder, your locale (language and region settings), and the version of five R packages. Save its output and paste it into a bug report.

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

**What you should see:** lines like these. Your versions will differ, and a package you have not installed shows `(not installed)`:

```
R:       R version 4.4.3 (2025-02-28)
Wd:      /Users/you/elements-of-style-lessons/lessons/interactive-computing
Sys.locale:  en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8
dplyr      1.2.1
ggplot2    4.0.3
DESeq2     (not installed)
edgeR      4.4.0
limma      3.62.1
```

### Try it yourself

Add a sixth sample to `df`, run the two summary cells again, then choose **Kernel**, then **Restart Kernel and Run All Cells**. If the output is the same as before (apart from your new sample), you have a reproducible R notebook.

### If something goes wrong

- **The kernel says "R" is not found, or there is no R tile.** R is not registered in the environment that runs JupyterLab. Do *Register the R kernel (only if there is no R tile)*, then restart JupyterLab.
- **`conda: command not found`.** See the [Introduction page](../introduction/README.md).
- **`DESeq2 (not installed)`.** This is expected. It is a larger Bioconductor package that you install later when a lesson needs it.

## Next

[running-a-jupyterlab-notebook.md](running-a-jupyterlab-notebook.md): run a real R notebook from GitHub. Or go back to the [interactive-computing lesson](README.md).
