# Agentic harness

*In the book: Sections 11.5.3 and 11.5.4, The Agentic Harness; Wiring a Claude Code Loop.*

An *agentic harness* is the setup on the assistant's side that makes your tools useful when an AI assistant drives them. In this lesson we meet its four parts, and then we connect one of our own tools to Claude Code.

## Start here

### Pre-requisites

- The setup on the [Introduction page](../introduction/README.md) is done, and JupyterLab is running from the `eos` environment.
- The previous lesson, [MCP server](../mcp-server/README.md), is done. We use the MCP server it builds.

### What you should see

You register your MCP server with Claude Code (`claude mcp add`) and see it in `claude mcp list`. Then you start `claude` and ask it to use your tool. Claude calls `greet`, writes a file and runs `git add`, `git commit` and `git push`.

> **Picture to add:** Claude Code in a terminal after the request, showing the tool call and the git commands (save a screenshot of the finished loop) (save as assets/overview.png)

### Where the files are

- `lessons/agentic-harness/wiring-a-claude-code-loop.ipynb` and `.md`: the walkthrough.
- `.claude/` in the repository: this repository's own harness (project memory, skills, agents and hooks).
- `lessons/agentic-harness/assets/`: pictures for this lesson.

## Steps to execute

1. [`wiring-a-claude-code-loop.md`](wiring-a-claude-code-loop.md) — register an MCP server with Claude Code and drive it from chat

## Ask an AI assistant

*Optional.* Please read [Using the AI prompts](../introduction/README.md) first.

**Ask it to explain.**

```text
Explain what an agent harness is: the instructions file, the tools, the permissions and the loop. Say what each one does in a coding agent such as Claude Code.
```

**Ask it to build.**

```text
Write the instructions file for an AI coding agent for my repository (named CLAUDE.md or AGENTS.md, depending on the tool). Include: what the repository is, the exact commands to build and test, the folder layout, the rules (never edit files under data/, never push, never delete), and how to report what it did. Ask me for anything you need first.
```

**Ask it to review.**

```text
Review this agent instructions file. Is anything unclear, contradictory or unsafe? Is there a command an agent could run that I would regret? Is there a rule it cannot check? List each.

<paste file>
```


## Further reading

- [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- [Skills](https://docs.claude.com/en/docs/claude-code/skills), [sub-agents](https://docs.claude.com/en/docs/claude-code/sub-agents) and [hooks](https://docs.claude.com/en/docs/claude-code/hooks)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Anthropic API documentation](https://docs.anthropic.com/) and [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

## Supplementary information

### Why a harness

The [MCP server](../mcp-server/README.md) lesson covered the *tool side*: wrapping a command-line tool so an assistant can call it. This lesson covers the *assistant side*: setting the assistant up to work well with your repository, your rules and your tools.

Without a harness the assistant guesses your conventions. With one it has:

- A place to *read* what the repository is and how it is organised.
- On-demand *skills* it can invoke.
- Specialised *sub-agents* it can hand tasks to.
- Deterministic *hooks* that block mistakes before they happen.

### The four pieces

**1. `CLAUDE.md`: project memory.** A Markdown file at the repository root that the assistant reads at the start of each session. It says what the repository is, how it is organised and what to do or avoid.

```markdown
# CLAUDE.md — elements-of-style-lessons

## What this repo is
A pragmatic set of biomedical-workflow lessons paired with a Springer
book. Every lesson has a canonical README at `lessons/<topic>/README.md`;
`docs/source/lessons/*.md` files are include-shims and should not be
edited directly.

## The four governing principles
1. One container, one job, one CLI.
2. One `.nf` module wraps one CLI verb.
3. `main-<name>.nf` composes modules into a workflow.
4. The story builds chapter by chapter.

## Never do
- Do not judge the author's work. Augment; don't replace.
- Do not edit files under `docs/source/lessons/`; edit the canonical
  README they point at.
- Do not add embellishments to author voice — plain prose only.
```

**2. Skills: packaged instructions on demand.** Skills live under `.claude/skills/`. Each is a folder with a `SKILL.md` that says what it does and when to use it. Good candidates here:

- `elements-of-style-review`: judge a lesson against the [eight principles](../elements-of-style-rules/README.md).
- `lesson-scaffold`: create a new lesson with the standard shape.
- `build-verify`: run `make html -W` and report warnings before a commit.

**3. Sub-agents: specialised roles.** They live under `.claude/agents/`. Each is a Markdown file with front matter that names the agent's tools and system prompt. Useful ones: `code-reviewer`, `data-validator` (opens an `.h5ad` or CSV and checks shape, columns and value ranges), `workflow-linter` (flags inline logic and missing container lines in `.nf` files) and `notebook-runner` (runs a notebook end to end and reports failing cells).

**4. Hooks: deterministic guards.** They live under `.claude/hooks/`, fire on tool events and can block an action. Useful here:

- `pre-write` on `docs/source/lessons/*.md`: block it, because those are shims. Send the edit to the canonical README.
- `pre-commit`: run `sphinx-build -W` and block the commit on warnings.
- `pre-commit`: run `jupyter nbconvert --to notebook --execute` on changed notebooks and block the commit if a cell fails.

### The self-modification pattern

Claude Code can write its own skills, agents and hooks. That is powerful and risky. **Powerful:** ask it to keep a new pattern as a skill, and next session the skill is there. **Risky:** it can write code that runs in later sessions. Please review what it writes like any code: read the diff, run it on a safe case, and commit only what you would have written yourself. The harness lives in version control, like your command-line tools.

### This repository's harness

```text
.claude/
├── CLAUDE.md                          # project memory
├── skills/
│   ├── elements-of-style-review/      # evaluate against the 8 principles
│   ├── lesson-scaffold/               # create a new lesson
│   └── build-verify/                  # run make html -W
├── agents/
│   ├── code-reviewer.md
│   ├── data-validator.md
│   └── workflow-linter.md
└── hooks/
    ├── pre-write-shim-guard.sh
    ├── pre-commit-sphinx-build.sh
    └── pre-commit-nb-execute.sh
```

### Configure Claude Code

On macOS:

```bash
# Install Claude Code (one time)
curl -fsSL https://claude.ai/install.sh | bash

# In the repository:
cd elements-of-style-lessons
claude
```

On Windows (Git Bash), follow the [Claude Code setup page](https://docs.claude.com/en/docs/claude-code/setup), then run `cd elements-of-style-lessons` and `claude`. The assistant picks up `CLAUDE.md`, skills, agents and hooks automatically.

## Next

[Publishing for agents](../publishing-for-agents/README.md): make your work findable by other agents, not just your own.
