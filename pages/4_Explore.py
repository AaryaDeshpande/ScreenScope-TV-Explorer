"""Bounded catalog exploration page.

Owner: Snehal / explore, QA, and deployment workstream.
"""

import streamlit as st

from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Explore | ScreenScope", page_icon="TV", layout="wide")
apply_global_styles()

st.title("Explore TV Shows")
st.caption("Filter a bounded TVmaze catalog sample when no title is in mind.")

left, middle, right = st.columns(3)
with left:
    st.selectbox("Genre", ["All genres"])
with middle:
    st.selectbox("Language", ["All languages"])
with right:
    st.slider("Minimum rating", 0.0, 10.0, 0.0, 0.5)

st.info("Explore workstream: populate filters and show cards from bounded catalog pages.")

