# Agentic harness

*In the book: Sections 11.5.3 and 11.5.4, The Agentic Harness; Wiring a Claude Code Loop.*

An *agentic harness* is the setup on the assistant's side that makes your tools useful when an AI assistant drives them. This lesson explains its four parts and has you connect one of your own tools to Claude Code.

## Before you start

Do [mcp-server](../mcp-server/README.md) first. You need the MCP server it builds.

## Do this

1. **Clone the course repository.** In a terminal, run:

   ```bash
   git clone https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons.git
   cd elements-of-style-lessons
   ```

2. **Open a terminal.** On a Mac, open *Terminal*. On Windows, open *Git Bash*. On Linux, open your terminal program. No terminal at hand? See [Other places to run these lessons](../introduction/other-places-to-run.md).
3. **Open the notebook.** From the repository folder, start JupyterLab with `jupyter lab`. Then open `lessons/agentic-harness/wiring-a-claude-code-loop.ipynb` ([view it on GitHub](https://github.com/Science-and-Technology-Consulting-LLC/elements-of-style-lessons/blob/main/lessons/agentic-harness/wiring-a-claude-code-loop.ipynb)) and run each cell in order, top to bottom.

## What you should see

You register your MCP server with Claude Code (`claude mcp add`), see it in `claude mcp list`, then start `claude` and ask it to use your tool. Claude calls `greet`, writes a file and runs `git add`, `git commit` and `git push`.

> **Picture to add:** Claude Code in a terminal after the request, showing the tool call and the git commands (save a screenshot of the finished loop) (save as assets/overview.png)

## Where the files are

- `lessons/agentic-harness/wiring-a-claude-code-loop.ipynb` and `.md`: the walkthrough.
- `.claude/` in the repository: this repository's own harness (project memory, skills, agents and hooks).
- `lessons/agentic-harness/assets/`: pictures for this lesson.

## Notebooks in order

1. [`wiring-a-claude-code-loop.md`](wiring-a-claude-code-loop.md) — register an MCP server with Claude Code and drive it from chat

## Next

[Publishing for agents](../publishing-for-agents/README.md): make your work findable by other agents, not just your own.

## Background

### Why a harness

The [MCP server](../mcp-server/README.md) lesson covered the *tool side*: wrap a CLI so an assistant can call it. This lesson covers the *assistant side*: set the assistant up to work well with your repository, your rules and your tools.

Without a harness the assistant improvises and guesses your conventions. With one it has:

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

Claude Code can write its own skills, agents and hooks. That is powerful and risky. **Powerful:** ask it to codify a new pattern as a skill, and next session the skill is there. **Risky:** it can write code that runs in later sessions. Review agent-written harness changes like any code: read the diff, run it on a safe case, and commit only what you would have written yourself. The harness is version-controlled, reviewed and committed like your CLIs.

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

### Further reading

- [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- [Skills](https://docs.claude.com/en/docs/claude-code/skills), [sub-agents](https://docs.claude.com/en/docs/claude-code/sub-agents) and [hooks](https://docs.claude.com/en/docs/claude-code/hooks)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Anthropic API documentation](https://docs.anthropic.com/) and [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
