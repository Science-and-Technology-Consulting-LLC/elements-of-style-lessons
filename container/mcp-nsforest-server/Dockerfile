# mcp-nsforest-server — MCP server wrapping nsforest-cli.
#
# The agentic-AI worked example. A researcher chats with an AI agent;
# the agent calls into this MCP server, which calls nsforest-cli, which
# runs the NSForest marker-discovery workflow.

FROM python:3.11-slim

COPY context/ /opt/mcp-nsforest-server/
RUN pip install --no-cache-dir /opt/mcp-nsforest-server/

ENTRYPOINT ["mcp-nsforest-server"]
CMD ["--help"]
