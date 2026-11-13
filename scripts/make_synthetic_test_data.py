"""Make the synthetic test data for main-bulk-de.nf.

Two cell types, four control and four case donors each, 400 genes. The first
20 genes are 4 times higher in the case group, so a working pipeline finds
those 20 genes and no others. The numbers are random with a fixed seed: run
this twice and the files are the same.

    python scripts/make_synthetic_test_data.py
"""
import os

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

OUT = "data/test-data"
N_GENES, N_PLANTED, CELLS_PER_DONOR, DONORS = 400, 20, 30, 4

os.makedirs(OUT, exist_ok=True)
genes = [f"G{i:03d}" for i in range(N_GENES)]
base = np.random.default_rng(0).gamma(2, 3, size=N_GENES)

rows = []
for seed, cell_type in enumerate(["TypeA", "TypeB"], start=1):
    rng = np.random.default_rng(seed)
    blocks, obs = [], []
    for condition in ["Ctrl", "EuE"]:
        for d in range(DONORS):
            mu = base.copy()
            if condition == "EuE":
                mu[:N_PLANTED] *= 4
            donor_size = rng.gamma(20, 1 / 20)
            blocks.append(rng.poisson(mu * donor_size, size=(CELLS_PER_DONOR, N_GENES)))
            obs += [(cell_type, f"{condition}{d + 1}", condition)] * CELLS_PER_DONOR
    adata = ad.AnnData(
        X=sp.csr_matrix(np.vstack(blocks).astype(np.float32)),
        obs=pd.DataFrame(obs, columns=["cell_type", "sample_id", "condition"],
                         index=[f"{cell_type}_c{i}" for i in range(len(obs))]),
        var=pd.DataFrame(index=genes),
    )
    path = f"{OUT}/synthetic_{cell_type}.h5ad"
    adata.write_h5ad(path, compression="gzip")
    rows.append({"cell_type": cell_type, "h5ad": path})

pd.DataFrame(rows).to_csv(f"{OUT}/bulk-de-samplesheet.csv", index=False)
print("wrote", len(rows), "h5ad files and the samplesheet to", OUT)
