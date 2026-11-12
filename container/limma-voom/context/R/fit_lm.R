#' Step 4 — Fit the linear model.
#'
#' Fit one linear model for each gene on the voom-weighted values
#' (limma's `lmFit`). The contrast and the moderated statistics come in step 5.
#'
#' @param voom_e  The voom EList from run_voom.
#' @param design  The design matrix from make_design.
#' @return The fitted MArrayLM.
#' @export
fit_lm <- function(voom_e, design) {
  limma::lmFit(voom_e, design)
}
