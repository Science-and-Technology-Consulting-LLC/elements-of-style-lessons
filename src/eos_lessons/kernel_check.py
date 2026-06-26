"""List Jupyter kernels visible to this env and report which conda env each runs in.

This CLI is a placeholder so the entry point in `pyproject.toml` resolves
and the structure is callable from day one. Annie will replace the
`main()` body with the real implementation.

Lesson directory: `interactive-computing/`
Console script:   `eos-kernel-check`
"""

import typer

app = typer.Typer(
    help="List Jupyter kernels visible to this env and report which conda env each runs in.",
    add_completion=False,
)


@app.command()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Print extra detail."),
) -> None:
    """Run eos-kernel-check (placeholder)."""
    if verbose:
        typer.echo("verbose mode on")
    typer.echo("eos-kernel-check: placeholder — see interactive-computing/README.md")


if __name__ == "__main__":
    app()
