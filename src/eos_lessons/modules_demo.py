"""Scaffold or inspect a Nextflow module (.nf + bin/ + smoke test).

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `nextflow/modules/`
Console script:   `eos-modules`
"""

import typer

app = typer.Typer(
    help="Scaffold or inspect a Nextflow module (.nf + bin/ + smoke test).",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-modules (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-modules: placeholder — see nextflow/modules/README.md")


if __name__ == "__main__":
    app()
