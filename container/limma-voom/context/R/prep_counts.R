#' Step 1 — Prepare counts.
#'
#' Load an h5ad (single-cell) into a SingleCellExperiment, aggregate
#' to pseudobulk by (cell_type x sample_id), filter low-expression
#' genes, and return a DGEList-compatible matrix + sample metadata.
#'
#' PLACEHOLDER implementation. Real logic to be migrated from
#' `elements-of-style-workflows/containers/limma-voom/pseudobulk_de.R`.
#'
#' @param h5ad        Path to the input .h5ad file.
#' @param min_count   Minimum aggregated count per gene to keep (default 10).
#' @param min_samples Gene must hit min_count in at least this many samples (default 3).
#' @return A list with $counts (matrix) and $coldata (data.frame).
#' @export
prep_counts <- function(h5ad, min_count = 10, min_samples = 3) {
  message("[limma-voom] prep_counts placeholder — h5ad=", h5ad,
          " min_count=", min_count, " min_samples=", min_samples)
  list(counts = NULL, coldata = NULL)
}
