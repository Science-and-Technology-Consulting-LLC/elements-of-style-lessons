# data/

Shared sample data used by `main-*.nf` runners, lesson notebooks, and
CI smoke tests. Small fixtures only — real datasets are referenced by
URL from each lesson's README.

```
data/
├── metadata/      Sample sheets, ENA exports, manifests
└── test-data/     Tiny inputs for `-profile test` runs
```

`test-data/` holds synthetic data for `main-bulk-de.nf`, made by
`scripts/make_synthetic_test_data.py`: two cell types, eight samples each, with
20 genes raised on purpose.


Case-study-specific data lives under each `case-studies/<name>/data/`.
