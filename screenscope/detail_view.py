"""Reusable Streamlit renderer for one selected movie or TV show.

Owner: Selected media detail workstream.
"""

from typing import Any

import streamlit as st


def render_detail_panel(media: dict[str, Any]) -> None:
    """Render a stable detail section below the search results."""
    # TODO (Yan 2/2): Use detail_fields() and simple Streamlit columns. Show a
    # poster when present plus title, overview, genres, date, rating,
    # popularity, runtime, and status. Keep the layout mobile-safe.
    st.info("Details workstream: render the selected normalized TMDB item here.")
