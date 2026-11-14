# Creating a CloudOS account

You will sign up for a free account on CloudOS, the Lifebit platform that runs pipelines for researchers. This matters because every later page in this lesson runs on that account.

*Part of the [platforms](README.md) lesson. The command-line tool is documented in the [cloudos-cli README](https://github.com/lifebit-ai/cloudos-cli).*

## What you will do

- Open the CloudOS sign-up page.
- Choose *Sign in with institutional login*.
- Pick your institution from the list.
- Know which free tier you are on.

## What you need

- An institutional email, such as a university or NIH address.
- An [ORCID](https://orcid.org/) (recommended). It is a free, permanent ID for researchers and credits you on any work run from this account.
- A web browser. No programs to install.
- [JupyterLab](https://jupyter.org/) with a Bash kernel only if you want to run this page as a notebook. It has nothing to run.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`creating-a-cloudos-account.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/creating-a-cloudos-account.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do Steps 4 and 6 of [Let's dive in](../introduction/lets-dive-in.md) first.

## Step 1. Open the sign-up page

Why: this is where you make your account. Open <https://cloudos.lifebit.ai/register> in your browser.

**What you should see:** the CloudOS registration page with an option called *Sign in with institutional login*.

> **Picture to add:** the CloudOS registration page with the institutional login option (save as assets/creating-a-cloudos-account-step-2.png)

## Step 2. Choose institutional login

Why: institutional login (also called *single sign-on*) lets you use your university or NIH sign-in. You do not make a new password.

Click *Sign in with institutional login*.

**What you should see:** a list or search box of institutions.

## Step 3. Pick your institution

Why: this sends you to your own institution's sign-in page.

Pick your institution from the list (NIH, your university, and so on). If it is not listed, ask at <https://lifebit.ai/contact>. Then sign in with your usual institutional account.

**What you should see:** after you sign in, you land on CloudOS and your account exists.

> **Picture to add:** the institution list on the CloudOS sign-up page (save as assets/creating-a-cloudos-account-step-2.png)

## Step 4. Know your tier

The free tier is *Lifebit Start*.

> **Check:** the page does not say what Lifebit Start includes or how to confirm you are on it. Where in the platform can a new user see their tier?

## If something goes wrong

- **Your institution is not in the list.** Ask at <https://lifebit.ai/contact>. Your institution's single sign-on may not be set up yet.
- **The sign-in page asks for a password you do not have.** Use the institutional login option, not a separate account.
- **You get an error after signing in at your institution.** Try a private browser window, and check that you used your institutional email.

## Next

[Logging into CloudOS](logging-into-cloudos.md): sign in and open a workspace.
