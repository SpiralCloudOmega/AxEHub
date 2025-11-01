import json
from pathlib import Path
from typing import Any, Dict

import yaml


def load_manifest(path: str | Path) -> Dict[str, Any]:
    path = Path(path)
    with path.open('r', encoding='utf-8') as handle:
        if path.suffix.lower() in {'.yaml', '.yml'}:
            return yaml.safe_load(handle) or {}
        return json.load(handle)


def save_manifest(manifest: Dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    with path.open('w', encoding='utf-8') as handle:
        if path.suffix.lower() in {'.yaml', '.yml'}:
            yaml.safe_dump(manifest, handle, sort_keys=False)
        else:
            json.dump(manifest, handle, indent=2)
