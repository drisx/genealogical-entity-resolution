from pathlib import Path


def test_required_project_files_exist():
    root = Path(__file__).resolve().parents[1]
    required = [
        root / "README.md",
        root / "configs" / "config.yaml",
        root / "requirements.txt",
        root / "notebooks" / "genealogical_entity_resolution_pipeline.ipynb",
    ]
    assert all(path.exists() for path in required)
