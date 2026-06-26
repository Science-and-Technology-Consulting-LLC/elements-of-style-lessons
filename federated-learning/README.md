# Federated learning

A specific application of [federated computing](federated-computing.md):
train (or fine-tune) a model where the training data lives in many
places that cannot share raw data. **The model travels; the data stays
put.**

For biomedical work, this is the only viable path for many cell-type
classifiers, batch-correction models, and patient-stratification models
that need to learn across institutions whose data-use agreements forbid
pooling.

## The federated learning loop

The basic loop is short enough to keep in your head:

1. The coordinator sends a model (architecture + current weights) to
   each participating site.
2. Each site trains the model on its own data for some number of local
   epochs.
3. Each site returns *only the updated weights* (or only the weight
   deltas), not the data, to the coordinator.
4. The coordinator aggregates the returned weights — typically by
   averaging, by taking the median, or by something more elaborate like
   FedAvg or FedProx.
5. The aggregated weights become the next round's starting point.
   Repeat from step 1 until convergence or until the round-over-round
   improvement is too small to matter.

The lesson is in the **loop**. Pick any one box, run it on real data,
and you have a single-institution model. Wire the boxes together with a
trustworthy transport and you have a federation.

## The worked example — `oadr-autoantibody`

The headline worked example, *the same one* introduced in
[federated computing](federated-computing.md), is the federated
beta-cell-function predictor in **[NIH-NLM/oadr-autoantibody](https://github.com/NIH-NLM/oadr-autoantibody)**.

This time, focus on the **learning** half of the story.

### Five methods, one federation protocol

| Method | Family | Interpretable? |
|--------|--------|----------------|
| Simple linear regression | Linear, no regularisation | yes (coefficients) |
| Lasso regression | Linear, L1-penalised feature selection | yes (non-zero coefficients) |
| Random Forest (used for regression) | Tree ensemble, non-linear | yes (feature importance) |
| Convolutional neural network | Non-linear deep model | no (latent layers) |
| Convolutional network with autoencoder pretraining | Two-stage: unsupervised representation + supervised head | no (latent layers) |

All five are evaluated under the same federation protocol: train at each
site, share parameters with the coordinator, aggregate by *median across
sites*, redistribute, repeat.

### What the experiment showed

These four results are the lesson — read them out loud once before you
open the notebook:

1. **For interpretable methods (linear, lasso, Random Forest), federation
   across more institutions sharply reduces prediction error.** Linear
   regression drops from 1.03 (averaged across solo runs) to 0.33 at
   four institutions. Lasso: 0.45 → 0.24. Random Forest: 0.37 → 0.25.
2. **For a naïve CNN, federation actively *hurts*.** Solo CNN: 0.36;
   four-institution federated: 0.41. Median-aggregating independently
   trained neural-network weights breaks the model because per-site
   networks settle into incompatible parameterisations.
3. **An autoencoder rescues neural-network federation.** Pretrain a
   per-institution autoencoder, federate *that* first, *then* attach a
   small supervised prediction head. The shared representation makes
   the heads compatible. Result: ~0.31, stable across cohort sizes and
   improving with iteration.
4. **Multi-round federation extracts further benefit, but the curve
   matters.** The plain CNN drops sharply between round 1 and 2 (warm
   start fixes the random init), then degrades from round 3 on. The
   autoencoder + head shows clean monotonic improvement, plateauing at
   round 4 with mean prediction error 0.245 — *matching lasso's single
   round to two decimal places.*

The notebook to open: [`ipynb/federated_analysis_simulation_3x3.ipynb`](https://github.com/NIH-NLM/oadr-autoantibody/blob/main/ipynb/federated_analysis_simulation_3x3.ipynb).

### Why the autoencoder result is the most important

It is the cleanest demonstration that **federated learning of deep models
needs a shared representation first.** Without that, every site's
network ends up in a different region of weight space, and averaging
those weights produces nonsense. With it, every site's *encoder* lives
in roughly the same place, and the small supervised head added at the
end has compatible inputs everywhere.

This pattern generalises. Whenever you're tempted to federate a deep
model directly: ask if there's a representation you can federate first.

## What you'll have at the end

You'll be able to:

- Diagram a federated learning round and name what flows on each arrow.
- Explain why median (or FedAvg) of model weights works for linear models
  and tree ensembles, and why it tends to fail for naïve deep models.
- Recognise when an autoencoder (or other shared-representation pretrain)
  is the right move.
- Read the four oadr-autoantibody notebooks and explain each headline
  finding to a colleague.

## The natural pairing

Federated learning is the case study where [MCP](mcp-server.md) +
[Platforms](platforms.md) (Lifebit) get *especially* interesting:

> A researcher describes a model-training intent in chat. The agent
> (Claude / ChatGPT) reads the MCP-exposed CLI's `--help`, infers the
> right inputs, and dispatches the federated training to Lifebit, which
> orchestrates per-site execution. Results return to the researcher's
> chat window. The researcher never writes a config file.

The oadr-autoantibody pipeline is exactly the kind of workflow that
benefits from this stack.

## Honest framing

"Federated" is *not* the same as "private." Three things to keep
mentally separated:

- **Federation** — data does not move between sites; only model
  parameters or aggregates do.
- **Differential privacy** — a mathematical guarantee that the
  contribution of any one subject to the released parameters is bounded.
  Requires adding calibrated noise.
- **Secure aggregation** — a cryptographic guarantee that the
  coordinator can compute the aggregate of the site-level updates
  *without* seeing any individual site's update.

A federated workflow without DP and without secure aggregation is still
a major improvement over centralisation in most biomedical contexts —
but call out which guarantees you have and which you don't have. Don't
let the word *federated* do work that *private* should be doing.

## Where to next

→ [MCP server](mcp-server.md) — wrap the federated-learning CLI in MCP
and let an agent drive it on Lifebit.
