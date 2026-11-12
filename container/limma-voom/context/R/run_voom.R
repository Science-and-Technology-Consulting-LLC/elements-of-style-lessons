#' Step 3 — voom transformation.
#'
#' Normalise the library sizes (TMM by default; Robinson and Oshlack 2010),
#' then apply voom, which gives each observation a precision weight
#' (Law et al. 2014). This is the order the limma and edgeR user guides give.
#'
#' @param counts       Filtered counts matrix from prep_counts.
#' @param design       Design matrix from make_design.
#' @param norm_method  "TMM" (default) or "none".
#' @return An EList object.
#' @export
run_voom <- function(counts, design, norm_method = "TMM") {
  counts <- counts[, rownames(design), drop = FALSE]
  y <- edgeR::DGEList(counts = counts)
  if (!identical(norm_method, "none")) {
    y <- edgeR::calcNormFactors(y, method = norm_method)
  }
  limma::voom(y, design, plot = FALSE)
}
