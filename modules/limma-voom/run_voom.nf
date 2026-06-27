// limma-voom · run-voom — Step 3 of 5.

process LIMMA_VOOM_RUN_VOOM {
    container 'ghcr.io/science-and-technology-consulting-llc/limma-voom:0.1.0'

    input:
    tuple val(cell_type), path(prep_rds), path(design_rds)

    output:
    tuple val(cell_type), path("${cell_type}.voom.rds")

    script:
    """
    limma-voom-run-voom \\
        --counts ${prep_rds} \\
        --design ${design_rds} \\
        --out ${cell_type}.voom.rds
    """
}
