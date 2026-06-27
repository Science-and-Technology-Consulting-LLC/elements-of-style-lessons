// main-hello-r-greet.nf — standalone runner for the hello-r greet module.
//
// Same shape as main-hello-py-greet.nf, but uses the R container.
// Demonstrates that the module pattern is identical across languages.

nextflow.enable.dsl = 2

include { HELLO_R_GREET } from './modules/hello-r/greet.nf'

params.name = 'world'

workflow {
    HELLO_R_GREET(Channel.of(params.name))
        .view { "greeting: $it" }
}
