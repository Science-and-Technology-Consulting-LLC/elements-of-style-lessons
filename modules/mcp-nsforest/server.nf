// mcp-nsforest · server — runs the MCP server as a long-lived process.
//
// Typically used outside Nextflow (an agent connects to it directly)
// but exposed here as a module for completeness and for headless tests.

process MCP_NSFOREST_SERVER {
    container 'ghcr.io/science-and-technology-consulting-llc/mcp-nsforest-server:0.1.0'

    input:
    val transport

    output:
    stdout

    script:
    """
    mcp-nsforest-server --transport ${transport}
    """
}
