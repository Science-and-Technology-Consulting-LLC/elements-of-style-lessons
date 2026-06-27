"""scanpy-qc — single-cell QC and h5ad conversion CLI."""
from setuptools import setup, find_packages

setup(
    name="scanpy-qc-cli",
    version="0.1.0",
    description="QC + h5ad conversion for single-cell data, as a Typer CLI.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "typer>=0.9",
        "scanpy>=1.9",
        "anndata>=0.10",
        "pandas>=2.0",
        "numpy>=1.26",
    ],
    entry_points={
        "console_scripts": [
            "scanpy-qc = scanpy_qc_cli.main:app",
        ],
    },
)
