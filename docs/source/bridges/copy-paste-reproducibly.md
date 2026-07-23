# Copy/paste, reproducibly

When the only way text moves between your laptop and a constrained platform
(e.g., the All of Us Researcher Workbench) is the clipboard, three patterns
make that copy/paste behave more like a proper sync.

## Pattern 1 — Manifest-driven copy

**The idea.** Keep a tiny text file — a *manifest* — that lists every script
you're maintaining on the platform, in the order you'd recreate them. The
manifest lives in your GitHub repo. When you set up a fresh notebook server
on the platform, you copy/paste each file in the order the manifest names.

**What it looks like.** In your GitHub repo:

```
my-aou-project/
├── manifest.txt
├── 01_setup.R
├── 02_load_phenotypes.R
└── 03_topic_model.R
```

`manifest.txt`:

```
01_setup.R
02_load_phenotypes.R
03_topic_model.R
```

**Why it helps.** The manifest is the recipe. When you rebuild the
environment after a platform reset (or share it with a collaborator),
nobody has to remember "what files were there and in what order." The
manifest is the truth.

## Pattern 2 — Snapshot-on-paste

**The idea.** Every time you paste an updated script *into* the Workbench,
commit the exact same text to GitHub *from your laptop* with a matching
message. The two sides stay in lockstep because every move on one side has
a matching move on the other.

**What it looks like in practice.**

1. Open the script in your laptop editor.
2. Copy-paste the new version into the Workbench.
3. Save inside the Workbench. Run it. Confirm it works.
4. Back on your laptop:
   ```bash
   git add 02_load_phenotypes.R
   git commit -m "AoU: add column-mapping for v8 phenotype table"
   git push
   ```
5. The commit message prefix (`AoU:`) makes it easy to grep for
   platform-paired commits later.

**Why it helps.** Your Git history becomes a timeline of what was on the
Workbench when. If something breaks, `git log --oneline -- 02_*.R` tells
you exactly what changed and when.

## Pattern 3 — Round-trip checksum

**The idea.** Use a checksum (e.g., `sha256sum`) on both sides to verify
that the script you pasted in is byte-for-byte identical to the one in
GitHub. This catches whitespace-only drift that nobody would otherwise
notice until a result silently changes.

**What it looks like.** On your laptop:

```bash
sha256sum 03_topic_model.R
# d4f5a... 03_topic_model.R
```

In the Workbench, after pasting:

```bash
sha256sum 03_topic_model.R
# d4f5a... 03_topic_model.R   ← same hash → identical content
```

If the hashes differ, *something* changed in the paste: an editor "smart
quote", an autocorrect, a trailing newline. Now you know.

**Why it helps.** Most "it ran differently this time" mysteries on
copy/paste platforms turn out to be invisible character drift. A checksum
takes ten seconds and removes that whole class of bug.

## Combining the three

In practice you don't need to do all three for every script. A reasonable
rhythm is:

- **Always** maintain the manifest. It costs nothing.
- **Snapshot on paste** whenever the script is one you'll be re-running
  for a result that matters.
- **Checksum** when you're about to launch a long or expensive job, or
  when results have shifted unexpectedly.

These are *additive* habits. None of them require your director to change
how the team works. They make copy/paste into something closer to a
version-controlled sync, on whatever timeline suits you.

## Where to next

If you'd like to graduate from these patterns into native Git use on
platforms that allow it, head back to
[Version control with Git](../lessons/version-control/index.md). The same
Git habits work everywhere; the bridge patterns are just the version for
environments where the front door is locked.
