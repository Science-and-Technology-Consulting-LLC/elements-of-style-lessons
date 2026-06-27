// main-limma-voom-contrasts.nf — standalone runner, Step 5 only.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_CONTRASTS } from './modules/limma-voom/contrasts.nf'

params.samplesheet = 'data/test-data/limma-voom-contrasts-samplesheet.csv'

workflow {
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.fit_rds), file(row.design_rds)) }

    LIMMA_VOOM_CONTRASTS(inputs).view()
}
