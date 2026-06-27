# hello-r — the smallest R CLI container
#
# Mirrors hello-py exactly, but in R. Pure R functions live in R/. The
# Rscript entry point in inst/scripts/ parses argv and calls them.

FROM rocker/r-ver:4.3.2

# Install the R package from context/
COPY context/ /opt/hello-r/
RUN R -e "install.packages(c('docopt'), repos='https://cloud.r-project.org')" \
 && R CMD INSTALL /opt/hello-r/

# Put the Rscript on PATH so `hello-r-greet` resolves anywhere
RUN ln -s /usr/local/lib/R/site-library/helloR/scripts/hello-r-greet /usr/local/bin/hello-r-greet

ENTRYPOINT ["hello-r-greet"]
CMD ["--help"]
