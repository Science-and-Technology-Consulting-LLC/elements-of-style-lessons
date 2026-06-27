// main-limma-voom-prep-counts.nf — standalone runner, Step 1 only.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_PREP_COUNTS } from './modules/limma-voom/prep_counts.nf'

params.samplesheet = 'data/test-data/limma-voom-samplesheet.csv'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.h5ad)) }

    LIMMA_VOOM_PREP_COUNTS(inputs)
        .view()
}
