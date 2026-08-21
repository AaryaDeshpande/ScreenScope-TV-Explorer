"""ScreenScope Streamlit entry point.

Owner: Aarya / app shell and integration workstream.
Keep feature implementation in the assigned modules and two pages.
"""

import streamlit as st

from screenscope.config import tmdb_access_token
from screenscope.styles import apply_global_styles


st.set_page_config(
    page_title="ScreenScope",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_global_styles()

st.title("ScreenScope")
st.caption("Movie & TV Explorer")

st.markdown(
    """
    Search movies and TV shows, inspect one result, or explore TMDB titles by
    genre and year. The Explorer turns the current results into a small pandas
    analysis with clearly labeled charts.
    """
)

search_col, explore_col = st.columns(2)
with search_col:
    st.subheader("1. Search")
    st.write("Find a movie or TV show and open its details.")
    st.page_link("pages/1_Search.py", label="Open Search")
with explore_col:
    st.subheader("2. Explorer")
    st.write("Filter one media type and analyze the returned result page.")
    st.page_link("pages/2_Explorer.py", label="Open Explorer")

if not tmdb_access_token():
    st.warning(
        "Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml before using live data."
    )

st.divider()
st.markdown(
    "This product uses the TMDB API but is not endorsed or certified by TMDB. "
    "[Visit TMDB](https://www.themoviedb.org/)."
)
