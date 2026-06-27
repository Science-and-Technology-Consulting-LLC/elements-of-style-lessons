"""hello-py CLI entry point.

This is the Typer app every subcommand registers against. Keep this file
minimal — one subcommand per topic file. Mirrors the sc-nsforest-qc-nf
pattern at container/nsforest/context/src/nsforest_cli/main.py.
"""
import typer

from . import greet as _greet

app = typer.Typer(
    help="The smallest Typer CLI we can teach with. One verb per file.",
    add_completion=False,
)

# Register subcommands. Each verb lives in its own file under this package.
app.command(name="greet")(_greet.greet)


if __name__ == "__main__":
    app()
