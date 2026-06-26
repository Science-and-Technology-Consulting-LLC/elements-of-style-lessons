"""Publish a CLI to PyPI/GHCR with an agent-ready README and MCP manifest.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `publishing-for-agents/`
Console script:   `eos-publish`
"""

import typer

app = typer.Typer(
    help="Publish a CLI to PyPI/GHCR with an agent-ready README and MCP manifest.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-publish (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-publish: placeholder — see publishing-for-agents/README.md")


if __name__ == "__main__":
    app()
