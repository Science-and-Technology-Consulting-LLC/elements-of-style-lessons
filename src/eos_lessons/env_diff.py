"""Diff two `environment.yml` files and tell you what changed.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `conda-environments/`
Console script:   `eos-env-diff`
"""

import typer

app = typer.Typer(
    help="Diff two `environment.yml` files and tell you what changed.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-env-diff (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-env-diff: placeholder — see conda-environments/README.md")


if __name__ == "__main__":
    app()
