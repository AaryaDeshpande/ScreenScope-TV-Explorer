"""ScreenScope Streamlit entry point.

Owner: Aarya / integration workstream.
Keep feature-specific implementation in the assigned modules and pages.
"""

import streamlit as st

from screenscope.styles import apply_global_styles


st.set_page_config(
    page_title="ScreenScope",
    page_icon="TV",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_global_styles()

st.title("ScreenScope")
st.caption("TV Show Explorer & Episode Analytics")

st.markdown(
    """
    Search TVmaze for a show, inspect its details and cast, then analyze episode
    ratings across seasons. Use the page navigation to begin.
    """
)

left, middle, right = st.columns(3)
with left:
    st.subheader("Search")
    st.write("Find and select the correct television show.")
with middle:
    st.subheader("Inspect")
    st.write("Review show metadata, images, summary, and cast.")
with right:
    st.subheader("Analyze")
    st.write("Compare episode and season ratings with pandas charts.")

st.divider()
st.markdown("Data provided by [TVmaze](https://www.tvmaze.com/).")

