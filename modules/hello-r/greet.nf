// hello-r · greet — calls `hello-r-greet` inside container/hello-r.

process HELLO_R_GREET {
    container 'ghcr.io/science-and-technology-consulting-llc/hello-r:0.1.0'

    input:
    val name

    output:
    stdout

    script:
    """
    hello-r-greet --name '${name}'
    """
}
