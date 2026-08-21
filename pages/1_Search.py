"""Search and result-selection page.

Owner: Debshree / search workstream.
"""

import streamlit as st

from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Search | ScreenScope", page_icon="TV", layout="wide")
apply_global_styles()

st.title("Search TV Shows")
st.caption("Search TVmaze and select a show to use across ScreenScope.")

query = st.text_input("Show title", placeholder="Try Friends or Stranger Things")
if st.button("Search", type="primary", use_container_width=False):
    if not query.strip():
        st.warning("Enter a show title before searching.")
    else:
        st.info("Search workstream: connect this action to screenscope.api.search_shows().")

