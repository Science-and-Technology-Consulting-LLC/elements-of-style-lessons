# Federated computing


> *In the book: Chapter 11 — Federated computing.*

:::{admonition} What you'll learn
:class: tip

- Diagram a federation: which boxes are sites, which is the coordinator.
- Explain what *doesn't* leave each site (the data) and what *does* (parameters).
- Apply the same shape to your own multi-institution biomedical problem.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

Biomedical data lives in silos — by funding, by institution, by IRB, by
data-use agreement. *Federated computing* is the discipline of running
the same workflow against data that lives in different places, without
the data leaving where it lives.

The compute travels to the data. The results travel back.

:::{admonition} Why this matters for NLM-CKN
:class: tip

Single-cell atlases are increasingly federated. The data for one study
lives at JAX; another lives at the Broad; a third lives in the All of Us
Workbench. A federated workflow lets you ask one question across all
three without negotiating bulk data transfers — and **without ever
violating the data-use agreement that says the data cannot leave its
institution**.
:::

## What this lesson teaches

By the end of this lesson you will:

1. Have a clean mental model of *"compute travels to data"* — and be able
   to explain it to a colleague in one minute.
2. Recognize when a problem is the right shape for federation, and when
   it isn't.
3. Be able to read a federated workflow (Nextflow or otherwise) and
   identify the *coordinator* and the *per-site* phases.
4. Understand the trust, audit, and provenance constraints that come
   along with federation — and the small set of habits that make those
   constraints manageable.

## The shape of a federated computation

A federated computation has two layers, and you can recognize them in
every real federated workflow:

1. **Per-site phase.** Each institution runs the same code against
   *its own* data, locally. Nothing leaves the institution except
   small, agreed-upon summary statistics, model parameters, or
   non-identifying metadata.
2. **Coordinator phase.** A central process — which can be as simple as
   *"take the median of what each site returned"* — combines the
   per-site outputs into a federated result.

That's it. Everything else is engineering. The hard parts are
**agreement on what summary leaves each site**, and **trust that each
site ran the code you think it ran**.

## The platform — ADAPTS (on Lifebit's federated fabric)

The platform behind the worked example below is **ADAPTS** —
Autoimmune Disease Analysis Platform Testing Space, an NIH initiative
led by NHLBI/CC, NHLBI, NIAMS, NIAID, with NIEHS, NIDCR, NINR, NINDS,
and NHGRI collaborating. ADAPTS runs on **Lifebit's federated
computing fabric** — the transport layer that lets each participating
institution train on its own data and share only model parameters with
a coordinator. The federation patterns this lesson teaches are the
same patterns ADAPTS uses in production.

## The worked example — `oadr-autoantibody`

The headline worked example for this lesson is a real, working federated
analysis in the NIH-NLM organisation:

**[Science-and-Technology-Consulting-LLC/oadr-autoantibody](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody)** —
*Predicting residual beta-cell function in Type 1 Diabetes, under
federation.*

The biology — for the one-paragraph version:

> Type 1 Diabetes is an autoimmune disease in which the patient's immune
> system destroys the insulin-producing beta cells of the pancreas. The
> readout of how many beta cells a patient has left is the **C-peptide
> AUC** during a four-hour mixed-meal tolerance test. The autoantibody
> panel (GAD65, IA-2, Insulin, ICA, ZnT8) is the immune signature of the
> attack. The natural scientific question is: *how well does the
> autoantibody profile predict the beta-cell function that survives the
> attack?*

The federation challenge:

> Each of four cohorts — **SDY524, SDY569, SDY797, SDY1737** — comes from a
> different institutional study with its own data-use governance. The
> data cannot be moved between institutions. But the institutions *can*
> share model parameters after each one has trained on its own subjects,
> and a coordinator can aggregate those parameters by taking the median
> across sites.

The three headline findings — these are the talk's central plots, and
they're the structural argument for federation:

1. **More institutions → lower error.** Simple linear regression's
   prediction error drops from 1.03 (averaged over the four solo runs)
   to 0.33 at four institutions — a *three-fold* improvement, with no
   institution acquiring more subjects.
2. **More rounds → continued benefit until plateau.** Iterating the
   federation (warm-starting from the previous round's aggregated
   parameters) reduces error further until the improvement is small
   enough to ignore.
3. **Federation lifts the cohort-size ceiling on statistical power.**
   The smallest cohort, SDY569 with N = 10, *cannot fit* a 9-feature
   regression alone. Stacked, the federation reaches N = 150 and can
   decisively detect biologically plausible effect sizes that
   single-institution studies would miss entirely.

The four notebooks worth opening:

- [`ipynb/federated_analysis_simulation_3x3.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/federated_analysis_simulation_3x3.ipynb)
  — the end-to-end federated story.
- [`ipynb/LinearRegression_vs_CNN_HeadToHead.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/LinearRegression_vs_CNN_HeadToHead.ipynb)
  — the centralised baseline the federation is compared against.
- [`ipynb/LASSO_ElasticNet_Autoantibody_CPeptide.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/LASSO_ElasticNet_Autoantibody_CPeptide.ipynb)
  — the interpretable-linear iteration.
- [`ipynb/EffectSizes_and_PowerAnalysis_Extended.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/ipynb/EffectSizes_and_PowerAnalysis_Extended.ipynb)
  — the power-vs-cohort-size argument that motivates federation.

Open the federated notebook first. Don't read the code; read the
**section headers** and the **figures**. Then come back to this page.

## What you'll have at the end

You'll be able to:

- Diagram the federation: which boxes are sites, which is the
  coordinator, what flows between them.
- Explain *what doesn't leave each site* (the data) and *what does*
  (model parameters, aggregate statistics, provenance metadata).
- Apply the same shape to a different biomedical problem of your own —
  for instance, federated NSForest marker discovery across cell atlases.

## The natural pairing

Federated computing pairs cleanly with three other lessons:

- [Nextflow](nextflow-workflows.md) — one pipeline, many environments.
- [Platforms](platforms.md) — Lifebit and others provide the federation
  transport.
- [Federated learning](federated-learning.md) — the special case where
  the per-site phase is *training a model* and the coordinator phase is
  *aggregating model weights*. The oadr-autoantibody example is exactly
  this case.

## Try the simulation on Lifebit

The full federated simulation lives in
[`case-studies/oadr-autoantibody`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/case-studies/oadr-autoantibody/README.md).

::::{tab-set}

:::{tab-item} Lifebit
:sync: lifebit

```bash
# In the oadr-autoantibody workspace on Lifebit:
jupyter notebook ipynb/federated_analysis_simulation_3x3.ipynb
# 30-60 min from cold; results cache so re-renders are seconds.
```

*This is the same simulation discussed above — same five methods,
same headline findings — running where Lifebit's transport layer can
later carry it to real per-site execution.*
:::

::::

## Honest constraints

Federation is not magic. Three constraints you should name out loud
every time you propose a federated design:

1. **Trust.** You're trusting each site to run the agreed-upon code on
   the agreed-upon data and to return only the agreed-upon summary.
   This is a governance problem, not a technical one.
2. **Audit.** The provenance trail has to survive across sites. The
   federated result has to be able to answer *which site contributed
   which subjects, run with which code version, at which point in time?*
3. **Privacy is not automatic.** "The data didn't leave" is not the same
   as "no information about an individual leaked." Model parameters
   themselves can leak training-set information in some adversarial
   settings. Differential privacy and secure aggregation are the next
   step beyond plain federation.

## Where to next

→ [Federated learning](federated-learning.md) — where the per-site phase
becomes model training, and the oadr-autoantibody example continues.
