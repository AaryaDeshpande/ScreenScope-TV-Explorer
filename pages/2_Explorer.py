"""Filtered discovery and data-analysis page.

Owner: Snehal / Explorer, QA, and deployment workstream.
Analysis helpers and charts are owned by Kuba in ``screenscope.analysis``.
"""

from datetime import date

import streamlit as st

from screenscope.config import tmdb_access_token
from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Explorer | ScreenScope", page_icon="S", layout="wide")
apply_global_styles()

st.title("Explore & Analyze")
st.caption("Filter one TMDB result page and analyze only those returned titles.")

token = tmdb_access_token()
if not token:
    st.warning("Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml first.")

media_label = st.radio(
    "Media type", ["Movies", "TV Shows"], horizontal=True, index=0
)
left, right = st.columns(2)
with left:
    st.selectbox("Genre", ["All genres"])
with right:
    st.number_input("Release year", min_value=1900, max_value=date.today().year + 1, value=date.today().year)

if st.button("Explore", type="primary", disabled=not bool(token)):
    st.info("Explorer workstream: call discover_media(), then render pandas analysis.")

st.divider()
st.subheader("Analysis of current results")
st.caption(
    "Planned outputs: summary metrics, results table, top popularity chart, "
    "and rating-versus-popularity chart."
)
