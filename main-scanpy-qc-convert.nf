// main-scanpy-qc-convert.nf — standalone runner for scanpy-qc convert.

nextflow.enable.dsl = 2

include { SCANPY_QC_CONVERT } from './modules/scanpy-qc/convert.nf'

params.samplesheet = 'data/test-data/scanpy-qc-samplesheet.csv'

workflow {
    samples = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.sample_id, file(row.input_path)) }

    SCANPY_QC_CONVERT(samples)
        .view { sample_id, out -> "converted ${sample_id} → ${out}" }
}
