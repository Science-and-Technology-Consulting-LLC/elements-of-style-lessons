// main-scanpy-qc-qc.nf — standalone runner for the scanpy-qc qc module.

nextflow.enable.dsl = 2

include { SCANPY_QC_QC } from './modules/scanpy-qc/qc.nf'

params.samplesheet = 'data/test-data/scanpy-qc-samplesheet.csv'

workflow {
    samples = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.sample_id, file(row.h5ad_path)) }

    SCANPY_QC_QC(samples)
        .view { sample_id, out -> "qc'd ${sample_id} → ${out}" }
}
