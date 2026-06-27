"""scanpy-qc CLI entry point.

Mirrors the sc-nsforest-qc-nf pattern: one Typer app, one file per verb.
Logic in `qc.py` and `convert.py`; this file only does registration.
"""
import typer

from . import qc as _qc
from . import convert as _convert

app = typer.Typer(
    help="Single-cell QC and h5ad conversion. One container, one job.",
    add_completion=False,
)

app.command(name="qc")(_qc.qc)
app.command(name="convert")(_convert.convert)


if __name__ == "__main__":
    app()
