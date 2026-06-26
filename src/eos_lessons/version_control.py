"""Summarize the current Git repo: branch, dirty files, upstream, recent commits.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `version-control/`
Console script:   `eos-version-control`
"""

import typer

app = typer.Typer(
    help="Summarize the current Git repo: branch, dirty files, upstream, recent commits.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-version-control (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-version-control: placeholder — see version-control/README.md")


if __name__ == "__main__":
    app()
