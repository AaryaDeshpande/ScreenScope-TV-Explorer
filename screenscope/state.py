"""Small helpers for cross-component Streamlit selection state."""

import streamlit as st


SELECTED_MEDIA_ID = "selected_media_id"
SELECTED_MEDIA_TYPE = "selected_media_type"


def select_media(media_id: int, media_type: str) -> None:
    """Store the selected TMDB ID and media type."""
    st.session_state[SELECTED_MEDIA_ID] = int(media_id)
    st.session_state[SELECTED_MEDIA_TYPE] = media_type


def selected_media() -> tuple[int, str] | None:
    """Return ``(media_id, media_type)`` when a result is selected."""
    media_id = st.session_state.get(SELECTED_MEDIA_ID)
    media_type = st.session_state.get(SELECTED_MEDIA_TYPE)
    if media_id is None or media_type not in {"movie", "tv"}:
        return None
    return int(media_id), str(media_type)
