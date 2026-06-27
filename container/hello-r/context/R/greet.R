#' Say hello
#'
#' Pure R function. No argv parsing. Importable from any other R code
#' (a notebook, a test, another package) the same way the Rscript entry
#' calls it.
#'
#' @param name Who to greet.
#' @param shout If TRUE, return the greeting in uppercase.
#' @return The greeting, as a character string.
#' @export
greet <- function(name = "world", shout = FALSE) {
  message <- paste0("Hello, ", name, "!")
  if (isTRUE(shout)) toupper(message) else message
}
