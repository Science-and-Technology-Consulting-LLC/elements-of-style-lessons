"""scanpy-qc convert — convert between single-cell file formats.

PLACEHOLDER IMPLEMENTATION. Will handle MEX → h5ad (and h5 → h5ad) once
the original `scanpy_qc.py` is migrated in.
"""
from pathlib import Path

import typer


def convert(
    input: Path = typer.Option(..., "--input", "-i", help="Source file or directory."),
    output: Path = typer.Option(..., "--output", "-o", help="Destination .h5ad."),
    fmt: str = typer.Option(
        "auto", "--format",
        help="Source format: auto | mex | h5 | h5ad.",
    ),
) -> None:
    """Convert single-cell data into a .h5ad."""
    typer.echo(
        f"scanpy-qc convert — placeholder\n"
        f"  input  = {input}\n"
        f"  output = {output}\n"
        f"  format = {fmt}"
    )
