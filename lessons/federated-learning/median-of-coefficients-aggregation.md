# Median-of-coefficients aggregation — the smallest FedAvg variant

*Companion walkthrough to the [federated-learning](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — copy each shell block into your terminal; copy each
  Python block into `python -` or your editor.
- **In the paired notebook** [`median-of-coefficients-aggregation.ipynb`](median-of-coefficients-aggregation.ipynb) — every Python
  cell is executed by a dedicated Jupyter **Python 3** kernel. Run the
  shell blocks in a terminal FIRST to create the env and register the
  kernel; then pick that kernel when you open the notebook.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### Once per walkthrough — a dedicated conda env + Jupyter kernel

Isolating the walkthrough in its own env means nothing you install here
leaks out. See [conda-environments](../conda-environments/README.md).

```bash
conda create -n median-of-coefficients-aggregation -y python=3.11 ipykernel
conda activate median-of-coefficients-aggregation
python -m ipykernel install --user \
    --name median-of-coefficients-aggregation \
    --display-name "Python (median-of-coefficients-aggregation)"
```

Lesson-specific `pip install`s appear in the steps below — they land in
this env.

### Every time — verify Python is on your PATH

```python
import shutil, sys
print("python  ", sys.executable)
for cmd in ["conda", "pip", "git", "docker"]:
    print(f"{cmd:<8}", shutil.which(cmd) or "MISSING")
```


## Why median, not mean

The classic FedAvg averages per-site model weights. Median-of-coefficients
is a small variant that is more robust when one site's data is very
different in scale (or, honestly, when one site's data is wrong). Both are
weight-aggregation strategies; both keep raw data behind institutional
walls.

## Setup

```bash
conda create -n fed-learn -y python=3.11 numpy pandas scikit-learn
conda activate fed-learn
```

## Compare mean vs. median aggregation

```bash
python - <<'PY'
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
PY
```

Read the two vectors. The mean is pulled toward the outlier; the median
is not. Federated learning at scale relies on aggregators that survive
that kind of shape-mismatched site.

## Where the abstraction really lives

- Local training: a black box — could be linear regression, could be a
  gradient step on a neural network, could be a whole Nextflow module
  scoring a pre-trained model.
- Aggregation: mean, median, trimmed mean, secure aggregation, differential
  privacy — swap in whichever your data-use agreement requires.
- Rounds: repeat *train → send weights → aggregate → broadcast* until the
  global loss stops moving.

The [oadr-cpep](../../case-studies/oadr-cpep/README.md) package
implements exactly this loop for C-Peptide AUC prediction across four
Type-1-Diabetes cohorts.

## Where to next

→ Back to the [federated-learning lesson](README.md).

→ The [oadr-autoantibody notebook](../../case-studies/oadr-autoantibody/README.md)
and its productised sibling [oadr-cpep](../../case-studies/oadr-cpep/README.md).
