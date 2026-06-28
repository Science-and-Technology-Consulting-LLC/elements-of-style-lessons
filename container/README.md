# Containers

Every container in this directory follows the same rule: **one container,
one job, one CLI.** The layout mirrors
[`Science-and-Technology-Consulting-LLC/sc-nsforest-qc-nf`](https://github.com/Science-and-Technology-Consulting-LLC/sc-nsforest-qc-nf).

## Layout

```
container/<name>/
├── Dockerfile
└── context/
    ├── env.yml                    Conda / pip / R dependency pin
    │
    ├── (Python containers)
    ├── setup.py                   installs the package + console script
    └── src/<name>_cli/
        ├── __init__.py
        ├── main.py                Typer app — registers each verb
        └── <verb>.py              one file per subcommand
    │
    └── (R containers)
    ├── DESCRIPTION                R package metadata
    ├── NAMESPACE
    ├── R/
    │   └── <verb>.R               pure R functions, no argv parsing
    └── inst/scripts/
        └── <name>-<verb>          Rscript entry point (parses argv, calls R/)
```

## What's here

| Container | Lang | Lesson | CLI verbs |
|-----------|------|--------|-----------|
| `hello-py/` | Python (Typer) | `reusable-clis` | `greet` |
| `hello-r/` | R (Rscript) | `reusable-clis` | `greet` |
| `scanpy-qc/` | Python (Typer) | `containers` | `qc`, `convert` |
| `limma-voom/` | R (Rscript) | `containers` | `prep-counts`, `make-design`, `run-voom`, `fit-lm`, `contrasts` |
| `mcp-nsforest-server/` | Python (MCP) | `mcp-server` | — (server) |

## The pattern

For Python: write one function per verb in `<verb>.py`. Register them in
`main.py` as Typer subcommands. The function is both an importable Python
function and the body of the subcommand. Same code, two callers.

For R: write one function per step in `R/<step>.R`. The function takes its
inputs as R arguments and returns its output. The Rscript in
`inst/scripts/` parses argv with `docopt` and calls the R function. The
function is importable from any R code (a notebook, a test); the Rscript
is callable from the shell, from Nextflow's `script:` block, and from an
AI agent through MCP.

This separation is what makes the limma-voom container ship **five**
independent CLI verbs — one per main step of the voom→fit→contrasts
process. Each verb gets its own Nextflow module in `../modules/limma-voom/`.

## See also

- [Containers lesson](../lessons/containers/README.md)
- [Reusable CLIs lesson](../lessons/reusable-clis/README.md)
- [Nextflow modules](../modules/) — every module here wraps exactly one
  CLI verb defined in this directory.
