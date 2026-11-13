#' Step 2 — Build the design matrix and the contrast.
#'
#' One column for each condition (a model without an intercept) and one
#' contrast, "test minus control". The contrast is written "Test-Control",
#' for example "EuE-Ctrl".
#'
#' Each condition needs at least `min_replicates` pseudobulk samples. Fewer
#' samples cannot give a usable variance estimate, and the step stops
#' with a message.
#'
#' @param coldata        data.frame from prep_counts: sample_id, cell_type,
#'                       condition, n_cells.
#' @param contrast       String "Test-Control".
#' @param min_replicates Smallest number of samples per condition (default 3).
#' @return A list with $design (matrix), $contrasts (matrix, one column),
#'   $cell_type and $contrast.
#' @export
make_design <- function(coldata, contrast, min_replicates = 3) {
  parts <- strsplit(contrast, "-", fixed = TRUE)[[1]]
  if (length(parts) != 2 || any(parts == "")) {
    stop("contrast must be 'Test-Control', for example 'EuE-Ctrl'. Got: ",
         contrast)
  }
  test <- parts[1]; control <- parts[2]
  for (lvl in parts) {
    if (make.names(lvl) != lvl) {
      stop("condition name '", lvl, "' is not a plain name (letters, digits, ",
           "'.' and '_'; it cannot start with a digit).")
    }
  }

  present <- unique(coldata$condition)
  absent <- setdiff(parts, present)
  if (length(absent) > 0) {
    stop("condition not in the data: ", paste(absent, collapse = ", "),
         ". Found: ", paste(present, collapse = ", "))
  }
  n <- table(factor(coldata$condition, levels = parts))
  if (any(n < min_replicates)) {
    stop("each condition needs at least ", min_replicates, " samples. ",
         paste(names(n), n, sep = " = ", collapse = ", "))
  }

  condition <- factor(coldata$condition, levels = c(control, test))
  keep <- !is.na(condition)
  design <- stats::model.matrix(~ 0 + condition[keep])
  colnames(design) <- levels(condition)
  rownames(design) <- rownames(coldata)[keep]
  contrasts <- limma::makeContrasts(contrasts = paste0(test, " - ", control),
                                    levels = design)
  colnames(contrasts) <- contrast

  list(design = design, contrasts = contrasts,
       cell_type = paste(unique(coldata$cell_type), collapse = ","),
       contrast = contrast)
}
