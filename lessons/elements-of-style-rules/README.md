# The Rules

> *In the book: Chapter 2 — The Rules.*

:::{admonition} What you'll learn
:class: tip

- The **eight canonical principles** that underpin every later lesson,
  drawn from Strunk & White and Kernighan & Plauger.
- A short collection of **derived rules of thumb** — pithier phrases
  to reach for when choosing between two ways to do something.
:::

## The canonical eight

Inspired by **Strunk & White** (*The Elements of Style*) and
**Kernighan & Plauger** (*The Elements of Programming Style*). Read
them once now; come back when you're choosing between two ways to do
something.

### 1. Write clearly — don't be too clever

If a colleague reading your code six months from now has to puzzle
out what it does, you've optimised for the wrong thing. Clever is for
crosswords. Clear is for science.

### 2. Pseudo-code first

Sketch what each step does in plain English before writing any
syntax. Most bugs are *thinking* bugs, not typing bugs. Pseudocode
catches the thinking ones before they become typing ones.

### 3. Modularize

One function does one thing. One CLI verb does one thing. One Nextflow
module does one thing. Things you can name independently you can test
and reuse independently.

### 4. Build and test in small pieces

Compose from working pieces. Don't build a 10-step pipeline and run
the whole thing hoping it works. Build step 1; test it. Build step 2;
test it. Then stitch.

### 5. Validate all inputs

Trust nothing that crosses a boundary — file format, column name,
expected range, missing values. The cell-counts in a `.h5ad` file
should match the row labels. The CSV header should be the columns
your code asks for. Check, don't assume.

### 6. Make it right before faster

Premature optimisation is the famous sin. Get the answer right,
*then* — if performance actually matters — measure where time is
going, and fix that. Most "slow" code is fine. Most "wrong" code is
not.

### 7. Keep it simple

Every layer of abstraction you add is a layer the next reader has to
peel back. If a one-line function would do, write the one-line
function.

### 8. Document data and functions

Every column has units. Every function has a purpose. Every CLI flag
has a meaning. Document them where they're defined. The README is the
*outside* of the box; the docstring is the *inside.* Both matter.

## Derived rules of thumb

Short phrases that summarise patterns this curriculum keeps returning
to. Most are direct corollaries of the eight above.

### On work that lasts

> **Workflows are letters to your future self.**

> **Pinning beats remembering.**

> **A notebook is a draft tool. A CLI is a durable tool.**

> **If you can't rerun it six months from now, it isn't a workflow.**

### On the discipline of one job at a time

> **One container, one job.**

> **One CLI does one thing well.**

> **One module is one process with documented inputs and outputs.**

### On honesty

> **If `--help` lies, the CLI is broken.**

> **Restart and Run All before you ship.**

> **Cite your data; pin your env.**

### On other people

> **Do not judge.** When a learner struggles, that's information about
> the lesson, not about the learner. When a collaborator's work isn't
> the way you'd do it, ask before "fixing." Augment what's there; don't
> replace it.

> **Educate without disrupting.**

> **Bridge constrained environments; don't fight them.**

> **Your README is for the next person — and the next person is sometimes you.**

### On the agentic AI era

> **A well-documented CLI is an API for AI agents.**

> **An MCP server is the politest introduction your tool can make.**

> **One MUST have a simple design idea in one's head — or one WILL be led astray.**

## Six things to remember

Six takeaways that map 1:1 to the curriculum spine. If you walk away
with nothing else, walk away with these.

### 1. Start simple

Shell scripts → test → scale. A working five-line script you've run
once beats a beautiful 200-line one you haven't.
*(Foundation lessons.)*

### 2. Containerize

Docker + Conda at the process level. One container, one job, one CLI.
*([Containers](containers.md).)*

### 3. Use workflow languages

Nextflow (or CWL / WDL — Nextflow first for biomedical work).
Parallelisation comes free. Same workflow runs on laptop, cluster, and
cloud.
*([Nextflow modules](nextflow-modules.md) → [Nextflow workflows](nextflow-workflows.md).)*

### 4. Version control

GitHub for everything. If it's worth running once, it's worth
committing once.
*([Version control](version-control.md).)*

### 5. AI wisely

Syntax help — yes. Architecture design — no. You hold the design idea
in your head; the AI fills in the keystrokes.
*([MCP server](mcp-server.md), [Publishing for agents](publishing-for-agents.md).)*

### 6. Fail fast

GitHub Actions for CI/CD. The sooner you find the broken thing, the
cheaper it is to fix.

## In-depth walkthrough

- [`a-few-simple-rules.md`](a-few-simple-rules.md) —
  Kernighan & Plauger's 55 pithy rules, in their original form, with Annie's
  annotations of which ones still bite in the containerised, workflow-driven,
  agentic-AI era. Adapted from the NICHD Kids First / INCLUDE course.

## Further reading

- [Strunk & White — *The Elements of Style*](https://en.wikipedia.org/wiki/The_Elements_of_Style)
- [Kernighan & Plauger — *The Elements of Programming Style*](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style)
- [Robert C. Martin — *Clean Code*](https://en.wikipedia.org/wiki/Clean_Code)
- [How to Design Programs](https://htdp.org/) — a free introduction to program design


## Where to next

→ [Command line, with Git Bash](command-line-and-git-bash.md)
