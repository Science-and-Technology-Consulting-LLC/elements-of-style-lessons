"""Wrap a single command as a Nextflow-ready `bin/` script with smoke test.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `nextflow/`
Console script:   `eos-nextflow-step`
"""

import typer

app = typer.Typer(
    help="Wrap a single command as a Nextflow-ready `bin/` script with smoke test.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-nextflow-step (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-nextflow-step: placeholder — see nextflow/README.md")


if __name__ == "__main__":
    app()
