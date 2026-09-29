# v5.5 Optimized Run: Saved Outputs

These aggregate outputs were selected from `gpu_pipeline_v5_5_cuda_optimized_outputs-20260929T200120Z-1-001.zip` for public review.

## Included

- `model_comparison.csv`: comparison of Logistic Regression, Random Forest, LightGBM, and XGBoost. LightGBM was selected by the validation-only selection score; its recorded backend was a CPU fallback.
- `feature_group_missingness_ablation.csv`: group-level missingness results on the identity-disjoint test split, with a threshold fixed from validation.
- `individual_feature_occlusion.csv`: test-split single-feature occlusion results.
- `gpu_runtime.json`: the recorded runtime and backend details. It reports a CUDA runtime and XGBoost CUDA, while the selected LightGBM model used a CPU fallback; GPU use should not be generalized to every stage or model.
- `deployment_gates.json`: pipeline-reported gate statuses. The saved run marks candidate-recall target and identity-leakage audit as met, while full-corpus latency testing, an operational human-review workflow, and a production feature store are not marked complete.

The ablation output is **test-time missingness for the fixed selected model**. `RUN_RETRAIN_ABLATION` was false and there is no retrained-ablation result in this run. The notebook and tables report results from one saved execution; they were not independently reproduced during this repository update.

## Excluded from the public repository

The source ZIP also contains Parquet tables with query, candidate, pair, or cleaned-record rows; fitted `.joblib` estimators, vectorizers and candidate indexes; and empty correction/cannot-link templates whose schemas allow record identifiers and reviewer notes. These files were excluded because they are unnecessary for a public portfolio summary, may contain or encode source-record information, or are generated binaries. The `feature_ablation_summary.json` was not copied because it embeds the original private Drive output path; its relevant experiment settings are documented in [`docs/ablation-study.md`](../../../docs/ablation-study.md).
