"""Configuration helpers that never expose project secrets."""

import os

import streamlit as st


def tmdb_access_token() -> str | None:
    """Return the TMDB read token from Streamlit secrets or the environment."""
    try:
        token = st.secrets.get("TMDB_ACCESS_TOKEN")
    except FileNotFoundError:
        token = None
    return token or os.getenv("TMDB_ACCESS_TOKEN")
