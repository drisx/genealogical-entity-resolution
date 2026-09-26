# Methodology

## Data handling

The pipeline audits required schema fields, normalizes text, handles numeric years, constructs normalized location/source keys, and computes an information-quality score. Development sampling keeps complete identity groups together before expensive processing.

## Leakage prevention

Labeled data are split by `person_id` using `GroupShuffleSplit`. The notebook explicitly checks pairwise identity-set overlap across train, calibration, validation, and test splits.

## Retrieval

Seven candidate channels are supported: strict blocking, loose blocking, surname-free retrieval, temporal/location retrieval, phonetic retrieval, character-TF-IDF retrieval, and semantic vector retrieval. Channel utility is estimated on held-out validation identities before dynamic candidate allocation.

## Representation learning

The pipeline uses character TF-IDF for lexical similarity and `intfloat/e5-small-v2` embeddings for dense semantic similarity. Normalized vectors are searched with FAISS when available, with CPU fallbacks.

## Pair modeling

Positive pairs are generated from duplicate identity groups. Negatives combine retrieved hard negatives, shortcut-breaking negatives, and random negatives.

## Ranking models

The notebook trains and compares Logistic Regression, Random Forest, LightGBM, and XGBoost using a validation-only selection policy. Probability calibration is fitted on a separate identity-disjoint calibration split.

## Decision policy

The final query layer applies calibrated scores, penalties, an ambiguity margin, and a three-way policy: automatic match, human review/abstain, or no match.

## Production considerations

The notebook also defines review-queue schemas, benchmark correction overlays, monitoring references, deployment gates, and conservative cluster-attachment/reconciliation policies. These are engineering scaffolds rather than a claim of production deployment.
