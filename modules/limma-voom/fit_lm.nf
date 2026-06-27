// limma-voom · fit-lm — Step 4 of 5.

process LIMMA_VOOM_FIT_LM {
    container 'ghcr.io/science-and-technology-consulting-llc/limma-voom:0.1.0'

    input:
    tuple val(cell_type), path(voom_rds), path(design_rds)

    output:
    tuple val(cell_type), path("${cell_type}.fit.rds")

    script:
    """
    limma-voom-fit-lm \\
        --voom ${voom_rds} \\
        --design ${design_rds} \\
        --out ${cell_type}.fit.rds
    """
}
