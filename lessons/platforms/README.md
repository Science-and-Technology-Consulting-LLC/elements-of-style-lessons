# Platforms — a transport-layer protocol for science as a service


> *In the book: Chapter 18 — Platforms — a transport-layer protocol for science.*

:::{admonition} What you'll learn
:class: tip

- Why Lifebit's free, institutional-login tier is the open-science on-ramp.
- Where CAVATICA and AoU fit (and why Biowulf is a different category).
- Drive a Lifebit run via the MCP server pattern from Chapter 13.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*TBD will drop a screenshot at `assets/overview.png` here showing the
key result of this lesson. Reference it from this README as
`![overview](assets/overview.png){width=520}` once captured.*
:::

Pipelines have to run somewhere. This lesson is about the *where*, and
about a new way to think about what those somewheres really are.

:::{admonition} The framing
:class: tip

**Lifebit offers a new transport-layer protocol for science as a
service.** The internet has HTTP. Science is converging on something
similar — a layer that delivers compute + data + provenance, on demand,
with institutional login. The researcher describes the work; the
platform delivers the work.

Combined with the [MCP server](mcp-server.md) pattern, this is what
makes agentic AI for science *actually useful*: the agent drives the
CLI, the CLI runs on the transport layer, results come back to the
researcher's chat window.
:::

## The platforms covered

### Lifebit — the open-science transport layer (headline)

- Free with **institutional login** — a real on-ramp for academic and
  research labs.
- Runs Nextflow natively (your `nextflow/` lessons work as-is).
- Provides federated execution (your
  [federated-computing](federated-computing.md) lesson lands here).
- The combination of *free*, *institutional-login*, and
  *Nextflow-native* is what makes the "transport-layer for science"
  framing real for a working biomedical scientist today.

### CAVATICA

- Cloud platform widely used in pediatric and rare-disease research.
- Strong on data-sharing and study-cohort tooling.
- Nextflow workflows can be imported.

### All of Us Researcher Workbench

- Where ~1M-participant population data lives.
- R and Nextflow supported; **direct `git pull` is not**.
- The [bridge patterns](../bridges/index.md) section is written for
  exactly this constraint.

### NIH HPC (Biowulf) — a different category

Biowulf is *not* a platform in the same sense as Lifebit, CAVATICA, or
AoU. It's a SLURM-managed HPC cluster — you SSH in, write batch scripts,
and submit to the queue. It's the right tool for very-large or
GPU-heavy jobs. But it doesn't offer the *transport layer* abstraction
(no built-in data federation, no native MCP/agent surface). Mention it
where it fits; don't conflate it with the cloud platforms.

## Get on Lifebit (the institutional-login path)

::::{tab-set}

:::{tab-item} Mac / Windows browser
:sync: web

1. Go to **[lifebit.ai](https://lifebit.ai)** and choose
   *Sign in with institutional login*.
2. Pick your institution from the SSO list (NIH, your university, etc.).
3. Create a workspace; pick the *biomedical analysis* template.
4. Open the workspace's JupyterLab. You're in.
:::

:::{tab-item} CLI from your laptop
:sync: cli

```bash
# Once Lifebit gives you an API token / personal access token, you can
# orchestrate runs from your local terminal.
# Details will be filled in alongside TBD worked-example run.
```
:::

::::

## What this lesson builds

A grounded comparison of where to run different kinds of work, plus
the practical setup for getting started on Lifebit with institutional
login.

## The natural pairing

Platforms close the loop the rest of the lessons opened. Every CLI you
built, every container you wrote, every Nextflow module you composed —
they all run on one of these platforms. The [MCP server](mcp-server.md)
lesson is what makes them agent-driveable.

## Further reading

- [Lifebit](https://lifebit.ai/) — federated computing platform (this lesson's headline)
- [Seven Bridges CAVATICA](https://www.cavatica.org/) — pediatric research platform
- [All of Us Researcher Workbench](https://www.researchallofus.org/data-tools/workbench/)
- [Biowulf](https://hpc.nih.gov/) — NIH HPC (comparison: HPC vs cloud PaaS)
- [Terra](https://terra.bio/) — Broad Institute genomics platform
- [DNAnexus](https://www.dnanexus.com/) — commercial PaaS


## Where to next

← Back to the [Introduction](introduction.md), or browse the
[book chapters](../chapters/index.md) for full worked examples.
