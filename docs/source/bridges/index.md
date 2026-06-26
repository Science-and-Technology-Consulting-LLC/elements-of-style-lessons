# Bridge patterns

Some platforms — for very good reasons — don't let you `git pull` from
inside them. The All of Us Researcher Workbench is the most common example
on our team: it supports R, R scripts, and Nextflow, but the door to
GitHub is one-way, and copy/paste is the road across.

That's not a problem to fix. It's a constraint to work *with*. This
section gives you patterns for keeping your work reproducible, versioned,
and recoverable even when the only thing crossing the boundary is text
on a clipboard.

:::{admonition} The diplomacy
:class: tip

If your director has told you to copy/paste between a constrained
environment and GitHub, **that's the right answer for your context.**
Nothing on this page contradicts that. What we offer is a small toolkit
that makes copy/paste itself behave more like a proper sync — so your
work survives platform updates, account changes, and the inevitable
"wait, which version of the script was the one that worked?"
:::

```{toctree}
:maxdepth: 1

copy-paste-reproducibly
```
