# Nextflow modules

Every `.nf` file here wraps **exactly one CLI verb** defined in
[`../container/`](../container/). The layout mirrors `container/` 1:1.

| Module | Wraps | Container |
|--------|-------|-----------|
| `hello-py/greet.nf` | `hello-py greet` | `hello-py` |
| `hello-r/greet.nf` | `hello-r-greet` | `hello-r` |
| `scanpy-qc/qc.nf` | `scanpy-qc qc` | `scanpy-qc` |
| `scanpy-qc/convert.nf` | `scanpy-qc convert` | `scanpy-qc` |
| `limma-voom/prep_counts.nf` | `limma-voom-prep-counts` | `limma-voom` |
| `limma-voom/make_design.nf` | `limma-voom-make-design` | `limma-voom` |
| `limma-voom/run_voom.nf` | `limma-voom-run-voom` | `limma-voom` |
| `limma-voom/fit_lm.nf` | `limma-voom-fit-lm` | `limma-voom` |
| `limma-voom/contrasts.nf` | `limma-voom-contrasts` | `limma-voom` |
| `mcp-nsforest/server.nf` | `mcp-nsforest-server` | `mcp-nsforest-server` |

## The rule

A module declares three things: a `container`, an `input:` block, an
`output:` block. The `script:` block is one line — the CLI call. No
business logic in `.nf` files. The logic lives in the container's `R/`
or `src/`.

## See also

- [`../container/`](../container/) — the containers each of these wraps.
- [Nextflow modules lesson](../lessons/nextflow-modules/README.md)
- [Nextflow workflows lesson](../lessons/nextflow-workflows/README.md)
- Root-level `main-*.nf` runners — one per module here, for standalone testing.
