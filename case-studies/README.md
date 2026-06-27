# Case studies

Threaded worked examples that combine *multiple* topical lessons into a
single real biological story. Each case study lives in its own directory
and references the lessons it uses.

| Case study | Story | Federation? |
|------------|-------|-------------|
| [`endometriosis/`](endometriosis/) | GSE179640 bulk + scRNA-seq | centralised |
| [`oadr-autoantibody/`](oadr-autoantibody/) | T1D beta-cell function across 4 SDY cohorts | **federated** |

## Where they fit in the book

- The endometriosis case study is the *centralised* path through the
  book — it touches `containers`, `nextflow-modules`,
  `nextflow-workflows`, and ends in the cross-validation between bulk
  DE and NSForest markers.
- The oadr-autoantibody case study is the *federated* path — it is
  the worked example for both `federated-computing` and
  `federated-learning`, and it sits next to the `mcp-server` and
  `platforms` lessons as the agentic-AI demonstration.
