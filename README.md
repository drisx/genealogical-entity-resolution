# Large-Scale Genealogical Entity Resolution

> A production-oriented machine learning pipeline for record linkage in noisy genealogical data using hybrid candidate retrieval, semantic embeddings, fuzzy matching, supervised pair classification, probability calibration, and human-in-the-loop decision policies.

## Why this project matters

Entity resolution is the task of deciding which records refer to the same real-world entity. The same technical problem appears in customer deduplication, patient matching, fraud detection, CRM consolidation, master-data management, historical record linkage, and knowledge graph construction.

This project uses a genealogical dataset as the domain, but the engineering and machine-learning patterns are designed to transfer to other record-linkage problems.

## What the pipeline demonstrates

- Identity-safe train/calibration/validation/test splitting
- Deterministic text, location, year, and metadata normalization
- Seven candidate-retrieval channels
- Character TF-IDF lexical retrieval
- E5 semantic embeddings and dense vector search
- FAISS/HNSW retrieval with CPU fallbacks
- Hard-negative, random-negative, and shortcut-negative sampling
- Pairwise feature engineering across lexical, semantic, temporal, geographic, relational, and data-quality signals
- Logistic Regression, Random Forest, LightGBM, and XGBoost comparison
- Held-out Platt probability calibration
- Query-level ranking evaluation with Recall@K, MRR, and NDCG@10
- Ambiguity-aware match / review / no-match decisions
- Rule-based penalties and review safeguards
- Review-queue and benchmark-correction schemas
- Monitoring references and deployment gates
- Conservative cluster attachment and offline delta reconciliation utilities

## System architecture

```text
Raw records
    |
    v
Schema audit + cleaning
    |
    v
Identity-safe split
    |
    v
Multi-pass candidate retrieval
    |
    +--> Strict blocking
    +--> Loose blocking
    +--> Surname-free retrieval
    +--> Temporal + location
    +--> Phonetic retrieval
    +--> TF-IDF retrieval
    +--> Dense vector retrieval
    |
    v
Candidate pool + provenance
    |
    v
Pairwise feature engineering
    |
    v
Model comparison
    |   Logistic Regression
    |   Random Forest
    |   LightGBM
    |   XGBoost
    v
Probability calibration
    |
    v
Decision policy
    |
    +--> Automatic match
    +--> Human review / abstain
    +--> No match
```

See [architecture.md](docs/architecture.md) for a fuller description.

## Data leakage controls

Entity resolution is especially vulnerable to leakage because multiple records can belong to the same underlying identity. The notebook therefore uses `GroupShuffleSplit` on `person_id` and explicitly audits overlap between the split identity sets before model development proceeds.

Predictive features exclude the raw person identifier, raw source identifier, and internal relationship IDs. The notebook also fits lexical/vector preprocessing on training data before transforming held-out splits.

## Retrieval design

The retrieval stage is intentionally hybrid. Exact/structured blocking helps control cost, while lexical and semantic retrieval recover records affected by spelling variation, missing names, and historical noise.

Channel utility is estimated on validation identities, then a dynamic pre-ranking budget allocates candidate slots across available channels. This makes the retrieval layer measurable rather than relying on one fixed similarity method.

## Modeling and calibration

The pairwise ranker uses engineered similarity and consistency features. Four model families are compared under a validation-only model-selection policy. A separate calibration split is used for Platt scaling before query-level decisions are applied.

The decision layer does not force a binary answer. It uses score thresholds, ambiguity margins, and rule-triggered review conditions to support three outcomes: automatic match, human review/abstain, and no match.

## Evaluation

The pipeline computes:

- ROC-AUC
- Average Precision
- Brier score
- Best-F1 threshold / F1 / precision / recall
- Candidate Recall
- Recall@1, Recall@5, Recall@10
- Mean Reciprocal Rank (MRR)
- NDCG@10
- Automatic-match precision and coverage
- Human-review load
- Distractor false-auto-match rate

The uploaded notebook did not include a complete persisted results table for a final full-corpus run, so this repository deliberately does **not** publish invented performance numbers. Run the notebook to generate the metrics for a documented experiment.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── requirements-gpu.txt
├── environment.yml
├── configs/config.yaml
├── notebooks/
│   └── genealogical_entity_resolution_pipeline.ipynb
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   └── limitations.md
├── data/README.md
├── models/README.md
├── results/
│   ├── figures/
│   └── metrics/README.md
├── demo/example_queries.py
├── tests/test_config.py
└── .github/workflows/tests.yml
```

## Reproducibility

### CPU baseline

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Then open `notebooks/genealogical_entity_resolution_pipeline.ipynb` and set the data path appropriate for your environment.

### GPU execution

The notebook detects CUDA availability and supports GPU-backed embeddings plus optional RAPIDS acceleration. GPU-capable LightGBM/XGBoost configurations include CPU fallbacks when the installed binary/runtime does not support CUDA.

For environment-specific GPU setup, see [methodology.md](docs/methodology.md).

## Scope and limitations

This repository is a portfolio implementation and research/engineering demonstration, not a claim of production deployment. Full-corpus load testing, durable feature storage, operational human review, and production monitoring require additional infrastructure.

See [limitations.md](docs/limitations.md).

## Skills demonstrated

**Data Science:** data quality, feature engineering, leakage prevention, model evaluation, error-aware decision policies

**Machine Learning:** classification, ranking, hard-negative mining, model comparison, calibration

**NLP / Information Retrieval:** TF-IDF, embeddings, semantic similarity, hybrid retrieval, vector search

**Data Engineering:** large-dataset processing, reproducibility, configuration, offline artifacts

**ML Engineering / MLOps:** tests, CI, model artifacts, monitoring references, deployment gates, human-in-the-loop workflows

## Author

**Lukman Idris** — Data Scientist | Machine Learning | AI | NLP

[LinkedIn](https://www.linkedin.com/in/lukman-idris-160ba8141/) · [GitHub](https://github.com/drisx)
