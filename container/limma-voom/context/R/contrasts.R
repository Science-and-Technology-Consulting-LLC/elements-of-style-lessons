#' Step 5 — Apply contrasts and emit results.
#'
#' Given a fitted model and a contrast matrix, run `contrasts.fit` →
#' `eBayes` → `topTable`, returning a results data.frame.
#'
#' PLACEHOLDER.
#'
#' @param fit        Fitted MArrayLM from fit_lm.
#' @param contrasts  Contrast matrix from make_design.
#' @return A data.frame of DE results (or NULL placeholder).
#' @export
contrasts_table <- function(fit, contrasts) {
  message("[limma-voom] contrasts_table placeholder")
  NULL
}
