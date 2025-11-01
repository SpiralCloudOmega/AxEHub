# AxEThrill QENETiX Backpack

Unified toolkit for AxEThrill/QENETiX projects:
- Validation (JSON, YAML, manifest)
- Manifest schemas
- Agent/event bus templates
- Streamlit browser UI
- FastAPI web API
- File generation
- Database wiring
- External tool connectors

## Quick Start

```powershell
# From repository root
scripts\run_fastapi.ps1
scripts\run_streamlit.ps1
```

- `run_fastapi.ps1` launches the validator at `http://localhost:8000` (override host/port with parameters).
- `run_streamlit.ps1` opens the live catalogue and auto-refreshes manifests from `C:/omega_quantum/backpack.db`.
## Install

```sh
pip install -r requirements.txt
```

## Usage

- `validate.py`: Validate files
- `manifest.py`: Manifest management
- `agent.py` + `eventbus.py`: Agent/event bus patterns
- `browser_ui.py`: Streamlit browser (`streamlit run browser_ui.py`)
- `api.py`: FastAPI (`uvicorn axe_thrill_qenetix.api:app`)
- `db.py`: SQLAlchemy DB
- `generate.py`: File generation utilities
- `external_tools.py`: External tool connectors
- catalogue.py: Markdown catalogue browser
- watcher.py: CLI watcher for live manifests (python axe_thrill_qenetix/watcher.py watch)

See docs/research_streams.md for ongoing research feeds.

