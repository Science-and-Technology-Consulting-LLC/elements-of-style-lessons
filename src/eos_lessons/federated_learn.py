"""Run one round of federated learning across simulated silos.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `federated-learning/`
Console script:   `eos-federated-learn`
"""

import typer

app = typer.Typer(
    help="Run one round of federated learning across simulated silos.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-federated-learn (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-federated-learn: placeholder — see federated-learning/README.md")


if __name__ == "__main__":
    app()
