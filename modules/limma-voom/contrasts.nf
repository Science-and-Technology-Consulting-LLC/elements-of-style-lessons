// limma-voom · contrasts — Step 5 of 5. Final output is a CSV (RFC 4180).

process LIMMA_VOOM_CONTRASTS {
    container 'ghcr.io/science-and-technology-consulting-llc/limma-voom:0.1.0'

    input:
    tuple val(cell_type), path(fit_rds), path(design_rds)

    output:
    tuple val(cell_type), path("${cell_type}.de.csv")

    script:
    """
    limma-voom-contrasts \\
        --fit ${fit_rds} \\
        --design ${design_rds} \\
        --out ${cell_type}.de.csv
    """
}
