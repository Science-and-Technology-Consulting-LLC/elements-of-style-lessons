# Other places to run these lessons

Further information. You do not need this page if you have a Mac, a Windows computer with Git Bash, or a Linux computer. Start with [Let's dive in](lets-dive-in.md).

Use this page if you have no terminal of your own, or when your work grows beyond your laptop.

## Google Cloud Shell

[Google Cloud Shell](https://shell.cloud.google.com/) is a free Bash terminal in your web browser. It is a way to practise when you cannot install anything.

1. Open <https://shell.cloud.google.com/>.
2. Sign in with any Google account.
3. A terminal opens at the bottom of the page. Run the clone commands from "Before you begin" in your notebook.
4. Install conda and create the `eos` environment. Miniconda is not pre-installed there:

   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3
   exec -l bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   conda env create -f eos.yml
   conda activate eos
   ```

   The full walkthrough is [Creating a conda environment](../conda-environments/creating-a-conda-environment.md).

Things to know:

- Its disk is small and is wiped between sessions. Push your work to GitHub before you close it.
- It has no Docker daemon you can rely on, so the container lessons need a laptop or Lifebit.

> **Check:** The old introduction said Google Cloud Shell comes with `conda`. The conda lesson says it does not. Which is right?

## Lifebit

[Lifebit CloudOS](https://cloudos.lifebit.ai/) is the platform for large runs. Its notebook servers already have `git`, `conda`, `docker` and `nextflow`.

1. [Create a CloudOS account](../platforms/creating-a-cloudos-account.md).
2. [Log in](../platforms/logging-into-cloudos.md).
3. [Start a JupyterLab notebook](../interactive-computing/starting-a-jupyter-lab-notebook.md), then open *Terminal* in the Launcher.
4. Notebook servers have conda already. Clone and create the environment:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   conda env create -f eos.yml
   conda activate eos
   ```

> **Check:** Cost and credits. What does a notebook server cost, when does it shut down, and are credits available to course students? The answer decides whether Lifebit can be a first step. Ask your course lead before you start a server.

## Amazon Web Services (AWS) and NIH STRIDES

Both give you a cloud computer you rent by the hour. Neither is needed for the first lessons.

- **AWS.** [Amazon Web Services](https://aws.amazon.com/) is a general cloud. It has a free tier for small tests. AWS also runs a separate [Cloud Credits for Research](https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/) programme. You apply to AWS, and AWS decides.
- **NIH STRIDES.** [STRIDES](https://cloud.nih.gov/) is an NIH programme that gives NIH-funded researchers discounted prices on Google Cloud and AWS. It lowers the price. It does not give free credits. You enrol through [cloud.nih.gov/enrollment](https://cloud.nih.gov/enrollment), usually through your institution's research computing office, and you need an active NIH award number. See the [STRIDES FAQ](https://cloud.nih.gov/resources/strides-faqs).
- **Lifebit.** Lifebit runs on cloud computers like these. The platform lessons use Lifebit, so you do not need your own AWS account to follow them.

> **Check:** I took the STRIDES facts from NIH pages and university pages dated 2019 to 2022. Before you rely on them, confirm the current partners, who is eligible, and how to enrol at [cloud.nih.gov](https://cloud.nih.gov/) or STRIDES@nih.gov. Also confirm the AWS credits terms on the AWS page. Students who are not NIH-funded may not qualify for STRIDES.

## Next

Back to [Let's dive in](lets-dive-in.md).
