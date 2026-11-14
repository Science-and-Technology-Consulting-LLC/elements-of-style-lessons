# Simulating a 3×3 federated run

You will simulate three hospitals that each train a model on their own data and send only the model's numbers to a coordinator. This is the smallest working picture of *federated computing*: the data stays where it is, and only small summaries travel.

*Part of the [federated-computing](README.md) lesson. This is the mechanical shape behind the oadr-autoantibody notebook.*

## What you will do

- Make fake data for three sites, A, B and C, each in its own folder.
- Train a simple model at each site and save only its three coefficients.
- Combine the three sets of coefficients with a median at the coordinator.
- See that the raw data never left the site folders.

## What you need

- [conda](https://docs.conda.io/) to make a clean environment. See [creating a conda environment](../conda-environments/creating-a-conda-environment.md).
- [JupyterLab](https://jupyter.org/) with a Python kernel. See [starting a JupyterLab notebook](../interactive-computing/starting-a-jupyter-lab-notebook.md).
- The Python packages [NumPy](https://numpy.org/) and [pandas](https://pandas.pydata.org/) (*Install the packages the simulation uses (in a terminal)* installs them).
- A terminal. On a Mac use *Terminal*. On Windows use *Git Bash*. See [command-line-and-git-bash](../command-line-and-git-bash/README.md).

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`simulating-a-3x3-federated-run.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/federated-computing/simulating-a-3x3-federated-run.ipynb) and run each cell in order, top to bottom.

## Make a clean environment for this walkthrough (in a terminal)

Why: a *conda environment* is a private folder of programs. Installing here keeps everything you add out of your other work. See [creating a conda environment](../conda-environments/creating-a-conda-environment.md). Run these lines in a **terminal**, not in a notebook cell. `conda create` makes the environment, `conda activate` switches to it, and `ipykernel install` lets Jupyter use it.

```bash
conda create -n simulating-a-3x3-federated-run -y python=3.11 ipykernel
conda activate simulating-a-3x3-federated-run
python -m ipykernel install --user \
    --name simulating-a-3x3-federated-run \
    --display-name "Python (simulating-a-3x3-federated-run)"
```

**What you should see:** conda prints a plan and downloads packages. At the end `ipykernel install` prints `Installed kernelspec simulating-a-3x3-federated-run`. Your terminal prompt now starts with `(simulating-a-3x3-federated-run)`. After you restart JupyterLab, the Launcher shows a tile called **Python (simulating-a-3x3-federated-run)**.

> **Check:** the `ipykernel` kernel installed here has no `numpy` or `pandas`. Which environment should the notebook run in, this one or the one in the next step?

## Install the packages the simulation uses (in a terminal)

Why: the simulation needs NumPy (numbers and arrays) and pandas (tables). This second environment has both, plus [scikit-learn](https://scikit-learn.org/). Run these lines in a **terminal**:

```bash
conda create -n fed-demo -y python=3.11 numpy pandas scikit-learn
conda activate fed-demo
```

**What you should see:** conda prints a plan, downloads packages and returns to the prompt. The prompt now starts with `(fed-demo)`.

> **Check:** *Make a clean environment for this walkthrough (in a terminal)* and *Install the packages the simulation uses (in a terminal)* make two different environments. Please confirm which one the notebook kernel should use, and whether `numpy` and `pandas` should be added to the *Make a clean environment for this walkthrough (in a terminal)* environment instead.

## Check which Python this notebook uses

Why: if the notebook uses a Python without NumPy and pandas, *Check which folder you are in* stops with `ModuleNotFoundError`. It is better to learn that now.

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "docker"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```

**What you should see:** the first line shows which Python the notebook uses. The other lines show where `conda`, `pip`, `git` and `docker` live, or `MISSING`. For this walkthrough only the Python line matters. `MISSING` for `docker` is fine.

```python
import numpy, pandas
print("numpy ", numpy.__version__)
print("pandas", pandas.__version__)
```

**What you should see:** two lines with version numbers. If you see `ModuleNotFoundError`, the notebook's Python lacks the packages. See **If something goes wrong** below.

## The idea

Three sites each hold a fold (a slice) of the data. Each site trains locally on its own fold. The coordinator combines *the model parameters* (never the raw data) into one global model. What makes it *federated* is that raw data never leaves each site.

## Check which folder you are in

Why: this notebook creates a folder called `sites` next to it. You want to know where that will be.

```python
import os
print(os.getcwd())
```

**What you should see:** a path that ends in `lessons/federated-computing`.

## Make three sites and their data

Why: real sites would each have real patient data. Here each site gets 200 made-up rows with three input columns `a`, `b`, `c` and one output column `y`. The outputs follow the same rule at every site (`y` is about 1.5 times `a`, minus 2 times `b`, plus 0.3 times `c`, plus a little noise). The line `rng = np.random.default_rng(0)` fixes the random numbers, so you get the same data every time. The cell writes one file, `sites/siteX/train.csv`, per site.

```python
import numpy as np, pandas as pd, os
rng = np.random.default_rng(0)
for site in ["siteA", "siteB", "siteC"]:
    os.makedirs(f"sites/{site}", exist_ok=True)
    n = 200
    X = rng.normal(size=(n, 3))
    y = X @ np.array([1.5, -2.0, 0.3]) + rng.normal(scale=0.5, size=n)
    pd.DataFrame(X, columns=list("abc")).assign(y=y).to_csv(
        f"sites/{site}/train.csv", index=False)
```

**What you should see:** nothing printed. The cell has no `print`. To check, run this in a terminal in the notebook's folder, which lists the three files:

```text
ls sites/*/train.csv
```

You should see `sites/siteA/train.csv`, `sites/siteB/train.csv` and `sites/siteC/train.csv`.

## Train at each site

Why: this is the *per-site phase*. Each site fits a straight-line model to its own file by least squares (the standard way to find the best-fitting line). It saves only the three fitted numbers, called *coefficients* (`beta`), in `model.json`. The data file stays put.

```python
import pandas as pd, numpy as np, json, sys
for site in ["siteA", "siteB", "siteC"]:
    df = pd.read_csv(f"sites/{site}/train.csv")
    X, y = df[["a","b","c"]].values, df["y"].values
    # linear regression coefficients via least squares
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    json.dump({"site": site, "beta": beta.tolist()},
              open(f"sites/{site}/model.json", "w"))
    print(site, beta)
```

**What you should see:** three lines, one per site, each with three numbers close to 1.5, -2.0 and 0.3. In the earlier run they were:

```text
siteA [ 1.45618988 -2.04875432  0.32745398]
siteB [ 1.51906479 -1.97674042  0.32127901]
siteC [ 1.5273781  -1.98049224  0.29937393]
```

Each site's numbers are a little different, because each site has different noise.

## Combine at the coordinator

Why: this is the *coordinator phase*. The coordinator reads only the three `model.json` files and takes the median of each coefficient across sites. The *median* is the middle value, so one odd site cannot pull the answer far. The result goes into `global_model.json`.

```python
import json, numpy as np
betas = [json.load(open(f"sites/{s}/model.json"))["beta"]
         for s in ["siteA","siteB","siteC"]]
global_beta = np.median(np.array(betas), axis=0)
json.dump({"global_beta": global_beta.tolist()},
          open("global_model.json", "w"))
print("global:", global_beta)
```

**What you should see:** one line that starts with `global:` and shows three numbers. In the earlier run:

```text
global: [ 1.51906479 -1.98049224  0.32127901]
```

The three numbers are close to 1.5, -2.0 and 0.3, the values used to make the data.

## What just happened

- Each site kept its data on disk. The data was never sent to the coordinator.
- Each site sent up only a vector of three numbers.
- The coordinator combined the three vectors (the median across sites) into one global model.
- On real infrastructure (Lifebit's federated fabric, ADAPTS, BeeKeeperAI) the "sent up" step is a signed message across a data-use-agreement boundary.

## If something goes wrong

- **`ModuleNotFoundError: No module named 'numpy'` (or `pandas`).** The notebook's Python is not the environment with the packages. In a terminal run `conda activate` for the environment your kernel uses, then `pip install numpy pandas`. Restart the kernel and run the cells again.
- **`conda: command not found` on Windows.** Open *Git Bash* (not PowerShell) after installing conda. See [conda-environments](../conda-environments/README.md).
- **The kernel tile for the new environment is missing in the Launcher.** Restart JupyterLab completely. Close the browser tab and stop `jupyter lab` in the terminal with Ctrl-C, then start it again.
- **`FileNotFoundError` on `sites/siteA/train.csv`.** You skipped *Make three sites and their data*. Run that cell first, then *Train at each site*.

## Next

Return to the [federated-computing lesson](README.md), or go to the real biomedical version with four cohorts and a proper coordinator: [oadr-autoantibody](../../case-studies/oadr-autoantibody/README.md) (cohorts SDY524, SDY569, SDY797 and SDY1737).
