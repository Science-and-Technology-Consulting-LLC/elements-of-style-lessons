# hello-py — the smallest possible Typer CLI container
#
# Single-purpose, single-CLI, version-pinned. Built so the reusable-clis
# lesson can demonstrate the container + CLI pattern with nothing else
# in the way.

FROM python:3.11-slim

# Install the CLI package (editable copy of context/) into the image
COPY context/ /opt/hello-py/
RUN pip install --no-cache-dir /opt/hello-py/

# Default invocation prints --help so the user sees what the tool does
ENTRYPOINT ["hello-py"]
CMD ["--help"]
