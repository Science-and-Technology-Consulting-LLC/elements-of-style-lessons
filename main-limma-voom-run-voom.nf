// main-limma-voom-run-voom.nf — standalone runner, Step 3 only.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_RUN_VOOM } from './modules/limma-voom/run_voom.nf'

params.samplesheet = 'data/test-data/limma-voom-voom-samplesheet.csv'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.prep_rds), file(row.design_rds)) }

    LIMMA_VOOM_RUN_VOOM(inputs).view()
}
