# Platforms — a transport-layer protocol for science as a service

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

## What this lesson builds

A grounded comparison of where to run different kinds of work, plus
the practical setup for getting started on Lifebit with institutional
login.

## The natural pairing

Platforms close the loop the rest of the lessons opened. Every CLI you
built, every container you wrote, every Nextflow module you composed —
they all run on one of these platforms. The [MCP server](mcp-server.md)
lesson is what makes them agent-driveable.

## Where to next

← Back to the [Introduction](introduction.md), or browse the
[book chapters](../chapters/index.md) for full worked examples.
