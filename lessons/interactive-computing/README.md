# Interactive computing with Jupyter

> *In the book: Section 3.8, Interactive Computing with JupyterLab.*

This lesson gives you a working picture of a Jupyter notebook, and two short starter notebooks (Python and R) that you can edit, rerun and reuse as templates.

## Start here

### Before you start

The previous lesson is [Reproducible environments with Conda](../conda-environments/README.md). You need the `eos` environment.

### Do this

1. **Clone the course.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Start JupyterLab and open the first notebook.** In the terminal run `conda activate eos`, then `jupyter lab`. In JupyterLab open `lessons/interactive-computing/starting-a-jupyter-lab-notebook.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/interactive-computing/starting-a-jupyter-lab-notebook.ipynb)). On Lifebit, JupyterLab is already running, so skip `jupyter lab` and open the notebook from the file browser.

### What you should see

- JupyterLab in your browser, with a file browser on the left, a Launcher in the middle, and a menu bar across the top.
- A Launcher with tiles for *Python 3*, *Bash*, *R* and *Terminal*.
- Each starter notebook printing a small table, a bar chart of mean reads per condition (control about 40.95, treated about 41.27), and a print-out of your software versions.
- A notebook that gives the same output after **Kernel**, then **Restart Kernel and Run All Cells**.

> **Picture to add:** JupyterLab with the file browser, the Launcher tiles and the menu bar (save as assets/overview.png)

### Where the files are

Everything is in `lessons/interactive-computing/` of the [course repository](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/tree/main/lessons/interactive-computing). Each walkthrough is a notebook (`.ipynb`) with a web page copy (`.md`). The two starter notebooks are `python.ipynb` and `r.ipynb` only.

## Steps to execute

Work through the notebooks in this order:

1. [starting-a-jupyter-lab-notebook.md](starting-a-jupyter-lab-notebook.md): start JupyterLab on your laptop.
2. [running-a-jupyterlab-notebook.md](running-a-jupyterlab-notebook.md): clone a real R notebook (`exampleVolcanoPlotNotebook`), choose the R kernel, and use Restart and Run All.
3. [exploring-an-r-notebook.md](exploring-an-r-notebook.md): register the R kernel and run a small worked example in R.
4. `python.ipynb` ([view on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/interactive-computing/python.ipynb)): the Python starter notebook. It has no web page copy. Open it in JupyterLab.
5. `r.ipynb` ([view on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/interactive-computing/r.ipynb)): the R starter notebook. It has no web page copy. Open it in JupyterLab.

## Ask an AI assistant

*Optional.* Read [Using the AI prompts](../introduction/README.md) first: what to paste, what never to paste, and how to check the answer.

**Ask it to explain.**

```text
Explain what a Jupyter kernel is, and why the notebook gives different answers after I run cells out of order. Then explain "Restart Kernel and Run All Cells".
```

**Ask it to build.**

```text
Here is the code from a notebook cell. Turn it into a function with a name, inputs and a return value, and add a second cell that calls it on a small example and prints the result. Keep the output the same.

<paste cell>
```

**Ask it to review.**

```text
Review this notebook for repeatability. Look for cells that depend on an earlier cell run in a different order, hard-coded file paths, and results that change on each run (random numbers with no seed). List each with the cell number. Do not rewrite the notebook.

<paste notebook text>
```


## Further reading

- [Project Jupyter](https://jupyter.org/): home page and documentation index
- [JupyterLab documentation](https://jupyterlab.readthedocs.io/): the modern interface
- [IRkernel](https://irkernel.github.io/): R kernel for Jupyter
- [Executable Books Project](https://executablebooks.org/): MyST-NB, Jupyter Book and friends
- [nbconvert](https://nbconvert.readthedocs.io/): convert notebooks to other formats

## Supplementary information

### What a notebook is

A Jupyter notebook is a **JSON file** (extension `.ipynb`) that holds an ordered list of **cells**. Each cell is one of two kinds:

- **Markdown**: text, headings, links and maths.
- **Code**: sent to a **kernel** to run.

The **kernel** is a separate program that runs your code. Open a Python notebook and Jupyter starts a Python kernel in the background. Open an R notebook and it starts an R kernel. Variables you create live in the kernel, not in the file. That is why restarting the kernel wipes them.

### Launch JupyterLab

On a laptop (macOS or Windows Git Bash), in a terminal:

```bash
conda activate eos
jupyter lab
# A browser tab opens at http://localhost:8888/lab
```

On a cloud platform such as Lifebit, a JupyterLab session is already running. See [Other places to run these lessons](../introduction/other-places-to-run.md).

### The two starter notebooks

Each one is short on purpose. The aim is a runnable example that explains the basics, not a course in pandas or tidyverse. Each has:

1. A "what this notebook is" section.
2. A few code cells that produce real output.
3. An environment section that shows which kernel, conda environment and package versions you are running. This is gold when something stops working later.
4. A "Try it yourself" prompt.

### A real worked example

To see a real-data notebook with the same pattern, only longer, open [`explore_metadata.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/endometriosis/notebooks/explore_metadata.ipynb) in JupyterLab. It pulls real metadata from the ENA API for the endometriosis dataset the book is built around.

### The "Restart and Run All" habit

You can run a notebook's cells in any order. That helps when exploring. It hurts when you save the notebook, reopen it tomorrow, and your variables are gone, but cells you ran in a random order left output that looks right.

**Habit:** before you save a notebook you plan to share, click **Kernel**, then **Restart Kernel and Run All Cells**. If it gives the same output, it is reproducible. If not, you have caught a problem early.

### A note for the All of Us Researcher Workbench

The All of Us Workbench gives you Jupyter directly. Python, R and Nextflow are supported. It does not give you a direct `git pull` from GitHub, so versioning your notebooks needs a different routine. The Bridge patterns page describes one.

> **Check:** The original linked this to `../../bridges/index.md`. That page is not in this folder tree. Where does it live now?

## Next

[Building reusable command-line tools](../reusable-clis/README.md): turn a notebook's code into a tool that anyone can run.
