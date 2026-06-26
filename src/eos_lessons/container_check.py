"""Inspect a Dockerfile/Singularity recipe against the one-container-one-job rule.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `containers/`
Console script:   `eos-container-check`
"""

import typer

app = typer.Typer(
    help="Inspect a Dockerfile/Singularity recipe against the one-container-one-job rule.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-container-check (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-container-check: placeholder — see containers/README.md")


if __name__ == "__main__":
    app()
