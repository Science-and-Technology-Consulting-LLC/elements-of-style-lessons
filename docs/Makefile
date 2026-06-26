# Minimal makefile for Sphinx documentation
#
# Usage:
#   make html        # build HTML to build/html/
#   make clean       # clear build/
#   make linkcheck   # validate external links

SPHINXOPTS    ?= -W --keep-going -n
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
