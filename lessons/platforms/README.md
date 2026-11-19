# Platforms: a transport layer for science as a service

*In the book: Section 6.6, Workflows on Cloud Platforms.*

Pipelines have to run somewhere. In this lesson we look at where, create an account on CloudOS (Lifebit), and then run a pipeline from a terminal.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [Publishing for agents](../publishing-for-agents/README.md), is done. The account pages need nothing from the earlier lessons, so you can also start here.
- An institutional email, such as a university or NIH address, for the sign-up.

### What you should see

You sign up for CloudOS with your institutional login, sign in, create a workspace and open JupyterLab. Then you save an API key with `cloudos configure` and submit a small job. Each page says what the screen or output should look like.

> **Picture to add:** the CloudOS home page after the first sign-in (save a screenshot of the signed-in page) (save as assets/overview.png)

### Where the files are

- `lessons/platforms/creating-a-cloudos-account.ipynb` and `.md`: sign up.
- `lessons/platforms/logging-into-cloudos.ipynb` and `.md`: sign in and open JupyterLab.
- `lessons/platforms/authenticating-on-cloudos.ipynb` and `.md`: API key and `cloudos configure`.
- `lessons/platforms/running-a-pipeline-on-cloudos.ipynb` and `.md`: import, submit, check, get results.
- `lessons/platforms/assets/`: pictures for this lesson.

## Steps to execute

1. [Creating a CloudOS account](creating-a-cloudos-account.md) (notebook: `creating-a-cloudos-account.ipynb`). Sign up for CloudOS with your institutional login.
2. [Logging into CloudOS](logging-into-cloudos.md) (notebook: `logging-into-cloudos.ipynb`). Sign in, create a workspace and open JupyterLab.
3. [Authenticating on CloudOS](authenticating-on-cloudos.md) (notebook: `authenticating-on-cloudos.ipynb`). Get an API key and run `cloudos configure`.
4. [Running a pipeline on CloudOS](running-a-pipeline-on-cloudos.md) (notebook: `running-a-pipeline-on-cloudos.ipynb`). Import a pipeline from GitHub, submit a job, check it and get the results.

## Ask an AI assistant

*Optional.* Please read [Using the AI prompts](../introduction/README.md) first.

**Ask it to explain.**

```text
Explain what a platform such as Lifebit CloudOS adds to running Nextflow on my own computer: where the data are, who pays, how results are kept. Keep it to ten lines.
```

**Ask it to build.**

```text
I have a Nextflow workflow in a GitHub repository. Write the steps, in order, to run it on <platform>: how to link the repository, which parameters to set, where to put a secret such as a token, and how to find the results. Ask me for what you cannot know. Tell me where you are unsure.
```

**Ask it to review.**

```text
Review this plan to run my workflow on a platform. Is a secret printed in a log or passed on a command line? Is the container image pinned? Could a rerun overwrite earlier results? What will it cost if the memory is set as shown? List each.

<paste plan>
```


## Further reading

- [Lifebit](https://lifebit.ai/): federated computing platform
- [All of Us Researcher Workbench](https://www.researchallofus.org/data-tools/workbench/)
- [Biowulf](https://hpc.nih.gov/): NIH high-performance computing
- [Terra](https://terra.bio/): Broad Institute genomics platform
- [DNAnexus](https://www.dnanexus.com/): commercial platform

## Supplementary information

### The framing

**Lifebit offers a transport-layer protocol for science as a service.** The internet has HTTP. Science is converging on a similar layer that delivers compute, data and provenance on demand, with institutional login. Combined with the [MCP server](../mcp-server/README.md) pattern, an assistant drives the CLI, the CLI runs on the transport layer, and results return to the researcher's chat.

### The platforms covered

**Lifebit, the open-science transport layer (headline).**

- Free with **institutional login**, a real on-ramp for academic and research labs.
- Runs Nextflow natively, so your `nextflow/` lessons work as they are.
- Provides federated execution. Your [federated-computing](../federated-computing/README.md) lesson lands here.

**All of Us Researcher Workbench.**

- About a million participants' population data lives here.
- R and Nextflow are supported. A direct `git pull` is not.
- The bridge patterns section of the book is written for that limit.

> **Check:** the earlier page linked to `../../bridges/index.md`, which does not exist in this repository. Where should the bridge patterns link go?

**NIH HPC (Biowulf), a different category.** Biowulf is a SLURM-managed high-performance computing cluster. You log in with SSH, write batch scripts and submit them to the queue. It suits very large or GPU-heavy jobs. It has no built-in data federation or agent surface, so do not group it with the cloud platforms.

### Get on Lifebit

- Sign up: <https://cloudos.lifebit.ai/register>
- Sign in: <https://cloudos.lifebit.ai/login>
- Institutional access requests: <https://lifebit.ai/contact> (if your institution's sign-in is not listed)

The pages in this lesson walk through these steps. In a browser: sign up, choose *Sign in with institutional login*, pick your institution, create a workspace with the *biomedical analysis* template and open its JupyterLab. Then, from your laptop's terminal:

```bash
pip install cloudos-cli
cloudos configure   # asks for your API key; see authenticating-on-cloudos.md
```

### Pairs well with

Platforms close the loop. Every command-line tool, container and Nextflow module you built runs on one of these platforms, and the [MCP server](../mcp-server/README.md) lesson makes them drivable by an assistant.

## Next

[Case studies](../../case-studies/README.md): five real pipelines that use everything you have learned.
