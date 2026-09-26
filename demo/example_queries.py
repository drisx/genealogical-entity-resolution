"""Minimal example showing the intended query contract.

The executable recommendation helper lives in the notebook; this file keeps the
portfolio repository lightweight and documents the input/output shape.
"""

example_query = {
    "first_name": "Example",
    "surname": "Person",
    "birthyear": 1885,
    "county": "Example County",
}

if __name__ == "__main__":
    print("Example query:")
    print(example_query)
    print("Run notebooks/genealogical_entity_resolution_pipeline.ipynb for the full pipeline.")
