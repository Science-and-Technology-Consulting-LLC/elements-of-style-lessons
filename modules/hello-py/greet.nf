// hello-py · greet — calls `hello-py greet` inside container/hello-py.
//
// This is the smallest possible Nextflow process. It does the three
// things every module here does: declare a container, declare I/O,
// call one CLI verb.

process HELLO_PY_GREET {
    container 'ghcr.io/science-and-technology-consulting-llc/hello-py:0.1.0'

    input:
    val name

    output:
    stdout

    script:
    """
    hello-py greet --name '${name}'
    """
}
