"""hello-py greet — say hello.

This is the canonical "one verb per file" example. The function below is
both an importable Python function AND the body of the `hello-py greet`
subcommand. Same code, two callers.
"""
import typer


def greet(
    name: str = typer.Option("world", "--name", "-n", help="Who to greet."),
    shout: bool = typer.Option(False, "--shout", help="Use uppercase output."),
) -> None:
    """Print a friendly greeting."""
    message = f"Hello, {name}!"
    typer.echo(message.upper() if shout else message)
