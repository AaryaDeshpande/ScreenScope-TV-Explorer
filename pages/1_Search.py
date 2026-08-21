"""Search, result selection, and selected-detail page.

Owner: Debshree / search workstream.
The reusable detail panel is owned by Yan in ``screenscope.detail_view``.
"""

import streamlit as st

from screenscope.config import tmdb_access_token
from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Search | ScreenScope", page_icon="S", layout="wide")
apply_global_styles()

st.title("Search Movies & TV Shows")
st.caption("Search TMDB, select one movie or show, and inspect its details.")

token = tmdb_access_token()
if not token:
    st.warning("Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml first.")

query = st.text_input("Title", placeholder="Try Dune, Friends, or Stranger Things")
# TODO (Debshree 2/2): On Search, call api.search_media(). Render each result
# using search.result_card_fields(). A Select button should call
# state.set_selected_media(id, media_type).
if st.button("Search", type="primary", disabled=not bool(token)):
    if not query.strip():
        st.warning("Enter a title before searching.")
    else:
        st.info("Search workstream: connect to screenscope.api.search_media().")

st.divider()
st.subheader("Selected details")
# TODO (Yan integration): Read the selected id/type from state, call
# api.get_media_details(), and pass the result to render_detail_panel().
st.caption("The selected movie or TV detail panel will render here.")
