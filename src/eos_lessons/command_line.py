"""Check that your terminal is happy (PATH, shell, basic tools).

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `command-line-and-git-bash/`
Console script:   `eos-command-line`
"""

import typer

app = typer.Typer(
    help="Check that your terminal is happy (PATH, shell, basic tools).",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-command-line (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-command-line: placeholder — see command-line-and-git-bash/README.md")


if __name__ == "__main__":
    app()
