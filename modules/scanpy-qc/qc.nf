// scanpy-qc · qc — calls `scanpy-qc qc` inside container/scanpy-qc.

process SCANPY_QC_QC {
    container 'ghcr.io/science-and-technology-consulting-llc/scanpy-qc:0.1.0'

    input:
    tuple val(sample_id), path(input_h5ad)

    output:
    tuple val(sample_id), path("${sample_id}.qc.h5ad")

    script:
    """
    scanpy-qc qc \\
        --input  ${input_h5ad} \\
        --output ${sample_id}.qc.h5ad \\
        --sample-id ${sample_id}
    """
}
