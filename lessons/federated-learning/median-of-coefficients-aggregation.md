# Median-of-coefficients aggregation: the smallest FedAvg variant

You will compare two ways of combining models from five sites, one of which has bad data, and see that the median beats the mean. This matters because in federated learning a single odd site can ruin the shared model if you combine the sites the wrong way.

*Part of the [Federated learning](README.md) lesson.*

## Start here

### What you will do

- Build five sets of model coefficients, one per site, with one site very far off.
- Combine them with the mean (the average).
- Combine them with the median (the middle value).
- See which answer the odd site spoils.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson page, [Federated computing](../federated-computing/README.md), is done. It shows [one site sending only numbers to a coordinator](../federated-computing/simulating-a-3x3-federated-run.md).
- The notebook is open: `median-of-coefficients-aggregation.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/federated-learning/median-of-coefficients-aggregation.ipynb)). Run each cell in order, top to bottom. It uses a Python kernel.
- We use [NumPy](https://numpy.org/). The steps below install it.

## Steps to execute

### Make a clean environment for this walkthrough (in a terminal)

Why: a clean environment keeps what we add out of our other work. Environments are explained in [creating a conda environment](../conda-environments/creating-a-conda-environment.md). Run these lines in a **terminal**, not in a notebook cell. `conda create` makes the environment, `conda activate` switches to it, and `ipykernel install` lets Jupyter use it.

```bash
conda create -n median-of-coefficients-aggregation -y python=3.11 ipykernel
conda activate median-of-coefficients-aggregation
python -m ipykernel install --user \
    --name median-of-coefficients-aggregation \
    --display-name "Python (median-of-coefficients-aggregation)"
```

**What you should see:** conda prints a plan and downloads packages. At the end `ipykernel install` prints `Installed kernelspec median-of-coefficients-aggregation`. Your terminal prompt now starts with `(median-of-coefficients-aggregation)`. After you restart JupyterLab, the Launcher shows a tile called **Python (median-of-coefficients-aggregation)**.

> **Check:** the `ipykernel` kernel installed here has no `numpy` or `pandas`. Which environment should the notebook run in, this one or the one in the next step?

### Install the packages the walkthrough uses (in a terminal)

Why: the code uses NumPy for arrays. This second environment has NumPy, pandas and [scikit-learn](https://scikit-learn.org/). Run these lines in a **terminal**:

```bash
conda create -n fed-learn -y python=3.11 numpy pandas scikit-learn
conda activate fed-learn
```

**What you should see:** conda prints a plan, downloads packages and returns to the prompt. The prompt now starts with `(fed-learn)`.

> **Check:** *Make a clean environment for this walkthrough (in a terminal)* and *Install the packages the walkthrough uses (in a terminal)* make two different environments. Please confirm which one the notebook kernel should use, and whether `numpy` should be added to the *Make a clean environment for this walkthrough (in a terminal)* environment instead.

### Check which Python this notebook uses

Why: if the notebook's Python has no NumPy, the comparison step stops with `ModuleNotFoundError`.

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "podman"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```

**What you should see:** the first line shows which Python the notebook uses. The other lines show where `conda`, `pip`, `git` and `podman` live, or `MISSING`. Only the Python line matters here. `MISSING` for `podman` is fine.

```python
import numpy
print("numpy", numpy.__version__)
```

**What you should see:** one line with a version number. `ModuleNotFoundError` means the notebook's Python lacks NumPy. See *If something goes wrong* below.

### Why median and not mean

Why: the classic method, *FedAvg* (federated averaging), takes the average of each site's model weights. The median is a small change. It is more robust when one site's data is very different in scale, or when one site's data is wrong. Both are ways to combine weights. In both, raw data stays behind each institution's walls. A *coefficient* is one number a model learns; a *weight* is the same idea.

### Compare the mean and the median

Why: the cell builds five sites' coefficients. Four sites agree, and the fifth is ten times too large. It then prints the mean and the median for each of the three coefficients.

```python
import numpy as np
np.random.seed(0)

# Simulate 5 sites — 4 well-scaled, one wildly outlier
betas = np.array([
    [ 1.5, -2.0,  0.3],
    [ 1.6, -1.9,  0.4],
    [ 1.4, -2.1,  0.2],
    [ 1.5, -2.0,  0.35],
    [15.0,-20.0,  3.0],   # outlier site
])

print("mean  :", betas.mean(axis=0))     # dragged by outlier
print("median:", np.median(betas, axis=0)) # unaffected
```

**What you should see:** two lines:

```text
mean  : [ 4.2  -5.6   0.85]
median: [ 1.5  -2.    0.35]
```

Read the two vectors. The mean is pulled toward the odd site, to 4.2, -5.6 and 0.85. The median stays at 1.5, -2.0 and 0.35, which is what the four good sites say. Federated learning at scale relies on ways of combining that survive an odd site.

### Where the idea really lives

- **Local training** is a black box. It could be linear regression, a step of a neural network, or a whole Nextflow module scoring a pre-trained model.
- **Aggregation** can be the mean, the median, a trimmed mean, secure aggregation or differential privacy. Swap in whatever your data-use agreement requires.
- **Rounds** repeat *train, send weights, aggregate, send back* until the shared model stops improving.

The [oadr-cpep](../../case-studies/oadr-cpep/README.md) package implements exactly this loop for C-peptide AUC prediction across four Type 1 Diabetes cohorts.

### If something goes wrong

- **`ModuleNotFoundError: No module named 'numpy'`.** The notebook's Python is not the environment with NumPy. In a terminal run `conda activate` for the environment your kernel uses, then `pip install numpy`. Restart the kernel and run the cells again.
- **`conda: command not found`.** Open a new terminal, as described on the [Introduction page](../introduction/README.md), then try again.
- **The kernel tile for the new environment is missing in the Launcher.** Stop `jupyter lab` in the terminal with Ctrl-C, start it again and reload the page.

## Next

Return to the [Federated learning lesson](README.md), or open the [oadr-autoantibody notebook](../../case-studies/oadr-autoantibody/README.md) and its productised sibling [oadr-cpep](../../case-studies/oadr-cpep/README.md).
