// main-bulk-de.nf — STITCHED workflow.
//
// Composes all five limma-voom modules into the end-to-end
// pseudobulk DE pipeline:
//
//   prep_counts → make_design → run_voom → fit_lm → contrasts
//
// The output of each step feeds the next. This is the canonical
// "modules compose into workflows" lesson.
//
// For Lifebit deployment: if the platform requires a main.nf filename,
// copy or symlink this file to main.nf at deploy time.

nextflow.enable.dsl = 2

include { LIMMA_VOOM_PREP_COUNTS  } from './modules/limma-voom/prep_counts.nf'
include { LIMMA_VOOM_MAKE_DESIGN  } from './modules/limma-voom/make_design.nf'
include { LIMMA_VOOM_RUN_VOOM     } from './modules/limma-voom/run_voom.nf'
include { LIMMA_VOOM_FIT_LM       } from './modules/limma-voom/fit_lm.nf'
include { LIMMA_VOOM_CONTRASTS    } from './modules/limma-voom/contrasts.nf'

params.samplesheet = 'data/test-data/bulk-de-samplesheet.csv'
params.contrast    = 'CF-Control'

workflow {
    // Read one row per cell type, with the path to its h5ad.
    inputs = Channel
        .fromPath(params.samplesheet)
        .splitCsv(header: true)
        .map { row -> tuple(row.cell_type, file(row.h5ad)) }

    // Step 1: prep counts.
    prep = LIMMA_VOOM_PREP_COUNTS(inputs)

    // Step 2: make design. Wraps in the contrast spec.
    design_in = prep.map { ct, prep_rds -> tuple(ct, prep_rds, params.contrast) }
    design    = LIMMA_VOOM_MAKE_DESIGN(design_in)

    // Step 3: voom. Joins prep + design by cell_type.
    voom_in = prep
        .join(design)
        .map { ct, prep_rds, design_rds -> tuple(ct, prep_rds, design_rds) }
    voom = LIMMA_VOOM_RUN_VOOM(voom_in)

    // Step 4: fit. Joins voom + design.
    fit_in = voom
        .join(design)
        .map { ct, voom_rds, design_rds -> tuple(ct, voom_rds, design_rds) }
    fit = LIMMA_VOOM_FIT_LM(fit_in)

    // Step 5: contrasts. Final output.
    contrasts_in = fit
        .join(design)
        .map { ct, fit_rds, design_rds -> tuple(ct, fit_rds, design_rds) }
    LIMMA_VOOM_CONTRASTS(contrasts_in)
        .view { ct, csv -> "DE results: ${ct} → ${csv}" }
}
