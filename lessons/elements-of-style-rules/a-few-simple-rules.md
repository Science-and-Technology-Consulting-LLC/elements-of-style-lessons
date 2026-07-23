# A few simple rules

*Adapted from the NICHD Kids First / INCLUDE course
([source](https://nih-nichd.github.io/classes/day-1-reasoning/A-Few-Simple-Rules/)) — woven into
the [elements-of-style-rules](README.md) lesson.*

:::{admonition} Two ways to run this walkthrough
:class: tip

- **In a terminal** — on your laptop, Lifebit, or CAVATICA Data Studio.
  Copy each shell block below into your terminal.
- **In the paired notebook** [`a-few-simple-rules.ipynb`](../ipynb/a-few-simple-rules.ipynb) — every code cell
  is a shell command executed by the Jupyter **Bash** kernel.

The walkthrough is **self-contained**. Work through *Set up the
environment* below once, then run the steps top-to-bottom.
:::

## Set up the environment

### One time — register the Bash kernel

Only needed if you'll run the paired notebook in JupyterLab. Skip if
you're doing everything in a terminal.

```bash
pip install bash_kernel
python -m bash_kernel.install
```

Restart JupyterLab; the launcher now shows a **Bash** tile.

### Every time — verify the tools this walkthrough uses

The commands below call one or more of these tools. Where a check
fails, the linked lesson has the install instructions.

| Tool | Check | If missing, see |
|---|---|---|
| Bash / Git Bash | `bash --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Git | `git --version` | [command-line-and-git-bash](../command-line-and-git-bash/README.md) |
| Conda | `conda --version` | [conda-environments](../conda-environments/README.md) |
| GitHub CLI (`gh`) | `gh --version` | [version-control](../version-control/why-git-and-setup.md) |
| Docker | `docker --version` | [containers](../containers/README.md) |
| Nextflow | `nextflow -version` | [nextflow-workflows](../nextflow-workflows/README.md) |
| Python 3 | `python3 --version` | [conda-environments](../conda-environments/README.md) |

Run them all at once:

```bash
for cmd in bash git conda gh docker nextflow python3; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s
" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING
" "$cmd"
  fi
done
```


## Disclaimer (from the original)

> The views expressed in this course represent the views of Anne Deslattes
> Mays, PhD and do not represent the views of NICHD, NIH, or the United
> States Government.
>
> In what follows is my development of a practice that enables workflow and
> platform independence facilitating reproducibility.

## Learning from those who have walked the journey

Kernighan, B. W., & Plauger, P. J. (1978). *The Elements of Programming
Style* (2nd ed.). McGraw Hill. ISBN 0-07-034207-5.

In 1919 the first World War was at its close, and a student — E. B. White —
took English 8 with William Strunk Jr. The course required *The Elements of
Style*, a slim book whose durability inspired Kernighan and Plauger's *The
Elements of Programming Style*. This lesson adapts those same maxims to the
world of workflows and containers — beginning, as Strunk and Kernighan did,
with philosophy before technique.

## The 55 pithy rules — as Kernighan and Plauger wrote them

Each rule is one line. Rules marked ***timeless (italic emphasis)*** carry
Annie's annotation about *why* the rule still fits containerised,
workflow-driven, agentic-AI-era work.

1. Write clearly — don't be too clever. ***timeless***
2. Say what you mean, simply and directly. ***timeless***
3. Use **containerised processes** (in a way similar to library functions)
   whenever feasible.
4. Avoid too many temporary variables.
5. Write clearly — don't sacrifice clarity for efficiency. ***timeless***
6. Let the machine do the dirty work. ***timeless***
7. Replace repetitive expressions by calls to common functions.
   ***timeless — when you catch yourself repeating, extract a function.***
8. Parenthesise to avoid ambiguity.
9. Choose variable names that won't be confused. ***timeless***
10. Avoid unnecessary branches.
11. If a logical expression is hard to understand, try transforming it.
    ***timeless***
12. Choose a data representation that makes the program simple.
13. Write first in easy-to-understand pseudo language; then translate into
    whatever language you have to use. ***timeless***
14. Modularise. Use procedures and functions.
    ***…and containerise — use GitHub Actions to build, test, and keep them
    up-to-date.***
15. Avoid gotos completely if you can keep the program readable.
16. Don't patch bad code — rewrite it.
17. Write and test a big program in small pieces.
    ***timeless — do this via tested, containerised processes.***
18. Use recursive procedures for recursively-defined data structures.
19. Test input for plausibility and validity.
    ***timeless — always understand the source of your data.***
20. Make sure input doesn't violate the limits of the program.
21. Terminate input by end-of-file marker, not by count.
22. Identify bad input; recover if possible.
23. Make input easy to prepare and output self-explanatory.
24. Use uniform input formats.
25. Make input easy to proofread. ***timeless***
26. Use self-identifying input. Allow defaults. Echo both on output.
27. Make sure all variables are initialised before use.
28. Don't stop at one bug.
29. Use debugging compilers.
    ***timeless — in workflow languages, test each step separately, verify
    inputs/outputs, containerise, test.***
30. Watch out for off-by-one errors. ***timeless***
31. Take care to branch the right way on equality.
32. Be careful if a loop exits to the same place from the middle and the
    bottom.
33. Make sure your code does "nothing" gracefully.
34. Test programs at their boundary values.
35. Check some answers by hand. ***timeless***
36. 10.0 times 0.1 is hardly ever 1.0. ***timeless — always aim for simplicity.***
37. 7/8 is zero while 7.0/8.0 is not zero. ***timeless — belongs in an R or
    Python class.***
38. Don't compare floating point numbers solely for equality. ***timeless.***
39. **Make it right before you make it faster.** ***timeless for everything.***
40. Make it fail-safe before you make it faster. ***timeless.***
41. Make it clear before you make it faster. ***timeless.***
42. Don't sacrifice clarity for small gains in efficiency. ***timeless.***
43. Let your compiler do the simple optimisations.
    ***In our world of platforms, let your platform help you — Platform-as-a-Service
    (CAVATICA by Seven Bridges, CloudOS by Lifebit).***
44. Don't strain to re-use code; reorganise instead. ***timeless — the more
    you perform a task, the simpler you see how to get it done. Exploit that
    simplicity and rewrite.***
45. Make sure special cases are truly special. ***timeless.***
46. Keep it simple to make it faster.
47. Don't diddle code to make it faster — find a better algorithm.
    ***timeless — find another bioinformatics algorithm, collaborate, give
    attribution, expand your reach.***
48. Instrument your programs. Measure before making efficiency changes.
    ***timeless — did the change do what you thought?***
49. Make sure comments and code agree. ***timeless.***
50. Don't just echo the code with comments — make every comment count.
    ***timeless.***
51. Don't comment bad code — rewrite it. ***timeless.***
52. Use variable names that mean something.
53. Use statement labels that mean something.
54. Format a program to help the reader understand it. ***timeless.***
55. Document your data layouts. ***timeless.***

## What to carry forward

The rules that show up in **every** lesson of this curriculum, in
plain-English form:

- **Write clearly.** Names, structure, comments.
- **Pseudo-code first.** Design in prose before you commit to a language.
- **Modularise.** One container, one job, one CLI.
- **Build and test in small pieces.** A Nextflow module you can smoke-test
  in isolation is a module that survives.
- **Validate inputs.** Every parameter has a check.
- **Make it right before faster.** Correctness first; optimise only when
  the numbers say to.
- **Keep it simple.** Rewrite before you patch.
- **Document data and functions.** Every column has units; every CLI flag
  has a meaning.

## Where to next

→ Back to the [elements-of-style-rules lesson](README.md).

→ Then [command-line-and-git-bash](../command-line-and-git-bash/README.md).
