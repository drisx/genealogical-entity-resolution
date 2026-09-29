# Evaluation Metrics

The pipeline computes model and retrieval metrics including ROC-AUC, Average Precision, Brier score, best-F1 threshold, Recall@1/5/10, MRR, NDCG@10, candidate recall, automatic-match precision/coverage, review load, and distractor false-auto-match rate.

This repository now includes aggregate outputs from one saved v5.5 optimized run under [`v5_5_optimized_run/`](v5_5_optimized_run/). The run notes describe the model-selection split, backend details, ablation scope, and deployment-gate limits. Treat the tables as outputs of that saved execution, not as independently reproduced or production-level guarantees.

Record-level rankings, candidate pairs, cleaned records, and fitted model/index artifacts are not published. See [`docs/ablation-study.md`](../../docs/ablation-study.md) for the feature-missingness study and artifact inventory.
