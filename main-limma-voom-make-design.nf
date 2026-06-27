// main-limma-voom-make-design.nf — standalone runner, Step 2 only.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_MAKE_DESIGN } from './modules/limma-voom/make_design.nf'

params.samplesheet = 'data/test-data/limma-voom-design-samplesheet.csv'
params.contrast    = 'CF-Control'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.prep_rds), params.contrast) }

    LIMMA_VOOM_MAKE_DESIGN(inputs).view()
}
