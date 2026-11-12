cwlVersion: v1.0
class: Workflow
id: fastqc_multiqc_wf
requirements:
  - class: MultipleInputFeatureRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_reads:   { type: 'File[]', doc: "Input fastq files" }
  fastqc_outdir: { type: 'string?', default: "results", doc: "FastQC output folder" }
  noextract:     { type: 'boolean?', default: true, doc: "FastQC flag" }
  flat:          { type: 'boolean?', default: true, doc: "MultiQC static images" }
  filename:      { type: 'string?', default: "report.multiqc", doc: "MultiQC output prefix" }
  cores:         { type: 'int?', default: 2 }
  ram:           { type: 'int?', default: 2 }

outputs:
  fastqc_results: { type: Directory, outputSource: fastqc/fastqc_results }
  multiqc_zip:    { type: File,      outputSource: multiqc/multiqc_zip }
  multiqc_html:   { type: File,      outputSource: multiqc/multiqc_html }

steps:
  fastqc:
    run: fastqc.cwl
    in:
      input_reads: input_reads
      outdir:      fastqc_outdir
      noextract:   noextract
      cores:       cores
      ram:         ram
    out: [fastqc_results]
  multiqc:
    run: multiqc.cwl
    in:
      fastqc_results: fastqc/fastqc_results
      flat:           flat
      filename:       filename
      cores:          cores
      ram:            ram
    out: [multiqc_zip, multiqc_html]
