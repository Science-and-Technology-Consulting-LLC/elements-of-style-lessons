# data/

Shared sample data used by `main-*.nf` runners, lesson notebooks, and
CI smoke tests. Small fixtures only — real datasets are referenced by
URL from each lesson's README.

```
data/
├── metadata/      Sample sheets, ENA exports, manifests
└── test-data/     Tiny inputs for `-profile test` runs
    └── endometriosis/   Real cells, cut down: stromal and lymphocytes
```

`test-data/` holds synthetic data for `main-bulk-de.nf`, made by
`scripts/make_synthetic_test_data.py`: two cell types, eight samples each, with
20 genes raised on purpose. They are the default for `-profile test`, because
the right answer is known.

`test-data/endometriosis/` holds two small h5ad files cut from the public
Jackson Laboratory endometriosis atlas (Tan et al., 2022) by
`lessons/differential-analysis/make_test_data.ipynb`: stromal cells and
lymphocytes, 12 donors each (3 Ctrl, 9 EuE), 50 cells per donor, 500 genes.
Run them with:

```bash
nextflow run main-bulk-de.nf -profile test \
    --samplesheet data/test-data/endometriosis/samplesheet.csv
```


Case-study-specific data lives under each `case-studies/<name>/data/`.
