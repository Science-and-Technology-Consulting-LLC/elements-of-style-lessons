# The Rules

Before any rule, there is a question to answer. This lesson gives the order we follow in all our work, and then the eight rules that keep our answers trustworthy.

> *In the book: Section 3.1 — The Rules.*

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done.

This lesson has no notebook and nothing to run. You read it. Please read it once now, and come back to it when you must choose between two ways to do something.

### What you should see

Nothing runs, so there is no output. When you finish, you can:

- say the four things we do before we touch the data,
- say the eight rules in your own words,
- tell a friend what *signal in the noise* means.

### Where the files are

- `lessons/elements-of-style-rules/README.md` — this page. It is the whole lesson.

## Steps to execute

### What we are doing

All analytics, and everything we do in this course, is one activity. We are looking for the signal in the noise.

Think of a hidden picture inside a complex diagram. If you do not know what you are looking for, you will not find an answer, or you will find a distraction. So we begin by knowing what we are looking for. Only then do we pick up our tools.

### Four things come first

These come before the rules. Please do them in this order.

**1. Ask the right question.** Write it down as one sentence. If we cannot say it plainly, we are not ready to open the data.

**2. Know the domain.** This is the first law of engineering, of software and of systems. Talk to the expert. Listen. Understand what is the cause and what is the effect. A method cannot tell us this. A person who has lived with the problem can.

**3. Know your measurement technologies.** Know how the numbers were made, and know what our code does to them. Numbers and code are our instruments, and we must understand an instrument before we trust its reading.

**4. Know what your answers could be.** Make a hypothesis and state it, before we look. Then test it. When we know what the possible answers look like, we can tell a real finding from a distraction.

### From a question to a durable answer

The path is the same every time:

1. **Shine the light broadly.** Look at all of the data first, so that we see what is there.
2. **Focus in.** Follow the part that stands out.
3. **State a hypothesis.** One sentence that could turn out to be wrong.
4. **Tell a story with your data.** Say what we think caused what, and why the numbers fit.
5. **Test it.** Are we right? What is significant, and what is chance? What would change our mind?
6. **Keep what is durable.** A durable answer is one that someone else, or we ourselves six months later, can repeat and get again.

The last step is the reason for the rules. A durable answer needs a method that can be repeated. That is what the eight rules give us.

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

## Ask an AI assistant

*Optional.* How to use these prompts is explained in [Using the AI prompts](../introduction/README.md).

**Ask it to question you.** Use this before you touch your data.

```text
I want to analyse <my data> to find out <what I wonder>. Do not suggest methods yet. Ask me, one question at a time: what exactly is my question; who is the expert I should talk to; how the numbers were measured and what can go wrong; what my answer could be; and what result would surprise me. When we are done, write my hypothesis as one sentence that could turn out to be wrong.
```

**Ask it to explain.**

```text
Here is a rule from the Elements of Style course: "<paste one rule>". Explain it in three sentences to a biologist, then give one example of a script that breaks the rule and the same script fixed.
```

**Ask it to build.**

```text
I have a script that does <what it does>. Rewrite it so that each step is one small function with a clear name, the settings are options and not numbers in the code, and every function has a one-line comment that says its purpose. Keep the output identical. Show me the result of a test I can run to prove it.
```

**Ask it to review.**

```text
Review the script below against the eight rules that follow. For each rule say met or not met, and quote the line. Do not rewrite the script.

<paste the eight rules from The Rules lesson>

<paste script>
```


## Further reading

- [Strunk and White, *The Elements of Style*](https://en.wikipedia.org/wiki/The_Elements_of_Style)
- [Kernighan and Plauger, *The Elements of Programming Style*](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style)
- [Robert C. Martin, *Clean Code*](https://en.wikipedia.org/wiki/Clean_Code)
- [How to Design Programs](https://htdp.org/), a free introduction to program design

## Supplementary information

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
2. **Containerize.** Use [Podman](https://podman.io/docs/installation) and [Conda](https://docs.conda.io/) at the level of one process. One container, one job, one command line tool. ([Containers](../containers/README.md).)
3. **Use workflow languages.** [Nextflow](https://www.nextflow.io/) first for biomedical work, or CWL or WDL. Running steps in parallel comes free. The same workflow runs on a laptop, a cluster and the cloud. ([Introduction to Nextflow](../nextflow-workflows/README.md), then [Nextflow modules and features](../nextflow-modules/README.md).)
4. **Use version control.** Put everything on [GitHub](https://github.com/). If it is worth running once, it is worth committing once. ([Version control](../version-control/README.md).)
5. **Use AI wisely.** Syntax help, yes. Architecture design, no. You hold the design idea in your head. The AI fills in the keystrokes. ([MCP server](../mcp-server/README.md), [Publishing for agents](../publishing-for-agents/README.md).)
6. **Fail fast.** Use [GitHub Actions](https://docs.github.com/en/actions) for CI/CD. The sooner you find the broken thing, the cheaper it is to fix. ([Continuous integration](../continuous-integration/README.md).)

## Next

[The command line, with Git Bash](../command-line-and-git-bash/README.md): the first practical lesson.
