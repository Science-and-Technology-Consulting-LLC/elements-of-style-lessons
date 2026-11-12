// main-hello-py-greet.nf — standalone runner for the hello-py greet module.
//
// Demonstrates the smallest possible Nextflow workflow that uses a module.
// `nextflow run main-hello-py-greet.nf -profile test --name Annie`

nextflow.enable.dsl = 2

include { HELLO_PY_GREET } from './modules/hello-py/greet.nf'

params.name = 'world'

workflow {
    HELLO_PY_GREET(Channel.of(params.name))
        .view { "greeting: $it" }
}
