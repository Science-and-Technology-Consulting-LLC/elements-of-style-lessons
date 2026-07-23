# Simulating a 3×3 federated run

*Companion walkthrough to the [federated-computing](README.md) lesson.
This is the mechanical shape behind the oadr-autoantibody design
notebook.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — copy each shell block into your terminal; copy each
  Python block into `python -` or your editor.
- **In the paired notebook** [`simulating-a-3x3-federated-run.ipynb`](../ipynb/simulating-a-3x3-federated-run.ipynb) — every Python
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
conda create -n simulating-a-3x3-federated-run -y python=3.11 ipykernel
conda activate simulating-a-3x3-federated-run
python -m ipykernel install --user \
    --name simulating-a-3x3-federated-run \
    --display-name "Python (simulating-a-3x3-federated-run)"
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


## The idea

Three sites, three data folds each. Each site trains locally on its own
fold; the coordinator aggregates *the model parameters* (never the raw
data) into a single global model. The pattern that makes it "federated"
is that raw data never leaves each site.

## Setup — one Python env, three folders

```bash
conda create -n fed-demo -y python=3.11 numpy pandas scikit-learn
conda activate fed-demo
```

## Prepare three folds

```bash
mkdir -p sites/{siteA,siteB,siteC}
python - <<'PY'
import numpy as np, pandas as pd, os
rng = np.random.default_rng(0)
for site in ["siteA", "siteB", "siteC"]:
    n = 200
    X = rng.normal(size=(n, 3))
    y = X @ np.array([1.5, -2.0, 0.3]) + rng.normal(scale=0.5, size=n)
    pd.DataFrame(X, columns=list("abc")).assign(y=y).to_csv(
        f"sites/{site}/train.csv", index=False)
PY
ls sites/*/train.csv
```

## Site-local training

Each site runs the same script on its own file:

```bash
python - <<'PY'
import pandas as pd, numpy as np, json, sys
for site in ["siteA", "siteB", "siteC"]:
    df = pd.read_csv(f"sites/{site}/train.csv")
    X, y = df[["a","b","c"]].values, df["y"].values
    # linear regression coefficients via least squares
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    json.dump({"site": site, "beta": beta.tolist()},
              open(f"sites/{site}/model.json", "w"))
    print(site, beta)
PY
```

## Coordinator — median aggregation

```bash
python - <<'PY'
import json, numpy as np
betas = [json.load(open(f"sites/{s}/model.json"))["beta"]
         for s in ["siteA","siteB","siteC"]]
global_beta = np.median(np.array(betas), axis=0)
json.dump({"global_beta": global_beta.tolist()},
          open("global_model.json", "w"))
print("global:", global_beta)
PY
```

## What just happened

- Each site kept its data on disk (never sent to the coordinator).
- Each site sent only a three-number parameter vector up.
- The coordinator combined the three vectors — median across sites —
  into one global model.
- On real infrastructure (Lifebit's federated fabric, ADAPTS,
  BeeKeeperAI) that "sent up" step is a signed message across a
  data-use-agreement boundary.

## Where to next

→ Back to the [federated-computing lesson](README.md).

→ [`case-studies/oadr-autoantibody/`](../../case-studies/oadr-autoantibody/README.md) —
the real biomedical version with four cohorts (SDY524, SDY569, SDY797,
SDY1737) and a proper coordinator.
