# Federated learning

*In the book: Sections 10.2.3 and 10.2.4, Federated Learning; Median-of-Coefficients Aggregation.*

*Federated learning* trains a model when the training data lives in many places that cannot share it. The model travels and the data stays put. This lesson gives you the loop and a tiny experiment that shows why the way you combine sites matters.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Federated computing](../federated-computing/README.md), is done.

Open `lessons/federated-learning/median-of-coefficients-aggregation.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/federated-learning/median-of-coefficients-aggregation.ipynb)) and run each cell in order, top to bottom. This notebook uses a Python kernel, and its first two sections make a conda environment for it.

### What you should see

We compare the mean and the median of coefficients from five sites, one of them far off. We see `mean  : [ 4.2  -5.6   0.85]` against `median: [ 1.5  -2.    0.35]`: the median ignores the odd site.

> **Picture to add:** the notebook's output showing the mean and median lines (save a screenshot of the finished run) (save as assets/overview.png)

### Where the files are

- `lessons/federated-learning/median-of-coefficients-aggregation.ipynb` and `.md`: the experiment.
- `lessons/federated-learning/assets/`: pictures for this lesson.
- [`oadr-autoantibody` notebooks](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/tree/main/ipynb): the real federated learning example.

## Steps to execute

1. [`median-of-coefficients-aggregation.md`](median-of-coefficients-aggregation.md) — compare mean and median aggregation with one outlier site

## Ask an AI assistant

*Optional.* How to use these prompts is explained in [Using the AI prompts](../introduction/README.md).

**Ask it to explain.**

```text
Explain the federated learning loop in five steps. Then explain why the median of the sites' coefficients can be safer than the mean when one site is unusual.
```

**Ask it to build.**

```text
Write a Python function that takes the model coefficients from several sites and returns the coordinate-wise median, and a second that returns the weighted mean by sample size. Add a test with three sites where one is an outlier, and print both answers.
```

**Ask it to review.**

```text
Review this federated learning design: <describe it>. What does each site send, and could a site's private data be inferred from it? Is there a site that could be too small to share safely? List the risks and what to check.
```

## Further reading

- [McMahan et al., Federated Averaging (2016)](https://arxiv.org/abs/1602.05629)
- [Flower framework](https://flower.ai/)
- [PySyft](https://github.com/OpenMined/PySyft)
- [oadr-autoantibody notebooks](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/tree/main/ipynb)

## Supplementary information

For biomedical work this is often the only way to build cell-type classifiers, batch-correction models and patient-stratification models across institutions whose data-use agreements forbid pooling. It is a special case of [federated computing](../federated-computing/README.md), where the per-site phase is training a model.

### The federated learning loop

1. The coordinator sends a model (design plus current weights) to each site.
2. Each site trains it on its own data for some local epochs (passes over the data).
3. Each site returns only the updated weights, or the changes in weights. The data stays.
4. The coordinator combines the weights: usually the mean, the median, or something like FedAvg or FedProx.
5. The combined weights start the next round. Repeat until the improvement is too small to matter.

### The worked example: `oadr-autoantibody`

This is the same example as in [Federated computing](../federated-computing/README.md): the federated beta-cell-function predictor in [oadr-autoantibody](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody). This time, look at the learning half.

| Method | Family | Interpretable? |
|--------|--------|----------------|
| Simple linear regression | Linear, no regularisation | yes (coefficients) |
| Lasso regression | Linear, L1-penalised feature selection | yes (non-zero coefficients) |
| Random Forest (used for regression) | Tree ensemble, non-linear | yes (feature importance) |
| Convolutional neural network | Non-linear deep model | no (latent layers) |
| Convolutional network with autoencoder pretraining | Two stages: unsupervised representation, then supervised head | no (latent layers) |

All five use the same protocol: train at each site, share parameters, combine by the *median across sites*, send back, repeat.

What the experiment showed:

1. **Linear, lasso and Random Forest improve with more institutions.** Linear regression drops from 1.03 (average of solo runs) to 0.33 at four institutions. Lasso: 0.45 to 0.24. Random Forest: 0.37 to 0.25.
2. **A plain CNN gets worse.** Solo CNN: 0.36. Four-institution federated: 0.41. Median-combining independently trained network weights breaks the model, because each site's network settles into a different arrangement of weights.
3. **An autoencoder fixes it.** Pretrain an autoencoder at each site, federate that first, then attach a small supervised head. Result: about 0.31, stable across cohort sizes and improving with iteration.
4. **More rounds help, but the curve matters.** The plain CNN drops sharply from round 1 to 2, then gets worse from round 3. The autoencoder plus head improves steadily and levels off at round 4 with mean error 0.245, matching lasso's single round to two decimals.

Open [`federated_analysis_simulation_3x3.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/oadr-autoantibody/blob/main/federated_analysis_simulation_3x3.ipynb).

**Why the autoencoder result matters most:** federated learning of deep models needs a shared representation first. Without it, every site's network ends up in a different region of weight space, and averaging gives nonsense. Whenever you want to federate a deep model directly, ask whether there is a representation you can federate first.

### Pairs well with

[MCP](../mcp-server/README.md) and [Platforms](../platforms/README.md) (Lifebit). A researcher describes a training goal in chat. The agent reads the MCP-exposed `--help`, infers the inputs and sends the federated training to Lifebit, which runs each site. Results return to the chat.

### Honest framing

"Federated" does not mean "private". Keep three things apart:

- **Federation:** data does not move between sites. Only parameters or summaries do.
- **Differential privacy:** a mathematical limit on how much any one subject can change the released parameters. It needs calibrated noise.
- **Secure aggregation:** a cryptographic way for the coordinator to compute the combined result without seeing any one site's update.

Federation without the other two is still a big gain over pooling in most biomedical settings. Say which guarantees you have and which you do not.

## Next

[MCP server](../mcp-server/README.md): wrap the federated-learning command-line tool so an AI agent can drive it on Lifebit.
