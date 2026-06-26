"""Inventory the platforms you have access to (Lifebit, CAVATICA, AoU, …).

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `platforms/`
Console script:   `eos-platforms`
"""

import typer

app = typer.Typer(
    help="Inventory the platforms you have access to (Lifebit, CAVATICA, AoU, …).",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-platforms (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-platforms: placeholder — see platforms/README.md")


if __name__ == "__main__":
    app()
