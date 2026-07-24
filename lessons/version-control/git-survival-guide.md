Git Survival Guide for Multi-Remote Biomedical Workflows

*Every example in this section happened during real development of
the NIH-NLM sc-nsforest-qc-nf single-cell quality control pipeline.
The mistakes are real. The fixes are tested.*

---

## 1. The Basics You Already Know (and One Thing You Don't)

You know `git add`, `git commit`, `git push`. You have used
`git clone`. You may even have made a pull request.

Here is the one thing most tutorials skip:

**Git tracks content, not files.** When git says "nothing to commit,
working tree clean," it means the content of every tracked file
matches what is stored. It does not mean your project is in good
shape. It does not mean the right version is deployed. It does not
mean your cloud platform pulled the latest image.

Keep this in mind. It will save you hours.

---

## 2. Forking: Your Copy, Their Repository

When you fork a repository on GitHub, you get an independent copy.
Your fork and the original (upstream) start identical, then diverge
as each side makes changes.

```
upstream (NIH-NLM/sc-nsforest-qc-nf)     your fork (adeslatt/sc-nsforest-qc-nf)
         |                                          |
         v                                          v
    commit A                                   commit A
    commit B  <-- shared history -->           commit B
    commit C  (upstream moves ahead)           commit D  (you move ahead)
    commit E                                   commit F
```

### Setting up both remotes

After cloning your fork, add the upstream remote:

```bash
git clone https://github.com/adeslatt/sc-nsforest-qc-nf.git
cd sc-nsforest-qc-nf

# Your fork is 'origin' (automatic)
git remote -v
# origin  https://github.com/adeslatt/sc-nsforest-qc-nf.git (fetch)
# origin  https://github.com/adeslatt/sc-nsforest-qc-nf.git (push)

# Add the institution's repo as 'upstream'
git remote add upstream https://github.com/NIH-NLM/sc-nsforest-qc-nf.git

git remote -v
# origin    https://github.com/adeslatt/sc-nsforest-qc-nf.git (fetch)
# origin    https://github.com/adeslatt/sc-nsforest-qc-nf.git (push)
# upstream  https://github.com/NIH-NLM/sc-nsforest-qc-nf.git (fetch)
# upstream  https://github.com/NIH-NLM/sc-nsforest-qc-nf.git (push)
```

**Your fork will diverge from upstream. Plan for it.**

The moment you make a commit on your fork that does not belong on
upstream — for example, redirecting `publishDir` to your own S3
bucket — your histories have permanently diverged. This is not a
problem. It is a feature. But you must be aware of it.

---

## 3. Fork Patterns: How Much Should You Diverge?

Forking is easy. The hard question is: **how do you customise a fork
for your own use while still benefiting from upstream improvements?**

This is not hypothetical. During development of this book we ran
`adeslatt/sc-nsforest-qc-nf` — a fork of `NIH-NLM/sc-nsforest-qc-nf` —
against the JAX endometriosis dataset. The pipeline needed one change:
publish results to *our* repository, not NIH-NLM's.

The question became: where do you put that change so that it does not
cause problems when NIH-NLM improves the pipeline tomorrow?

### The diff that tells the story

```bash
git fetch upstream
git diff upstream/main main --stat
```

```
 .github/workflows/docs.yml         | 4 +++-
 data/endometriosis_Tan_2022.csv    | 2 +-
 modules/publish/publish_results.nf | 4 ++--
 nextflow.config                    | 2 +-
 params/chapter09.json              | 9 +++++++++
 5 files changed, 16 insertions(+), 5 deletions(-), 1 new file
```

Five files differ from upstream. But they differ for **different reasons**:

| File | Why it differs | Risk if upstream changes it |
|------|---------------|---------------------------|
| `docs.yml` | Bug fix (Node.js 16 → 20, fork guard) | Low — we should PR this upstream |
| `publish_results.nf` | Bug fix (hardcoded clone dir) | Low — we should PR this upstream |
| `nextflow.config` | Bug fix (missing closing quote) | Low — we should PR this upstream |
| `data/endometriosis_Tan_2022.csv` | Our dataset, our annotation choice | Medium — upstream may update this file |
| `params/chapter09.json` | **Our customisation only** | **Zero — upstream will never touch this** |

This taxonomy is the key insight:

> **Know which files upstream owns. Do not put your customisations there.**

### The three fork patterns

**Pattern 1 — Rebase your branch onto upstream (for active contributors)**

Keep a named branch for your changes. When upstream improves, rebase:

```bash
git fetch upstream
git rebase upstream/main my-branch
git push origin my-branch --force-with-lease
```

Your customisation "floats" on top of upstream forever.
This is the Linux kernel pattern — used by thousands of driver maintainers.
It requires understanding rebase, but is the cleanest long-term solution.

**Pattern 2 — Params file (for users, not contributors)**

*This is what we use for the book.*

Move all your customisations into a file that upstream will **never** touch.
In Nextflow, that is a params file:

```bash
# params/chapter09.json  — lives in YOUR fork, upstream ignores params/
{
  "publish_repo":     "adeslatt/elements-of-style-workflows",
  "publish_dest_dir": "docs/chapter-09/results",
  "datasets_csv":     "data/endometriosis_Tan_2022.csv",
  "organ":            "endometrium"
}
```

Run it with:

```bash
nextflow run main.nf \
  -params-file params/chapter09.json \
  --github_token <token>
```

Fork `main` stays mergeable with upstream forever because:
- `nextflow.config` is untouched — no conflicts
- `params/` is a new directory upstream does not own
- Bug fixes in other files can be PRed back cleanly

This is the nf-core institutional convention — every hospital or research
institute that runs nf-core pipelines uses a `<site>.config` or params file
that they own entirely. Upstream never conflicts with it.

**Pattern 3 — Cherry-pick selectively (for pragmatic divergence)**

Accept the fork will diverge. When upstream fixes something you care about,
cherry-pick that specific commit:

```bash
git cherry-pick <upstream-commit-sha>
```

Do not try to sync wholesale. Pick what matters. This is what most
bioinformatics groups actually do in practice.

### Applying Pattern 2

Here is the exact sequence used for this book:

```bash
# 1. Create the params directory (upstream doesn't have it — no conflicts possible)
mkdir -p params

# 2. Write your customisations here, not in nextflow.config
cat > params/chapter09.json << 'EOF'
{
  "publish_repo":     "adeslatt/elements-of-style-workflows",
  "publish_dest_dir": "docs/chapter-09/results",
  "datasets_csv":     "data/endometriosis_Tan_2022.csv",
  "organ":            "endometrium",
  "uberon_json":      "data/uberon_endometrium.json",
  "disease_json":     "data/disease_endometriosis.json",
  "hsapdv_json":      "data/hsapdv_reproductive_age.json"
}
EOF

# 3. Commit to fork main — this is safe, upstream will never conflict here
git add params/chapter09.json
git commit -m "book: add params/chapter09.json for Chapter 9 endometriosis run"
git push origin main

# 4. Verify what truly differs from upstream
git fetch upstream
git diff upstream/main main --stat
# Only params/chapter09.json should be purely yours
# Everything else should be PRable bug fixes
```

Now when NIH-NLM updates `nextflow.config`, `publish_results.nf`, or adds
new datasets, you can sync with:

```bash
git fetch upstream
git merge upstream/main
# No conflict — params/chapter09.json is yours alone
```

### The diff surface area principle

> **Minimise the diff surface area between your fork and upstream.**

Every file you modify is a potential future conflict. Every file you add
that upstream does not own is conflict-free forever.

Ask yourself before every fork customisation:
- Does this change belong upstream? → Open a PR
- Does this change serve only my use case? → Put it in a file upstream will never touch

If the answer to both is "yes" — it belongs upstream AND serves your use
case — open the PR. That is how open source improves: someone using
the software hits a problem, fixes it, and contributes back. You become
a contributor, not just a consumer.

---

## 4. The Publish Commit Trap

Here is a real scenario that cost half a day:

You fork a pipeline. You change one line in `publish_results.nf`
to redirect output to your own GitHub repository instead of the
institution's. You commit this:

```
50e53ab fork: redirect publish destination to adeslatt/elements-of-style-workflows
```

Then you fix four bugs. Your commit history now looks like this:

```
c49544a corrected call
a345b85 underscores wrong - hyphens for choices
0f60fcd fixed parsing
bed2f0b default to silhouette-score-col is correct
50e53ab fork: redirect publish destination       <-- THIS ONE
```

You want to push the four bug fixes to upstream. But `50e53ab`
is in the middle of your history. A simple `git push upstream main`
would push all five commits — including the one that redirects
publishing away from the institution's repository.

**You cannot push your main branch to upstream.** Not without
carrying the publish redirect along.

### The solution: cherry-pick

`git cherry-pick` applies individual commits by hash. You pick
only the ones you want:

```bash
# Start from upstream's main
git fetch upstream
git checkout -b clean-main upstream/main

# Pick only the bug fixes (skip 50e53ab)
git cherry-pick bed2f0b 0f60fcd a345b85 c49544a

# Push to the institution's repo
git push upstream clean-main:main
```

**Cherry-pick is your scalpel. Merge is your sledgehammer.**

Use `git merge` when you want everything from a branch.
Use `git cherry-pick` when you want specific commits.
In a multi-remote workflow, you will use cherry-pick far more
often than you expect.

---

## 4. When Cherry-Pick Says "Already Applied"

Sometimes git tells you a cherry-picked commit is empty:

```
The previous cherry-pick is now empty, possibly due to conflict
resolution. If you wish to commit it anyway, use:
    git commit --allow-empty
Otherwise, please use 'git cherry-pick --skip'
```

This means the changes in that commit already exist on the target
branch — perhaps from a prior pull request that was merged, or from
a parallel commit that made the same change independently.

**Do not panic.** Just skip it:

```bash
git cherry-pick --skip
```

If you are cherry-picking a sequence of commits and several are
empty, keep skipping. Git will tell you when the sequence is done.

---

## 5. The Clean-Main Pattern

When your local `main` has diverged too far from upstream and you
need to push specific changes, the cleanest approach is:

```bash
# Fetch latest from upstream
git fetch upstream

# Create a fresh branch from upstream's main
git checkout -b clean-main upstream/main

# Cherry-pick only the commits you want
git cherry-pick <hash1> <hash2> <hash3>

# Push directly to upstream's main
git push upstream clean-main:main
```

This pattern gives you a branch that is guaranteed to be compatible
with upstream, containing only your chosen commits. No merge
conflicts from your fork-specific changes. No accidental publish
redirects.

**When to use it:**
- You have fork-specific commits mixed with upstream-worthy fixes
- `git push upstream main` is rejected as non-fast-forward
- Your main branch has diverged and `git pull` would create a
  messy merge commit

---

## 6. Resolving "Non-Fast-Forward" Rejections

```
! [rejected]  main -> main (non-fast-forward)
error: failed to push some refs
hint: Updates were rejected because the tip of your current branch
hint: is behind its remote counterpart.
```

This means someone pushed to the remote since your last fetch.
Do not force-push. Instead:

```bash
git fetch upstream
git rebase upstream/main
git push upstream HEAD:main
```

If the rebase says your commits were "skipped previously applied,"
it means they are already on upstream — someone else merged them,
or a PR was accepted. Check:

```bash
git log --oneline upstream/main -5
```

If your changes are there, you are done. There is nothing to push.

---

## 7. Container Image Tags: Why `:latest` Is a Trap

Cloud platforms like CloudOS cache container images aggressively.
When your `nextflow.config` says:

```groovy
container = 'ghcr.io/nih-nlm/sc-nsforest-qc-nf/nsforest:latest'
```

The platform may use a cached version of `:latest` even after you
push a new image. The tag `:latest` is mutable — it points to
whatever was pushed most recently, but the platform does not know
that the pointer changed.

**The fix:** Tag with the git commit SHA.

```groovy
container = 'ghcr.io/nih-nlm/sc-nsforest-qc-nf/nsforest:08903ecc434ec6a2'
```

To get the current SHA:

```bash
git log --oneline -1
# 08903ec  fix: dendrogram negative distances

# Or the full SHA (some registries need it)
git rev-parse HEAD
# 08903ecc434ec6a26692458817fbb25450ab551a
```

**Tag container images with commit SHAs, not `:latest`.** (This connects
to Lesson 5 — test input for plausibility. A SHA tag is how you verify
that the right code is running.)

When something breaks on the cloud, the first question is always
"which version of the code is running?" A SHA tag answers that
immediately. `:latest` answers "whatever was most recent at some
unknown point in the past."

---

## 8. GitHub Actions and Path Filters

Your repository may have GitHub Actions that build Docker images.
A common question: if I change a Nextflow file (not a Docker file),
does the Docker image rebuild?

It depends on the workflow trigger:

```yaml
# This rebuilds on ANY push to main
on:
  push:
    branches: [main]

# This rebuilds only when Docker-related files change
on:
  push:
    branches: [main]
    paths:
      - 'container/**'
      - 'Dockerfile'
```

If your workflow uses the first pattern (no path filter), every
push to main triggers a rebuild — even if you only changed a
`.nf` file. This is wasteful but safe.

If it uses path filters, changes to Nextflow files will not
trigger a Docker rebuild. You must manually trigger the build
or change a file in the filtered path.

**Check your `.github/workflows/` directory** to understand what
triggers what. Surprises here cost time and cloud compute credits.

---

## 9. The Dropbox Problem

If your git repository lives inside a Dropbox-synced folder,
you may encounter mysterious behavior:

- `git status` shows "up to date" when files have clearly changed
- `git add` silently does nothing
- Files are "untracked" even though they exist in tracked directories

Dropbox's filesystem synchronization can interfere with git's
index. The `.git` directory contains binary index files that
Dropbox may partially sync, corrupt, or lock.

**Workarounds:**
- Run `git add -f <file>` to force-add files git does not see
- If that fails, refresh the index: `git update-index --no-assume-unchanged <file>`
- Consider keeping your git repositories outside Dropbox and
  syncing results separately

This is not a git bug. It is a filesystem-level conflict between
two systems (git and Dropbox) that both want to manage file state.

---

## 10. The Edit-on-GitHub Trap: Stash Before You Sync

Here is a scenario that catches everyone at least once:

1. You edit a file locally but do not commit
2. You realize the same file needs a fix on upstream
3. You edit it directly on GitHub (the web interface)
4. You sync your fork on GitHub (the "Sync fork" button)
5. You run `git pull` locally

Git refuses:

```
error: Your local changes to the following files would be overwritten by merge:
    nextflow.config
Please commit your changes or stash them before you merge.
Aborting
```

Your local edit conflicts with the version you just synced from
GitHub. You do not want to commit the local version — you want
the GitHub version. The fix is `git stash`:

```bash
# Shelve your local changes temporarily
git stash

# Pull the synced version from GitHub
git pull origin main

# Drop the stash (your local edit is no longer needed)
git stash drop
```

`git stash` saves your uncommitted changes on a stack and reverts
your working tree to the last commit. After pulling, `git stash drop`
discards them. If you wanted to re-apply them on top of the new
code, you would use `git stash pop` instead — but in this case,
the GitHub edit supersedes the local one.

**When to stash vs when to commit:**
- **Stash** when your local changes are experimental or superseded
- **Commit** when your local changes are the ones you want to keep
- **Never** force-pull or `checkout -- .` without checking what
  you would lose

This connects to Lesson 1 — write clearly. If you find yourself
editing the same file in two places, something about your workflow
is unclear. Pick one place to make changes and be consistent.

---

## 11. Quick Reference

### Daily commands

```bash
# See what changed
git status
git diff

# Save your work
git add <specific-files>
git commit -m "descriptive message"

# Stay current with upstream
git fetch upstream
git log --oneline upstream/main -5
```

### Multi-remote commands

```bash
# Set up remotes
git remote add upstream https://github.com/ORG/REPO.git
git remote -v

# Push to upstream (not your fork)
git push upstream main

# Cherry-pick specific commits
git cherry-pick <hash>

# The clean-main pattern
git checkout -b clean-main upstream/main
git cherry-pick <hash1> <hash2>
git push upstream clean-main:main
```

### Recovery commands

```bash
# Abort a stuck merge or cherry-pick
git merge --abort
git cherry-pick --abort

# Skip an empty cherry-pick
git cherry-pick --skip

# Stash local changes, pull, discard stash
git stash
git pull origin main
git stash drop

# See what is on a remote
git fetch upstream
git log --oneline upstream/main -5

# Check if a file is being ignored
git check-ignore -v <file>
```

### Container tagging

```bash
# Get short SHA for config
git log --oneline -1

# Get full SHA for container registry
git rev-parse HEAD

# Check which image a process uses
grep 'container' nextflow.config
```

---

## Summary

Working with git in a multi-remote biomedical workflow is not the
same as working with git on a solo project. The complexity comes
from two realities:

1. **You have fork-specific changes** (publish destinations, test
   data paths) that must never reach upstream.
2. **You have bug fixes and features** that must reach upstream
   without carrying the fork-specific changes along.

Cherry-pick and the clean-main pattern handle this cleanly.
Container SHA tagging prevents cloud caching surprises.
And checking `git remote -v` before every push prevents the
"wrong remote" mistake that has bitten every developer at least
once.

**The most important git command is not `commit` or `push`.
It is `git log --oneline -5`. Know where you are before you
decide where to go.**

---

*Next: Chapter 5 — Containerization*
