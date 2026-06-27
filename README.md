# Elements of Style — Lessons

**The book companion for *Elements of Style in Creating Workflows for
Biomedical Research in the Era of Agentic AI*** by Anne Deslattes Mays
(Springer Nature, 2026).

The lessons here are designed for **working biomedical scientists** at
every skill level — from summer researchers in their first terminal
session to PIs already shipping Nextflow pipelines. Each lesson is
topical, ships its own deliverables (containers, CLIs, Nextflow modules,
notebooks), and references its corresponding chapter in the book.

## The published site

**https://science-and-technology-consulting-llc.github.io/elements-of-style-lessons/**

## Repository structure

```
elements-of-style-lessons/
│
├── lessons/                        The teaching narratives (one dir per topic)
│   ├── introduction/
│   ├── elements-of-style-rules/
│   ├── command-line-and-git-bash/
│   ├── version-control/
│   ├── conda-environments/
│   ├── interactive-computing/
│   ├── reusable-clis/
│   ├── containers/
│   ├── nextflow-modules/
│   ├── nextflow-workflows/
│   ├── federated-computing/
│   ├── federated-learning/
│   ├── mcp-server/
│   ├── publishing-for-agents/
│   └── platforms/
│
├── container/                      Every container ships a CLI
│   ├── hello-py/                   Python — Typer
│   ├── hello-r/                    R — Rscript wrapping an R package
│   ├── scanpy-qc/                  Python — `qc`, `convert`
│   ├── limma-voom/                 R — 5 CLI verbs (prep-counts → contrasts)
│   └── mcp-nsforest-server/        Python — MCP server wrapping nsforest-cli
│
├── modules/                        Mirrors container/ — one .nf per CLI verb
│
├── main-<name>.nf                  Root-level runners — standalone per module +
│                                   stitched workflows (main-bulk-de.nf,
│                                   main-geo-to-h5ad.nf, …)
│
├── configs/                        test, docker, lifebit Nextflow profiles
├── scripts/                        helper utilities
│
├── case-studies/                   Threaded worked stories
│   ├── endometriosis/              GSE179640 bulk + scRNA-seq
│   └── oadr-autoantibody/          T1D federated (NIH-NLM/oadr-autoantibody)
│
├── bridges/                        AoU-style "can't git pull" patterns
├── data/                           shared sample / test fixtures
├── docs/                           Sphinx source → GitHub Pages
├── pyproject.toml                  console-script manifest
├── environment.yml                 conda env (eos-lessons)
└── .github/workflows/{docs,ci}.yml
```

## The four governing principles

1. **Container = single-purpose unit shipping a CLI.** Python = Typer.
   R = an R package (`R/` pure functions) + an Rscript entry point in
   `inst/scripts/`. No container without an honest `--help`.
2. **Module = thin wrapper around a CLI call.** Each `.nf` in `modules/`
   declares inputs/outputs, names the container, calls one CLI verb.
   No business logic in `.nf`.
3. **Workflow = composition of modules.** `main-<name>.nf` composes
   modules into a runnable pipeline. `main-bulk-de.nf` is the canonical
   example: 5 limma-voom modules → end-to-end pseudobulk DE.
4. **The story builds chapter by chapter.** *Reusable CLIs* introduces
   the pattern with `hello-py` + `hello-r`. *Containers* makes them real
   with `scanpy-qc` + `limma-voom`. *Nextflow modules* wraps them in
   `.nf`. *Nextflow workflows* composes them. *Federated / MCP / Platforms*
   stack on top.

## Build locally

```bash
conda env create -f environment.yml
conda activate eos-lessons
cd docs && make html
python -m http.server -d build/html 8000
# open http://localhost:8000
```

## Run a Nextflow module (smallest example)

```bash
nextflow run main-hello-py-greet.nf -profile test --name Annie
```

## License

MIT — see [LICENSE](LICENSE).

## Citation

> Deslattes Mays, A. (2026). *Elements of Style in Creating Workflows for
> Biomedical Research in the Era of Agentic AI*. Springer Nature.

---

*"Writing and building work like notes and letters to your future self."*
