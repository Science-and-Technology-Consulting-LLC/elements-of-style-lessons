// main-geo-to-h5ad.nf — STITCHED workflow.
//
// Downloads .h5 files from GEO and converts each to a clean .h5ad.
// Composes scanpy-qc convert (and any downstream modules added later).
//
// Migrated from elements-of-style-workflows/workflows/geo-to-h5ad/main.nf.
// The original lived as workflows/geo-to-h5ad/main.nf; that file will be
// retired in favor of this root-level main-geo-to-h5ad.nf which uses the
// shared modules/.

nextflow.enable.dsl = 2

include { SCANPY_QC_CONVERT } from './modules/scanpy-qc/convert.nf'

params.samplesheet = 'data/test-data/geo-to-h5ad-samplesheet.csv'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.sample_id, file(row.h5_path)) }

    SCANPY_QC_CONVERT(inputs)
        .view { sample_id, out -> "h5ad: ${sample_id} → ${out}" }
}
