# Nextflow and CWL: shared structure, shared elements

You will compare one pipeline step written in Nextflow and in the Common Workflow Language, so that you see why a well-built container can move between workflow languages.

## Start here

### What you will do

- Read the goal and the strategy behind the course.
- See what Nextflow and CWL have in common.
- Compare one FastQC step side by side.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- This walkthrough is mostly reading and installs nothing. It helps to have done [Building a Nextflow workflow](building-a-nextflow-workflow.md) and [Building a CWL workflow](building-a-cwl-workflow.md) first.
- The kernel name at the top right of the notebook says **Bash**. If it does not, click the name and choose **Bash**.

## Steps to execute

### Read the goal

*Why:* everything in this course serves one aim. Make our science *as platform-independent and workflow-independent as possible*, in service of open, reproducible science.

**What you should take away:** the aim is not a particular tool. It is work that survives a change of tool.

### Read the strategy

*Why:* one habit makes the aim real. **Containerise at the logical, single-purpose level.** One container ([Containers](../containers/README.md)) does one job and has one command-line interface. Do that, and the same container fits into a Nextflow module, a CWL step, a Snakemake rule, or a plain `podman run` on your laptop. The computation stays identical. Only the language that joins the steps changes.

The Elements of Style calls this the *fan-in* shape: many workflow languages, all using the same container-level building blocks. See also [Reusable command-line tools](../reusable-clis/README.md).

**What you should take away:** the container is the stable part. The workflow language is the replaceable part.

### See what Nextflow and CWL share

*Why:* once you see the shared parts, a new workflow language looks familiar. Both languages describe the same three things:

- **Inputs**: the parameters and files the step uses.
- **Outputs**: the files or values the step makes.
- **Scripts or commands**: what the step actually runs, inside a container.

They differ in *syntax* and in *how data moves between steps*: Nextflow uses channels ([Building a Nextflow workflow](building-a-nextflow-workflow.md)), and CWL writes each step-to-step connection down explicitly. The scientific containers are identical.

**What you should take away:** three shared primitives, and one real difference, the wiring.

### Compare one FastQC step side by side

*Why:* seeing the two versions next to each other makes the shared structure concrete. Match up the lines: the container, the command, the input and the output appear in both.

**Nextflow (DSL2):**

```groovy
process fastqc {
    container 'ghcr.io/<owner>/fastqc:v0.11.9'
    input:
      path reads
    output:
      path "*_fastqc.{zip,html}"
    script:
      """
      fastqc $reads
      """
}
```

**CWL:**

```yaml
class: CommandLineTool
id: fastqc
requirements:
  - class: DockerRequirement
    dockerPull: 'ghcr.io/<owner>/fastqc:v0.11.9'
baseCommand: fastqc
inputs:
  input_reads: { type: 'File[]', inputBinding: { position: 99 } }
outputs:
  fastqc_results:
    type: Directory
    outputBinding:
      glob: results
```

**What you should see:** different syntax, **same container, same command, same intent.** `<owner>` stands for your own registry name.

### Read why this discipline pays off

- **Reproducible science.** The container fixes the tool version. The workflow language only organises the steps.
- **Cleaner, testable parts.** Each container can be run with `--help` and smoke-tested without any workflow engine.
- **Reuse in other workflows.** The container you built for a Nextflow step drops straight into someone else's CWL pipeline, a Snakemake rule or a plain shell script.

This is why the curriculum spends so much time on the **containers** and **reusable-clis** lessons before it touches a `.nf` file. Those are the parts that carry the load. Workflow syntax is a thin layer on top.

### If something goes wrong

- **A tool shows `MISSING` in the tool check (the *Check your tools* step of [Let's dive in](../introduction/lets-dive-in.md)).** This walkthrough does not need it. If you want it, install it with the lesson that covers it (the lesson list is on the [Introduction page](../introduction/README.md)).
- **The Bash tile is missing in JupyterLab.** Repeat step 4 of the [Introduction page](../introduction/README.md) and restart JupyterLab.

## Next

[Nextflow modules and features](../nextflow-modules/README.md): how a one-file script grows into `modules/` and `main-*.nf`.
