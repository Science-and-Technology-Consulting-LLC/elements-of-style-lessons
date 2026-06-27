# data/

Shared sample data used by `main-*.nf` runners, lesson notebooks, and
CI smoke tests. Small fixtures only — real datasets are referenced by
URL from each lesson's README.

```
data/
├── metadata/      Sample sheets, ENA exports, manifests
└── test-data/     Tiny inputs for `-profile test` runs
```

Case-study-specific data lives under each `case-studies/<name>/data/`.
