"""Selected movie/TV detail page."""

import streamlit as st

from screenscope import api, state
from screenscope.config import tmdb_access_token
from screenscope.detail_view import render_detail_panel
from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Detail | ScreenScope", page_icon="S", layout="wide")
apply_global_styles()

st.page_link("pages/1_Search.py", label="Back to Search")
st.title("Details")

token = tmdb_access_token()
selection = state.selected_media()

if not token:
    st.warning("Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml first.")
elif not selection:
    st.caption("Select a result from Search to see its details.")
else:
    selected_id, selected_type = selection
    try:
        selected_details = api.get_media_details(selected_type, selected_id, token)
        render_detail_panel(selected_details)
    except api.TMDBAPIError as error:
        st.error(str(error))
