# Feature Ablation and Missingness Results

The review notebook includes a feature-missingness study for the selected ranker. It evaluates the identity-disjoint test split while keeping the decision threshold fixed at the value chosen on validation. The saved run contains two experiments:

- **Group missingness:** masks a full evidence group at test time to measure the immediate effect if that evidence is unavailable after training.
- **Individual feature occlusion:** replaces one feature at a time with its neutral value. Correlated features can compensate for each other, so group results are more informative about evidence loss.

The optional drop-group retraining experiment was disabled in the saved run. The results therefore do not measure how a newly trained model would adapt when a feature group is permanently unavailable.

## Findings from the saved run

In the group-missingness table, removing all identity text produced the largest reported average-precision loss, followed by removing birth-year features. Removing structured name features had a larger fixed-threshold F1 impact than removing learned text representations in this run. In the individual-feature table, birth-year similarity and first-name similarity ranked highest by average-precision loss.

These are pipeline-reported results from one saved run. They are not independently rerun here, and should not be read as production guarantees or as evidence that every data population will behave the same way.

## Saved files

- [`model_comparison.csv`](../results/metrics/v5_5_optimized_run/model_comparison.csv) — four-model training/validation comparison and validation-only selection.
- [`feature_group_missingness_ablation.csv`](../results/metrics/v5_5_optimized_run/feature_group_missingness_ablation.csv) — aggregate test-split results by evidence group.
- [`individual_feature_occlusion.csv`](../results/metrics/v5_5_optimized_run/individual_feature_occlusion.csv) — aggregate single-feature occlusion results.
- [`gpu_runtime.json`](../results/metrics/v5_5_optimized_run/gpu_runtime.json) — runtime/backend report from the run.
- [`deployment_gates.json`](../results/metrics/v5_5_optimized_run/deployment_gates.json) — pipeline-reported deployment gate status.

The saved tables contain aggregate metrics and feature labels. Query rankings, candidate rows, cleaned record tables, corrections, and fitted model/index binaries were excluded from this public repository copy.

See the [run notes](../results/metrics/v5_5_optimized_run/README.md) for backend details and scope limitations.
