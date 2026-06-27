// limma-voom · prep-counts — Step 1 of 5.
// Calls `limma-voom-prep-counts` inside container/limma-voom.

process LIMMA_VOOM_PREP_COUNTS {
    container 'ghcr.io/science-and-technology-consulting-llc/limma-voom:0.1.0'

    input:
    tuple val(cell_type), path(h5ad)

    output:
    tuple val(cell_type), path("${cell_type}.prep.rds")

    script:
    """
    limma-voom-prep-counts --h5ad ${h5ad} --out ${cell_type}.prep.rds
    """
}
