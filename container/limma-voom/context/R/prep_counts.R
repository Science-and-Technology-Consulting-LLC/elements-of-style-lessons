#' Step 1 — Prepare counts.
#'
#' Read an h5ad file into a SingleCellExperiment, sum the raw counts of the
#' cells of each sample into one pseudobulk sample, and drop genes that are
#' too low to test. Summing by biological replicate, not testing cell by
#' cell, is what Squair et al. (2021) recommend (doi:10.1038/s41467-021-25960-2).
#'
#' The file must have `cell_type`, `sample_id` and `condition` in `obs`.
#' The counts must be raw integers.
#'
#' @param h5ad        Path to the input .h5ad file.
#' @param min_count   A gene counts as expressed in a sample when its summed
#'                    count is at least this (default 10).
#' @param min_samples A gene is kept when it is expressed in at least this
#'                    many samples (default 3).
#' @return A list with $counts (genes by samples matrix) and $coldata
#'   (data.frame: sample_id, cell_type, condition, n_cells).
#' @export
prep_counts <- function(h5ad, min_count = 10, min_samples = 3) {
  if (!file.exists(h5ad)) stop("h5ad file not found: ", h5ad)
  sce <- zellkonverter::readH5AD(h5ad)

  need <- c("cell_type", "sample_id", "condition")
  missing <- setdiff(need, colnames(SummarizedExperiment::colData(sce)))
  if (length(missing) > 0) {
    stop("obs is missing: ", paste(missing, collapse = ", "),
         ". The file needs cell_type, sample_id and condition.")
  }

  assay_name <- if ("counts" %in% SummarizedExperiment::assayNames(sce)) "counts"
                else SummarizedExperiment::assayNames(sce)[1]
  x <- SummarizedExperiment::assay(sce, assay_name)
  probe <- as.matrix(x[seq_len(min(100, nrow(x))), seq_len(min(100, ncol(x)))])
  if (any(probe != round(probe))) {
    stop("assay '", assay_name, "' does not hold integer counts. ",
         "limma-voom needs raw counts.")
  }

  ids <- SummarizedExperiment::colData(sce)[, c("cell_type", "sample_id")]
  pb <- scuttle::aggregateAcrossCells(
    sce, ids = ids, use.assay.type = assay_name, statistics = "sum"
  )

  counts <- as.matrix(SummarizedExperiment::assay(pb, assay_name))
  cd <- SummarizedExperiment::colData(pb)
  coldata <- data.frame(
    sample_id = as.character(cd$sample_id),
    cell_type = as.character(cd$cell_type),
    condition = as.character(cd$condition),
    n_cells   = as.integer(cd$ncells),
    stringsAsFactors = FALSE
  )
  colnames(counts) <- paste(coldata$cell_type, coldata$sample_id, sep = "_")
  rownames(coldata) <- colnames(counts)

  keep <- rowSums(counts >= min_count) >= min_samples
  message("[limma-voom] ", ncol(counts), " pseudobulk samples; ",
          sum(keep), " of ", nrow(counts), " genes kept")
  list(counts = counts[keep, , drop = FALSE], coldata = coldata)
}
