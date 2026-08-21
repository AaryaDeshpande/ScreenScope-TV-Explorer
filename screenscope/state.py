"""Small helpers for cross-page Streamlit selection state."""

import streamlit as st


SELECTED_SHOW_ID = "selected_show_id"


def select_show(show_id: int) -> None:
    """Store the selected TVmaze show ID for detail and analysis pages."""
    st.session_state[SELECTED_SHOW_ID] = int(show_id)


def selected_show_id() -> int | None:
    """Return the currently selected TVmaze show ID, if one exists."""
    value = st.session_state.get(SELECTED_SHOW_ID)
    return int(value) if value is not None else None

