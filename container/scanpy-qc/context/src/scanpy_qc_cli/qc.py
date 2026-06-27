"""scanpy-qc qc — QC, normalisation, clustering on a single sample.

The function below is both an importable Python function (callable from
a notebook) and the body of the `scanpy-qc qc` subcommand.

PLACEHOLDER IMPLEMENTATION. The full scientific logic — covering count
filtering, mitochondrial-percentage cutoff, normalisation, HVG selection,
PCA → neighbors → UMAP → Leiden — lives in the legacy script at
`elements-of-style-workflows/containers/scanpy-qc/scanpy_qc.py` and will
be migrated step by step into this file.
"""
from pathlib import Path

import typer


def qc(
    input: Path = typer.Option(
        ..., "--input", "-i",
        help="Path to 10x MEX directory or raw .h5ad file.",
    ),
    output: Path = typer.Option(
        ..., "--output", "-o",
        help="Path where the QC'd .h5ad will be written.",
    ),
    sample_id: str = typer.Option(
        ..., "--sample-id",
        help="Stable sample identifier; recorded in obs.",
    ),
    min_genes: int = typer.Option(
        200, "--min-genes",
        help="Drop cells expressing fewer than this many genes.",
    ),
    max_mt_pct: float = typer.Option(
        20.0, "--max-mt-pct",
        help="Drop cells whose mitochondrial fraction exceeds this %.",
    ),
    leiden_resolution: float = typer.Option(
        0.5, "--leiden-resolution",
        help="Leiden resolution parameter for clustering.",
    ),
) -> None:
    """Run QC, normalisation, and Leiden clustering on one sample."""
    typer.echo(
        f"scanpy-qc qc — placeholder\n"
        f"  input             = {input}\n"
        f"  output            = {output}\n"
        f"  sample_id         = {sample_id}\n"
        f"  min_genes         = {min_genes}\n"
        f"  max_mt_pct        = {max_mt_pct}\n"
        f"  leiden_resolution = {leiden_resolution}\n"
        f"  (Replace this body with the migrated scanpy logic.)"
    )
