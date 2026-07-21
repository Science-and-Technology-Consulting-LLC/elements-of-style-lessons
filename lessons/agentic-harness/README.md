# Agentic harness

> *In the book: Chapter 16 — Agentic harness.*

:::{admonition} What you'll learn
:class: tip

- What an "agentic harness" is — the agent-side configuration that
  makes your CLIs and workflows productive when driven by an AI agent.
- The four pieces of a harness: `CLAUDE.md`, skills, sub-agents,
  hooks.
- How to configure this repo's harness so an agent can review,
  validate, and extend the curriculum without breaking anything.
- The self-modification pattern — because Claude Code can write
  skills, agents, and hooks for itself, the harness is not a one-time
  setup.
:::

:::{admonition} 📸 Screenshot placeholder
:class: note

*A screenshot will land at `assets/overview.png` showing Claude Code
running with a project skill invoked. Reference it as
`![overview](assets/overview.png){width=520}` once captured.*
:::

## Why an agentic harness

The [MCP server](mcp-server.md) lesson taught the *tool-facing* side:
wrap a CLI so an agent can call it. This lesson teaches the
*agent-facing* side: configure the agent so it works well with your
repo, your rules, your tools.

Without a harness, an agent will improvise. It will guess your
conventions, sometimes correctly. With a harness, the agent has:

- A place to *read* what the repo is and how it's organised.
- A set of on-demand *skills* it can invoke without prompting.
- Specialised *sub-agents* it can delegate to for specific tasks.
- Deterministic *hooks* that guard against mistakes before they happen.

Together, these four pieces are the harness.

## The four pieces

### 1. `CLAUDE.md` — project memory

A Markdown file at the repo root. The agent reads it on every session
in that repo. It's the README your agent needs — one that tells it
what the repo *is*, how it's organised, and what to do / not do.

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

### 2. Skills — packaged instructions on demand

Skills live under `.claude/skills/`. Each is a folder with a
`SKILL.md` describing what it does and when to use it. When the agent
detects the skill is relevant, it loads and follows the instructions.

Good candidates for this repo:

- `.claude/skills/elements-of-style-review/` — evaluate a lesson or
  notebook against the [eight canonical principles](elements-of-style-rules.md).
- `.claude/skills/lesson-scaffold/` — create a new lesson with the
  standard shape (README + notebooks + eye-candy + assets).
- `.claude/skills/build-verify/` — run `make html -W` and report
  warnings before committing.

### 3. Sub-agents — specialised roles

Sub-agents live under `.claude/agents/`. Each is a Markdown file with
frontmatter declaring the agent's tools and system prompt. The main
agent can delegate to them.

Useful sub-agents for biomedical workflow work:

- `code-reviewer` — reads the diff, checks it against the rules.
- `data-validator` — opens an `.h5ad` or CSV and checks shape,
  column names, expected value ranges.
- `workflow-linter` — reads `.nf` files and flags inline logic,
  missing container declarations, misnamed channels.
- `notebook-runner` — executes a notebook end-to-end and reports
  cells that fail or produce unexpected output.

### 4. Hooks — deterministic guards

Hooks live under `.claude/hooks/` and fire on tool events. They run
*before* an action completes and can block it if a condition fails.

Useful for this repo:

- `pre-write` on `docs/source/lessons/*.md` — block; those are shims.
  Route the edit to the canonical README.
- `pre-commit` — run `sphinx-build -W`. If warnings, block the commit.
- `pre-commit` — run `jupyter nbconvert --to notebook --execute` on
  changed notebooks. If a cell fails, block the commit.

## The self-modification pattern

Claude Code can write its own skills, agents, and hooks. This is
powerful and dangerous.

**Powerful:** the agent extends itself as you teach it your practice.
Working on a new pattern? Ask the agent to codify it as a skill. It
adds a folder under `.claude/skills/`. Next session, that skill is
available.

**Dangerous:** the agent can write code that runs in future sessions.
Review agent-authored harness additions the same way you review any
other code:

1. Read the diff.
2. Run it against a known-safe scenario.
3. Commit only if you'd write it yourself.

The rule: **the harness is version-controlled, reviewed, and
committed like any other code**. Nothing is "just an agent's helper" —
everything gets the same discipline as your CLIs.

## This repo's harness — the worked example

Everything in `.claude/` in this repo is the demo:

```
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

Open any of them and you'll see the pattern applied.

## Configure Claude Code — three platforms

::::{tab-set}

:::{tab-item} macOS
:sync: mac

```bash
# Install Claude Code (one time)
curl -fsSL https://claude.ai/install.sh | bash

# In the repo:
cd elements-of-style-lessons
claude
# The agent picks up CLAUDE.md, skills, agents, and hooks automatically.
```
:::

:::{tab-item} Windows (Git Bash)
:sync: win

```bash
# Install Claude Code (one time) — see
# https://docs.claude.com/en/docs/claude-code/setup
# for Windows-specific instructions.

# In the repo:
cd elements-of-style-lessons
claude
```
:::

:::{tab-item} Lifebit
:sync: lifebit

Claude Code runs in the notebook workspace's terminal. Install once
per workspace; the harness in the repo picks up automatically.
:::

::::

## Further reading

- [Claude Code documentation](https://docs.claude.com/en/docs/claude-code) —
  authoritative reference.
- [Skills](https://docs.claude.com/en/docs/claude-code/skills) —
  packaged instructions the agent picks up on demand.
- [Sub-agents](https://docs.claude.com/en/docs/claude-code/sub-agents) —
  specialised roles.
- [Hooks](https://docs.claude.com/en/docs/claude-code/hooks) —
  deterministic guards on tool events.
- [Model Context Protocol](https://modelcontextprotocol.io/) — the
  standard the harness uses to talk to MCP servers.
- [Anthropic API documentation](https://docs.anthropic.com/) — for
  building your own agent instead of using Claude Code.
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) —
  worked patterns.

## Where to next

→ [Publishing for agents](publishing-for-agents.md) — make your work
findable by *other* agents, not just your own.
