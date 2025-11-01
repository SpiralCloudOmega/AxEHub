import json
from pathlib import Path
from typing import Any, Dict

import yaml


def generate_manifest(
    name: str,
    version: str,
    entrypoint: str,
    domains: list[str],
    dependencies: list[str],
    environment: Dict[str, Any],
    metadata: Dict[str, Any],
    path: str | Path,
) -> None:
    manifest = {
        "name": name,
        "version": version,
        "entrypoint": entrypoint,
        "domains": domains,
        "dependencies": dependencies,
        "environment": environment,
        "metadata": metadata,
    }
    path = Path(path)
    with path.open('w', encoding='utf-8') as handle:
        if path.suffix.lower() in {'.yaml', '.yml'}:
            yaml.safe_dump(manifest, handle, sort_keys=False)
        else:
            json.dump(manifest, handle, indent=2)
    print(f"Manifest generated at {path}")
