// scanpy-qc · convert — calls `scanpy-qc convert` inside container/scanpy-qc.

process SCANPY_QC_CONVERT {
    container 'ghcr.io/science-and-technology-consulting-llc/scanpy-qc:0.1.0'

    input:
    tuple val(sample_id), path(input_file)

    output:
    tuple val(sample_id), path("${sample_id}.h5ad")

    script:
    """
    scanpy-qc convert --input ${input_file} --output ${sample_id}.h5ad
    """
}
