"""Run a workflow against a federated data manifest, one site at a time.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `federated-computing/`
Console script:   `eos-federated-compute`
"""

import typer

app = typer.Typer(
    help="Run a workflow against a federated data manifest, one site at a time.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-federated-compute (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-federated-compute: placeholder — see federated-computing/README.md")


if __name__ == "__main__":
    app()
