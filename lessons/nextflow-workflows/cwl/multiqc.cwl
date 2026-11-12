cwlVersion: v1.0
class: CommandLineTool
id: multiqc
requirements:
  - class: DockerRequirement
    dockerPull: 'ghcr.io/science-and-technology-consulting-llc/multiqc:v1.0.0'
  - class: InlineJavascriptRequirement
  - class: ResourceRequirement
    ramMin: ${ return inputs.ram * 1024 }
    coresMin: $(inputs.cores)

baseCommand: [multiqc]
arguments:
  - position: 1
    valueFrom: "--zip-data-dir"

inputs:
  fastqc_results: { type: Directory, inputBinding: {position: 99}, doc: "FastQC output folder" }
  flat:           { type: 'boolean?', default: true, inputBinding: { position: 2, prefix: "--flat" } }
  filename:       { type: 'string?', default: "report.multiqc", inputBinding: { position: 2, prefix: "--filename" } }
  cores:          { type: 'int?', default: 2 }
  ram:            { type: 'int?', default: 2 }
outputs:
  multiqc_html:
    type: File
    outputBinding:
      glob: $(inputs.filename).html
  multiqc_zip:
    type: File
    outputBinding:
      glob: $(inputs.filename)_data.zip
