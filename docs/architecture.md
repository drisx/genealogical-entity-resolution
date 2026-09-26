# Architecture

```text
Raw genealogical records
          |
          v
Schema audit + deterministic cleaning
          |
          v
Identity-safe train/calibration/validation/test split
          |
          v
+---------------- Multi-pass retrieval ----------------+
| strict | loose | surname-free | temporal/location  |
| phonetic | TF-IDF lexical | semantic/vector search |
+-------------------------------------------------------+
          |
          v
Candidate pool + provenance
          |
          v
Pairwise lexical / semantic / structured features
          |
          v
Logistic Regression / Random Forest / LightGBM / XGBoost
          |
          v
Held-out probability calibration
          |
          v
Penalty + ambiguity policy
          |
          v
Automatic match / Human review or abstain / No match
          |
          v
Monitoring, governance, and safe cluster utilities
```
