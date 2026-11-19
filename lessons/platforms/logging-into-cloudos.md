# Logging into CloudOS

You will sign in to CloudOS, create a workspace and open JupyterLab inside it. This matters because the workspace is where your analysis runs.

*Part of the [platforms](README.md) lesson.*

## Start here

### What you will do

- Open the login page and sign in with your institution.
- Create a workspace from the *biomedical analysis* template.
- Open JupyterLab in that workspace.

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- A CloudOS account. See [creating a CloudOS account](creating-a-cloudos-account.md).
- A web browser. There is nothing to install, and this page has nothing to run.

## Steps to execute

### Open the login page

Why: this is the front door of the platform. Open <https://cloudos.lifebit.ai/login> in a browser.

**What you should see:** the CloudOS login page.

> **Picture to add:** the CloudOS login page (save as assets/logging-into-cloudos-step-2.png)

### Use institutional login

Why: you made your account this way, so you sign in this way.

Choose *Sign in with institutional login* and pick your institution from the list. If it is not listed, ask at <https://lifebit.ai/contact>.

**What you should see:** your institution's sign-in page, and after you sign in, the CloudOS home page.

### Create a workspace

Why: a *workspace* is a private area with its own files and tools for your project.

Create a workspace and pick the *biomedical analysis* template.

**What you should see:** a new workspace in your list.

> **Picture to add:** the create-workspace screen with the biomedical analysis template selected (save as assets/logging-into-cloudos-step-2.png)

> **Check:** which button or menu creates a workspace, and how long does a new workspace take to start?

### Open JupyterLab

Why: JupyterLab is where you run notebooks, like this one.

Open the workspace's JupyterLab. Then continue with [starting-a-jupyter-lab-notebook](../interactive-computing/starting-a-jupyter-lab-notebook.md).

**What you should see:** the JupyterLab Launcher with tiles for notebooks and a terminal.

> **Picture to add:** JupyterLab open inside the CloudOS workspace (save as assets/logging-into-cloudos-step-3.png)

### If something goes wrong

- **Your institution is not in the list.** Ask at <https://lifebit.ai/contact>.
- **You sign in but see no workspace.** Create one in *Create a workspace*. A new account starts with none.
- **The JupyterLab tab opens blank or is blocked.** Allow pop-ups for `cloudos.lifebit.ai` in your browser and try again.

## Next

[Authenticating on CloudOS](authenticating-on-cloudos.md): get an API key and run `cloudos configure`, so you can run jobs from a terminal.
