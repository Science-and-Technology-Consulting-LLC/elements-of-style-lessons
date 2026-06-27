#' Step 2 — Build the design matrix.
#'
#' Given the pseudobulk coldata and a contrast specification, return a
#' model matrix and a contrast matrix that the later steps can consume.
#'
#' PLACEHOLDER.
#'
#' @param coldata   A data.frame of per-sample metadata.
#' @param contrast  String contrast spec, e.g., "CF-Control".
#' @return A list with $design (matrix) and $contrasts (matrix).
#' @export
make_design <- function(coldata, contrast) {
  message("[limma-voom] make_design placeholder — contrast=", contrast)
  list(design = NULL, contrasts = NULL)
}
