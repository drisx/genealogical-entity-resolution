# Limitations and Scope

- The development notebook uses a sampled labeled corpus by default; full-corpus validation remains a required deployment step.
- The source dataset is not published in this repository.
- Some large preprocessing stages remain CPU/RAM bound even when GPU acceleration is available.
- The notebook simulates point lookup with in-memory dataframes; a production service would require durable indexed storage/feature retrieval.
- Open-world unlabeled candidates require adjudication before they can be treated as ground truth.
- Cluster utilities are safety-oriented policy scaffolds and require dedicated end-to-end merge tests before production use.
- Performance metrics should be regenerated from a documented run rather than copied from prior experiments.
