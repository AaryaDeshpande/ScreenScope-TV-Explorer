"""Reusable Streamlit renderer for one selected movie or TV show.

Owner: Selected media detail workstream.
"""

from typing import Any

import streamlit as st


def render_detail_panel(media: dict[str, Any]) -> None:
    """Render a stable detail section below the search results."""
    st.info("Details workstream: render the selected normalized TMDB item here.")
