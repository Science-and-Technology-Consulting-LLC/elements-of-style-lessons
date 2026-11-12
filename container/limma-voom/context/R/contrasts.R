#' Step 5 — Apply the contrast and emit the results.
#'
#' `contrasts.fit`, then `eBayes` (which moves each gene's variance toward
#' the average, Smyth 2004), then `topTable` for every gene.
#'
#' @param fit        Fitted MArrayLM from fit_lm.
#' @param contrasts  Contrast matrix from make_design (one column).
#' @param cell_type  Label written to the `cell_type` column (optional).
#' @param fdr        Adjusted p-value threshold for `significant` (default 0.05).
#' @param logfc      Absolute log2 fold-change threshold (default 1).
#' @return A data.frame: gene, logFC, AveExpr, t, P.Value, adj.P.Val, B,
#'   cell_type, significant.
#' @export
contrasts_table <- function(fit, contrasts, cell_type = NA_character_,
                            fdr = 0.05, logfc = 1) {
  fit2 <- limma::contrasts.fit(fit, contrasts)
  fit2 <- limma::eBayes(fit2)
  res <- limma::topTable(fit2, coef = 1, number = Inf, sort.by = "P")
  res <- cbind(gene = rownames(res), res, stringsAsFactors = FALSE)
  rownames(res) <- NULL
  res$cell_type <- cell_type
  res$significant <- res$adj.P.Val < fdr & abs(res$logFC) > logfc
  res
}
