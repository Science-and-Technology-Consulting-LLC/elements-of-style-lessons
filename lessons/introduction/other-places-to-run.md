# Other places to run these lessons

## Start here

Further information. You do not need this page if you have a Mac, a Windows computer with Git Bash, or a Linux computer. Start with [Let's dive in](lets-dive-in.md).

Use this page if you have no terminal of your own, or when your work grows beyond your laptop.

## Other places to run

### Lifebit

[Lifebit CloudOS](https://cloudos.lifebit.ai/) is the platform for large runs. Its notebook servers already have `git`, `conda`, `podman` and `nextflow`.

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


## Next

Back to [Let's dive in](lets-dive-in.md).
