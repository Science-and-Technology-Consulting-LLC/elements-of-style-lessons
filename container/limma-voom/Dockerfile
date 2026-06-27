# limma-voom — R container, ONE R package, FIVE CLI verbs.
#
# Each main step of the voom→fit→contrasts pipeline is its own Rscript
# entry point in inst/scripts/. The pure R functions live in R/. The
# Nextflow modules in modules/limma-voom/ wrap exactly one verb each.

FROM bioconductor/bioconductor_docker:RELEASE_3_18

# Install R-side dependencies
RUN R -e "install.packages(c('docopt', 'optparse'), repos='https://cloud.r-project.org')" \
 && R -e "BiocManager::install(c('limma', 'edgeR', 'SingleCellExperiment', 'scuttle', 'zellkonverter'), update=FALSE, ask=FALSE)"

# Install the limma-voom package itself
COPY context/ /opt/limma-voom/
RUN R CMD INSTALL /opt/limma-voom/

# Expose the 5 Rscript entries as commands on PATH
RUN for verb in prep-counts make-design run-voom fit-lm contrasts; do \
        ln -s /usr/local/lib/R/site-library/limmaVoomCLI/scripts/limma-voom-${verb} /usr/local/bin/limma-voom-${verb}; \
    done

# Default: show the multi-step help
RUN echo '#!/usr/bin/env bash\necho "limma-voom container — 5 CLI verbs"\necho ""\necho "Available verbs (each one is its own command on PATH):"\necho "  limma-voom-prep-counts   Step 1: load counts, build SCE, filter low-expression"\necho "  limma-voom-make-design   Step 2: build the design matrix from a phenotype CSV"\necho "  limma-voom-run-voom      Step 3: voom transformation"\necho "  limma-voom-fit-lm        Step 4: fit the linear model"\necho "  limma-voom-contrasts     Step 5: apply contrasts, write results"\necho ""\necho "Add --help to any verb for its full usage."' > /usr/local/bin/limma-voom \
 && chmod +x /usr/local/bin/limma-voom

ENTRYPOINT ["limma-voom"]
