# oadr-autoantibody — the federated worked example

The federated analysis paired with the
[federated-computing](../../lessons/federated-computing/README.md) and
[federated-learning](../../lessons/federated-learning/README.md) lessons
lives in its own repository:

**[Science-and-Technology-Consulting-LLC/oadr-autoantibody](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody)**

*Predicting residual beta-cell function in Type 1 Diabetes, under
federation.*

The federated platform behind this case study is **ADAPTS**
(Autoimmune Disease Analysis Platform Testing Space) — an NIH
initiative running on Lifebit's federated computing fabric. The
case study is the demonstration of what's possible when the
federated lessons are stacked on the ADAPTS / Lifebit platform.

## What it shows

Each of four cohorts — **SDY524**, **SDY569**, **SDY797**, **SDY1737** —
comes from a different institutional Type 1 Diabetes study with its own
data-use governance. The data cannot be moved between institutions, but
the institutions can share *model parameters*. A coordinator aggregates
those parameters by taking the median across sites.

The headline findings — which are the spine of the federated lessons:

1. **More institutions → lower error.** Simple linear regression's
   prediction error drops from 1.03 (averaged across solo runs) to
   0.33 at four institutions — a three-fold improvement, with no
   institution acquiring more subjects.
2. **More rounds → continued benefit until plateau.** Iterating the
   federation reduces error further until the improvement is small
   enough to ignore.
3. **Federation lifts the cohort-size ceiling on statistical power.**
   The smallest cohort, SDY569 with N = 10, *cannot fit* a 9-feature
   regression alone. Stacked, the federation reaches N = 150 and can
   decisively detect biologically plausible effect sizes that
   single-institution studies would miss entirely.

## Five methods, one protocol

| Method | Family | Federation result |
|--------|--------|-------------------|
| Simple linear regression | Linear | ✓ 1.03 → 0.33 |
| Lasso regression | Linear, L1 | ✓ 0.45 → 0.24 |
| Random Forest (regression) | Tree ensemble | ✓ 0.37 → 0.25 |
| Convolutional neural network | Deep | ✗ federation *hurts* (0.36 → 0.41) |
| CNN + autoencoder pretraining | Deep, two-stage | ✓ 0.31 stable, plateaus at 0.245 |

The autoencoder result is the most important: **federated learning of
deep models needs a shared representation first.**

## The four notebooks to open

In the upstream repo:

- [`ipynb/federated_analysis_simulation_3x3.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/federated_analysis_simulation_3x3.ipynb) — end-to-end federated story
- [`ipynb/LinearRegression_vs_CNN_HeadToHead.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/LinearRegression_vs_CNN_HeadToHead.ipynb) — centralised baseline
- [`ipynb/LASSO_ElasticNet_Autoantibody_CPeptide.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/LASSO_ElasticNet_Autoantibody_CPeptide.ipynb) — interpretable linear
- [`ipynb/EffectSizes_and_PowerAnalysis_Extended.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/EffectSizes_and_PowerAnalysis_Extended.ipynb) — power-vs-cohort-size

## Why a separate repo, not a fork here

The oadr-autoantibody analysis is its own scientific work product, with
its own data-use considerations and its own provenance. We *link* to it
from the federated lessons rather than fork it into this repo, so:

- The federated workflow stays current with upstream changes.
- Provenance is clean — readers can see exactly whose IRBs the data sits under.
- We avoid duplicating sensitive metadata across repos.

## See also

- [`endometriosis/`](../endometriosis/) — the threaded *centralised* worked example.
- [federated-computing lesson](../../lessons/federated-computing/README.md)
- [federated-learning lesson](../../lessons/federated-learning/README.md)
