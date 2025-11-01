import time
from typing import Any, Dict

import streamlit as st

try:
    from axe_thrill_qenetix.db import Microcontainer, bootstrap_database
except ImportError:
    Microcontainer = None  # type: ignore
    bootstrap_database = None  # type: ignore


def fetch_manifests(session_factory):
    session = session_factory()
    try:
        rows = session.query(Microcontainer).all()
        return [
            {
                'name': row.name,
                'version': row.version,
                'entrypoint': row.entrypoint,
                'domains': row.domains,
                'payload': row.payload,
            }
            for row in rows
        ]
    finally:
        session.close()


st.title('AxEThrill Manifest Catalogue')

if Microcontainer is None or bootstrap_database is None:
    st.error('Backpack database module not available. Ensure axe_thrill_qenetix is on PYTHONPATH.')
else:
    db_uri = st.text_input('Database URI', 'sqlite:///C:/omega_quantum/backpack.db')
    session_factory = bootstrap_database(db_uri)

    refresh_interval = st.slider('Auto-refresh interval (seconds)', 0, 60, 5)

    container = st.container()

    def render() -> None:
        container.empty()
        manifests = fetch_manifests(session_factory)
        container.success(f'Loaded {len(manifests)} manifest(s)')
        for manifest in manifests:
            with container.expander(f"{manifest['name']}@{manifest['version']}"):
                st.json(manifest)

    render()

    if refresh_interval > 0:
        time.sleep(refresh_interval)
        st.experimental_rerun()
