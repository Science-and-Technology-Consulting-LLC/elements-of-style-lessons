# scanpy-qc — Python container, one CLI with subcommands.
#
# Verbs: qc, convert. Each verb lives in its own file under
# context/src/scanpy_qc_cli/. The Typer app in main.py registers them.

FROM python:3.11-slim

# System deps needed by scanpy/anndata wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libhdf5-dev \
        zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

COPY context/ /opt/scanpy-qc/
RUN pip install --no-cache-dir /opt/scanpy-qc/

ENTRYPOINT ["scanpy-qc"]
CMD ["--help"]
