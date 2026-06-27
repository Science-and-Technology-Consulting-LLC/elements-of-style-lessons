"""mcp-nsforest-server — MCP server wrapping nsforest-cli."""
from setuptools import setup, find_packages

setup(
    name="mcp-nsforest-server",
    version="0.1.0",
    description="MCP server wrapping nsforest-cli for agent-driven NSForest runs.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "typer>=0.9",
        # MCP SDK pin to be added once the public release stabilises.
        # "mcp>=0.1",
    ],
    entry_points={
        "console_scripts": [
            "mcp-nsforest-server = mcp_nsforest_server.server:app",
        ],
    },
)
