# NLM-CKN — the trustworthy Cell Knowledge Network

The largest worked example this book companion touches:

**[NIH-NLM/nlm-ckn](https://github.com/NIH-NLM/nlm-ckn)** — the NIH National
Library of Medicine's Cell Knowledge Network.

Live site: [https://nlm-ckn.org](https://nlm-ckn.org)
GitHub Pages: [https://nih-nlm.github.io/nlm-ckn/](https://nih-nlm.github.io/nlm-ckn/)

## What NLM-CKN is

A trustworthy, data-driven biomedical knowledge base of **cell phenotypes**
for the National Library of Medicine — the graph-database backbone that
lets a working scientist (or an agent acting on their behalf) ask
questions of the form *"which cell types express X under Y condition, and
where is the primary evidence for that claim?"* and receive answers with
citations.

Every lesson in this curriculum feeds into NLM-CKN somehow:

- The **containers, modules, and workflows** produce the cell-type-marker
  results NLM-CKN ingests.
- The **CI + docker-publish** pipelines are how ingestion nodes stay in
  sync with upstream tools.
- The **MCP server** pattern is how the graph becomes *agent-driveable* —
  the [`NLM-CKN-MCP`](https://github.com/NIH-NLM/NLM-CKN-MCP) server
  exposes graph queries as MCP tools so an AI agent can traverse the
  knowledge base while chatting with a scientist.

## Reference chapter

Scheuermann, R. H., Deslattes Mays, A., Diller, M., LeClair, R.,
Spear, W., & Zhang, Y. *A trustworthy data-driven biomedical knowledge
base of cell phenotypes for the National Library of Medicine.* In
**Knowledge Graphs in U.S. Government Agencies**, Springer, forthcoming.

Every lesson in this curriculum that touches the trustworthiness /
provenance / knowledge-graph story cites this chapter.

## Which lessons this case study uses

The full stack:

| Layer | Uses lesson | Demonstrates |
|---|---|---|
| Source scientific containers | [containers](../../lessons/containers/README.md) | `scanpy-qc`, `nsforest`, `limma-voom`, and more |
| Pipeline composition | [nextflow-workflows](../../lessons/nextflow-workflows/README.md) | `NIH-NLM/sc-nsforest-qc-nf` — the reference workflow this whole curriculum's `container/` + `modules/` + `main-*.nf` shape mirrors |
| Publishing scientific results as an API | [mcp-server](../../lessons/mcp-server/README.md) | [`NIH-NLM/NLM-CKN-MCP`](https://github.com/NIH-NLM/NLM-CKN-MCP) |
| Publishing to be readable by agents | [publishing-for-agents](../../lessons/publishing-for-agents/README.md) | machine-readable schemas + provenance |
| Federated computation across sites | [federated-computing](../../lessons/federated-computing/README.md) | how ingestion works across institutional data owners |
| Documentation as a first-class deliverable | [documentation](../../lessons/documentation/README.md) | [nih-nlm.github.io/nlm-ckn](https://nih-nlm.github.io/nlm-ckn/) |
| Continuous integration | [continuous-integration](../../lessons/continuous-integration/README.md) | every push builds, deploys, and re-ingests |
| Platforms | [platforms](../../lessons/platforms/README.md) | the transport layer for federated ingestion |

## The driving question

> *If a paper cites a specific cell-type marker, can a reader (or an
> agent) traverse from the marker back to the primary evidence — every
> preprocessing step, every container tag, every model version, every
> statistical assumption?*

The answer is the trustworthiness framework Scheuermann et al. describe.
This case study is the *entire book* condensed into one production
system.

## See also

- The [MCP-server lesson](../../lessons/mcp-server/README.md) — how the
  graph becomes conversational for an agent.
- The [publishing-for-agents lesson](../../lessons/publishing-for-agents/README.md).
- The [documentation lesson](../../lessons/documentation/README.md) — the
  Sphinx-and-MyST toolchain that renders both NLM-CKN's public site and
  this one.
