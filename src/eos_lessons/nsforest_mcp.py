"""MCP server wrapping nsforest-cli — the agentic-AI worked example.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `mcp-server/`
Console script:   `eos-mcp-nsforest`
"""

import typer

app = typer.Typer(
    help="MCP server wrapping nsforest-cli — the agentic-AI worked example.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-mcp-nsforest (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-mcp-nsforest: placeholder — see mcp-server/README.md")


if __name__ == "__main__":
    app()
