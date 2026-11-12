"""mcp-nsforest-server entry point.

This is the agentic-AI worked example. The MCP server exposes nsforest-cli
verbs as MCP tools so an AI agent (Claude, ChatGPT, …) can drive them in
natural language.

PLACEHOLDER. The MCP server wiring is not written yet.
"""
import typer

app = typer.Typer(
    help="MCP server wrapping nsforest-cli (placeholder).",
    add_completion=False,
)


@app.command()
def main(
    nsforest_bin: str = typer.Option(
        "nsforest-cli", "--nsforest-bin",
        help="Path to the nsforest-cli executable to wrap.",
    ),
    transport: str = typer.Option(
        "stdio", "--transport",
        help="MCP transport: stdio | http.",
    ),
) -> None:
    """Run the MCP server."""
    typer.echo(
        f"mcp-nsforest-server (placeholder)\n"
        f"  wrapping  = {nsforest_bin}\n"
        f"  transport = {transport}\n"
        f"  (Replace with real MCP server once SDK is pinned.)"
    )


if __name__ == "__main__":
    app()
