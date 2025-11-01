import json
import sys

import jsonschema
import yaml
from rich.console import Console

console = Console()


def validate_json(path: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
        console.print(f"[green]Valid JSON.[/green] Entry count: {len(data) if hasattr(data, '__len__') else 'n/a'}")
        return True
    except Exception as exc:  # pylint: disable=broad-except
        console.print(f"[red]ERROR:[/red] {exc}")
        return False


def validate_yaml(path: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            data = yaml.safe_load(handle)
        keys = list(data.keys()) if isinstance(data, dict) else []
        console.print(f"[green]Valid YAML.[/green] Top-level keys: {keys}")
        return True
    except Exception as exc:  # pylint: disable=broad-except
        console.print(f"[red]ERROR:[/red] {exc}")
        return False


def validate_manifest(path: str, schema_path: str = "schemas/microcontainer_schema.json") -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            manifest = json.load(handle)
        with open(schema_path, 'r', encoding='utf-8') as schema_handle:
            schema = json.load(schema_handle)
        jsonschema.validate(instance=manifest, schema=schema)
        console.print(f"[green]Manifest {path} OK[/green]")
        return True
    except Exception as exc:  # pylint: disable=broad-except
        console.print(f"[red]Manifest {path} INVALID:[/red] {exc}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        console.print("Usage: python validate.py [json|yaml|manifest] <path>")
    else:
        mode, file_path = sys.argv[1:3]
        if mode == "json":
            validate_json(file_path)
        elif mode == "yaml":
            validate_yaml(file_path)
        elif mode == "manifest":
            validate_manifest(file_path)
        else:
            console.print(f"Unknown mode {mode}")
