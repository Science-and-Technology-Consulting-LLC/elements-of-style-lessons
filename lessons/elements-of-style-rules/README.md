# The Rules

This lesson gives you eight rules, drawn from Strunk and White and from Kernighan and Plauger, that every later lesson relies on.

> *In the book: Section 3.1 — The Rules.*

## Before you start

The previous lesson: [Introduction](../introduction/README.md).

## Do this

This lesson has no notebook and nothing to run. You read it.

1. **Clone the repository** (optional, if you want the files on your computer). In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal** only if you cloned. On a Mac, open *Terminal*. On Windows, open *Git Bash*.
3. **Read this page.** On your computer it is `lessons/elements-of-style-rules/README.md`. On the web it is [here](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/elements-of-style-rules/README.md). Read the eight rules once now. Come back when you must choose between two ways to do something.

## What you should see

Nothing runs, so there is no output. When you finish, you can say the eight rules in your own words and name the six things to remember.

## Where the files are

- `lessons/elements-of-style-rules/README.md` — this page. It is the whole lesson.

## Next

[Command line, with Git Bash](../command-line-and-git-bash/README.md)

## Background

### The eight rules

These come from Strunk and White, [*The Elements of Style*](https://en.wikipedia.org/wiki/The_Elements_of_Style), and from Kernighan and Plauger, [*The Elements of Programming Style*](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style).

**1. Write clearly. Do not be too clever.** If a colleague reading your code six months from now has to puzzle out what it does, you have optimised for the wrong thing. Clever is for crosswords. Clear is for science.

**2. Write pseudo-code first.** Sketch what each step does in plain English before you write any syntax. Most bugs are thinking bugs, not typing bugs. Pseudo-code catches the thinking ones early.

**3. Modularize.** One function does one thing. One command line verb does one thing. One Nextflow module does one thing. Things you can name independently, you can test and reuse independently.

**4. Build and test in small pieces.** Do not build a 10-step pipeline and run the whole thing hoping it works. Build step 1 and test it. Build step 2 and test it. Then join them.

**5. Validate all inputs.** Trust nothing that crosses a boundary: file format, column name, expected range, missing values. The cell counts in a `.h5ad` file should match the row labels. The CSV header should hold the columns your code asks for. Check. Do not assume.

**6. Make it right before faster.** Premature optimisation is the famous sin. Get the answer right. Then, if speed matters, measure where the time goes and fix that. Most "slow" code is fine. Most "wrong" code is not.

**7. Keep it simple.** Every layer of abstraction is a layer the next reader must peel back. If a one-line function does the job, write the one-line function.

**8. Document data and functions.** Every column has units. Every function has a purpose. Every command line flag has a meaning. Document each where it is defined. The README is the outside of the box. The docstring is the inside. Both matter.

### Derived rules of thumb

Short phrases for patterns the lessons keep returning to. Most follow from the eight rules above.

**On work that lasts**

- Workflows are letters to your future self.
- Pinning beats remembering.
- A notebook is a draft tool. A command line tool is a durable tool.
- If you cannot rerun it six months from now, it is not a workflow.

**On one job at a time**

- One container, one job.
- One command line tool does one thing well.
- One module is one process with documented inputs and outputs.

**On honesty**

- If `--help` lies, the tool is broken.
- Restart and Run All before you ship.
- Cite your data. Pin your environment.

**On other people**

- Do not judge. When a learner struggles, that is information about the lesson, not about the learner. When a collaborator's work is not the way you would do it, ask before you "fix" it. Add to what is there. Do not replace it.
- Educate without disrupting.
- Bridge constrained environments. Do not fight them.
- Your README is for the next person. The next person is sometimes you.

**On the agentic AI era**

- A well-documented command line tool is an API for AI agents.
- An MCP server is the politest introduction your tool can make.
- One must have a simple design idea in one's head, or one will be led astray.

### Six things to remember

These map one to one onto the lessons.

1. **Start simple.** Write a shell script, test it, then scale. A working five-line script you have run once beats a beautiful 200-line one you have not. (Foundation lessons.)
2. **Containerize.** Use [Docker](https://docs.docker.com/get-docker/) and [Conda](https://docs.conda.io/) at the level of one process. One container, one job, one command line tool. ([Containers](../containers/README.md).)
3. **Use workflow languages.** [Nextflow](https://www.nextflow.io/) first for biomedical work, or CWL or WDL. Running steps in parallel comes free. The same workflow runs on a laptop, a cluster and the cloud. ([Nextflow modules](../nextflow-modules/README.md), then [Nextflow workflows](../nextflow-workflows/README.md).)
4. **Use version control.** Put everything on [GitHub](https://github.com/). If it is worth running once, it is worth committing once. ([Version control](../version-control/README.md).)
5. **Use AI wisely.** Syntax help, yes. Architecture design, no. You hold the design idea in your head. The AI fills in the keystrokes. ([MCP server](../mcp-server/README.md), [Publishing for agents](../publishing-for-agents/README.md).)
6. **Fail fast.** Use [GitHub Actions](https://docs.github.com/en/actions) for CI/CD. The sooner you find the broken thing, the cheaper it is to fix. ([Continuous integration](../continuous-integration/README.md).)

### Further reading

- [Strunk and White, *The Elements of Style*](https://en.wikipedia.org/wiki/The_Elements_of_Style)
- [Kernighan and Plauger, *The Elements of Programming Style*](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style)
- [Robert C. Martin, *Clean Code*](https://en.wikipedia.org/wiki/Clean_Code)
- [How to Design Programs](https://htdp.org/), a free introduction to program design

### The notebooks in this lesson

This lesson has no notebooks.
