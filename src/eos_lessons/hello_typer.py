"""A minimal Typer CLI — the teaching exemplar for the reusable-clis lesson.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `reusable-clis/`
Console script:   `eos-hello`
"""

import typer

app = typer.Typer(
    help="A minimal Typer CLI — the teaching exemplar for the reusable-clis lesson.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-hello (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-hello: placeholder — see reusable-clis/README.md")


if __name__ == "__main__":
    app()
