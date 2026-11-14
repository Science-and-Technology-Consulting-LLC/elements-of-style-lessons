# Pre-training: Kids First, INCLUDE and other accounts

You will create two data-hub accounts, one at Kids First and one at INCLUDE, before the course starts. Each takes a few minutes, and both link to the same NIH identity so access to controlled data can flow through.

*Part of the [platforms](README.md) lesson.*

## What you will do

- Create a Kids First Data Resource Center (DRC) account.
- Create an INCLUDE Data Hub account.
- Learn what GA4GH is and why these accounts follow its rules.

## What you need

- A web browser. No programs to install.
- An NIH login for the Kids First account, through the NIH Researcher Authentication Service (RAS). The step names the service you pick.
- A Google account or an [ORCID](https://orcid.org/) for the INCLUDE account. ORCID is the recommended one.
- [JupyterLab](https://jupyter.org/) with a Bash kernel only if you want to run this page as a notebook. It has nothing to run.

## Before you begin

1. **Get the code.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`, then open [`pre-training-creating-kids-first-and-other-accounts.ipynb`](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/platforms/pre-training-creating-kids-first-and-other-accounts.ipynb) and run each cell in order, top to bottom.

## Check your setup

This notebook runs shell commands with the Bash kernel and uses tools such as `git` and `conda`. If the top right of this notebook does not say **Bash**, or a later command says *command not found*, do the *Register the Bash kernel* and *Check your tools* steps of [Let's dive in](../introduction/lets-dive-in.md) first.

## Why these accounts

Why: before the five-day course starts, two data-hub accounts are worth having. Each takes minutes to register, and each links to the same NIH identity so authorisation flows through.

## Create your Kids First DRC account

Why: you need an account to see which Kids First data you may access.

1. Go to [https://kidsfirstdrc.org/](https://kidsfirstdrc.org/).
2. Click **Create your account**.
3. Choose a *connection service*. Pick **NIH Researcher Authentication Service (RAS)**. This is the service that knows which controlled-access datasets you are authorised for.
4. Enter basic profile information.
5. Agree to the **NIH Genomic Data User Code of Conduct**.
6. You land on the Kids First Portal Dashboard.

**What you should see:** the Kids First Portal Dashboard.

> **Picture to add:** the Kids First sign-up page with the connection service choice (save as assets/pre-training-creating-kids-first-and-other-accounts-step-1.png)

> **Picture to add:** the Kids First Portal Dashboard after the account is created (save as assets/pre-training-creating-kids-first-and-other-accounts-step-1b.png)

## Create your INCLUDE Data Hub account

Why: INCLUDE is a second data hub. It is tied to your identity in the same way.

1. Go to [https://portal.includedcc.org/](https://portal.includedcc.org/).
2. Click **Sign Up**.
3. Authenticate with **Google** or **ORCID**. ORCID is the recommended path, because it doubles as your authoritative researcher identifier. *eRA Commons login for INCLUDE is on the roadmap.*

**What you should see:** the INCLUDE portal, signed in.

> **Picture to add:** the INCLUDE sign-up page with the Google and ORCID options (save as assets/pre-training-creating-kids-first-and-other-accounts-step-2.png)

## GA4GH, the framework behind the rules

Pediatric data and human data are *sensitive data*. The **Global Alliance for Genomics & Health ([GA4GH](https://www.ga4gh.org/))** sets policy and technical standards. Its mission is *responsible genomic data sharing within a human-rights framework*. The two accounts above implement pieces of that framework.

## If something goes wrong

- **RAS asks for an NIH login you do not have.** Ask your institution or the course team how to get one. Kids First needs it to know which controlled datasets you may open.
- **You do not see a Create your account button.** Look for **Login** or **Sign in**. The page layout may have changed.
- **INCLUDE does not accept your Google or ORCID.** Try the other one. ORCID is recommended.

## Next

[Creating a CloudOS account](creating-a-cloudos-account.md), then [logging into CloudOS](logging-into-cloudos.md). Or return to the [platforms lesson](README.md).
