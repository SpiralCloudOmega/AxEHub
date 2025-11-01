import time
from typing import Dict, Iterable, Set, Tuple

import requests
import typer

app = typer.Typer(help="CLI helpers for the AxEThrill backpack")


def _summarise(manifest: Dict) -> str:
    domains = ",".join(manifest.get("domains", []))
    entrypoint = manifest.get("entrypoint", "-" )
    return f"{manifest.get('name')}@{manifest.get('version')} -> {entrypoint} [{domains}]"


@app.command()
def watch(
    api: str = typer.Option("http://localhost:8000/manifests", help="FastAPI endpoint to poll"),
    interval: float = typer.Option(5.0, help="Polling interval in seconds"),
    quiet: bool = typer.Option(False, help="Suppress heartbeat output")
) -> None:
    """Poll the manifests endpoint and print new entries as they appear."""
    seen: Set[Tuple[str, str]] = set()
    typer.echo(f"Watching {api} every {interval}s. Press Ctrl+C to stop.")
    try:
        while True:
            try:
                response = requests.get(api, timeout=5)
                response.raise_for_status()
                manifests: Iterable[Dict] = response.json()
            except Exception as exc:  # pragma: no cover - network errors
                typer.echo(f"[error] {exc}")
                time.sleep(interval)
                continue

            new_items = 0
            for manifest in manifests:
                key = (manifest.get("name", ""), manifest.get("version", ""))
                if key and key not in seen:
                    seen.add(key)
                    typer.echo(f"[NEW] {_summarise(manifest)}")
                    new_items += 1
            if new_items == 0 and not quiet:
                typer.echo("[heartbeat] no new manifests")
            time.sleep(interval)
    except KeyboardInterrupt:
        typer.echo("Watcher stopped.")


if __name__ == "__main__":
    app()
