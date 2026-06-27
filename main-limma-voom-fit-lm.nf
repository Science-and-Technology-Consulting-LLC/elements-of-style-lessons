// main-limma-voom-fit-lm.nf — standalone runner, Step 4 only.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_FIT_LM } from './modules/limma-voom/fit_lm.nf'

params.samplesheet = 'data/test-data/limma-voom-fit-samplesheet.csv'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.voom_rds), file(row.design_rds)) }

    LIMMA_VOOM_FIT_LM(inputs).view()
}
