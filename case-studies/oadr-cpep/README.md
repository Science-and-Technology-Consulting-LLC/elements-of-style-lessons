# oadr-cpep — the productised federated package

The federated learning analysis prototyped in the
[`oadr-autoantibody/`](../oadr-autoantibody/README.md) case study —
predicting residual β-cell function in Type 1 Diabetes — was carried
forward from *notebook design* to a *Python package* here:

**[NIH-NLM/oadr-cpep](https://github.com/NIH-NLM/oadr-cpep)**

Homepage: [https://nih-nlm.github.io/oadr-cpep/](https://nih-nlm.github.io/oadr-cpep/)

## What it is

From the upstream README:

> C-Peptide AUC prediction Python package using features from ImmPort SDY
> data, demonstrating the ability to achieve a-priori power by increasing
> N and then using the same workflow but federating on the coefficients
> (weights) decreases mean square error (MSE) and increases R² (variation
> explained by features).

## The two-repo pattern — notebook, then package

This case study is deliberately paired with
[`oadr-autoantibody/`](../oadr-autoantibody/README.md):

| Repo | Role | Format |
|---|---|---|
| [`NIH-NLM/oadr-autoantibody`](https://github.com/NIH-NLM/oadr-autoantibody) | **Design notebook** — the federated analysis in prose + `.ipynb`, four notebooks exploring linear vs. CNN, ElasticNet, effect sizes, and power analysis. | Jupyter notebooks. |
| [`NIH-NLM/oadr-cpep`](https://github.com/NIH-NLM/oadr-cpep) | **Productised package** — the same computation refactored into a `pip install`-able Python package with a CLI, unit tests, and CI. | Python package. |

This is exactly the *"notebook is a draft tool; a CLI is a durable tool"*
transition from
[The Rules](../../lessons/elements-of-style-rules/README.md), applied to a
real federated-learning problem.

## Which lessons this case study uses

| Step | Uses lesson | Demonstrates |
|------|-------------|--------------|
| Prototype in a notebook | [interactive-computing](../../lessons/interactive-computing/README.md) | `oadr-autoantibody/ipynb/*.ipynb` |
| Refactor to a Python CLI | [reusable-clis](../../lessons/reusable-clis/README.md) | `oadr-cpep` Typer CLI |
| Containerise + publish | [containers](../../lessons/containers/README.md) + [continuous-integration](../../lessons/continuous-integration/README.md) | Dockerfile + GHCR publish |
| Wrap as a Nextflow module | [nextflow-modules](../../lessons/nextflow-modules/README.md) | one module per CLI verb |
| Run under federation | [federated-computing](../../lessons/federated-computing/README.md) + [federated-learning](../../lessons/federated-learning/README.md) | ADAPTS platform, median-of-coefficients aggregation |

## Why the pair matters pedagogically

Most working scientists live in a notebook forever. The oadr-cpep pair
shows *what changes and what stays the same* when the notebook graduates
to a package:

- **Stays the same:** the science (features, model choice, evaluation
  metrics).
- **Changes:** every step becomes a callable function, every function has
  a test, every configuration knob becomes a CLI flag, and the whole
  package installs into a container that a federated coordinator can pull.

The book chapter grounds this transition explicitly.

## See also

- [`oadr-autoantibody/`](../oadr-autoantibody/README.md) — the design
  notebook this package descends from.
- The [federated-computing lesson](../../lessons/federated-computing/README.md)
  and [federated-learning lesson](../../lessons/federated-learning/README.md).
