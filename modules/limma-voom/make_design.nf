// limma-voom · make-design — Step 2 of 5.

process LIMMA_VOOM_MAKE_DESIGN {
    container 'ghcr.io/science-and-technology-consulting-llc/limma-voom:0.1.0'

    input:
    tuple val(cell_type), path(prep_rds), val(contrast)

    output:
    tuple val(cell_type), path("${cell_type}.design.rds")

    script:
    """
    limma-voom-make-design \\
        --coldata ${prep_rds} \\
        --contrast '${contrast}' \\
        --out ${cell_type}.design.rds
    """
}
