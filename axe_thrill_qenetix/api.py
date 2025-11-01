from fastapi import Depends, FastAPI
from pydantic import BaseModel

try:
    from axe_thrill_qenetix.db import Microcontainer, bootstrap_database
except ImportError:
    Microcontainer = None  # type: ignore
    bootstrap_database = None  # type: ignore

app = FastAPI(title="AxEThrill QENETiX API")


def get_session_factory(uri: str = "sqlite:///C:/omega_quantum/backpack.db"):
    if bootstrap_database is None:
        raise RuntimeError("Backpack database not available")
    return bootstrap_database(uri)


def get_session(session_factory=Depends(get_session_factory)):
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


class Manifest(BaseModel):
    name: str
    version: str
    entrypoint: str
    domains: list[str]
    payload: dict | None = None


@app.get("/status")
def status():
    return {"status": "AxEThrill QENETiX API is running."}


@app.post("/validate_manifest")
def validate_manifest(manifest: Manifest):
    return {"valid": True, "detail": "Manifest structure OK", "manifest": manifest.model_dump()}


@app.get("/manifests")
def list_manifests(session=Depends(get_session)):
    if Microcontainer is None:
        return []
    rows = session.query(Microcontainer).all()
    return [
        {
            "name": row.name,
            "version": row.version,
            "entrypoint": row.entrypoint,
            "domains": row.domains,
            "payload": row.payload,
        }
        for row in rows
    ]
