"""hello-py — the smallest Typer CLI we can teach with."""
from setuptools import setup, find_packages

setup(
    name="hello-py-cli",
    version="0.1.0",
    description="A minimal Typer CLI for the reusable-clis lesson.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["typer>=0.9"],
    entry_points={
        "console_scripts": [
            "hello-py = hello_py_cli.main:app",
        ],
    },
)
