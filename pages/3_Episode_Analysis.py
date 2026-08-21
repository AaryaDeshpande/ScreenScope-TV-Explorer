"""Episode and season analysis page.

Owner: Kuba / analysis workstream.
"""

import streamlit as st

from screenscope.state import selected_show_id
from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Episode Analysis | ScreenScope", page_icon="TV", layout="wide")
apply_global_styles()

st.title("Episode Analysis")
show_id = selected_show_id()
if show_id is None:
    st.info("Select a show from the Search page before running analysis.")
else:
    st.info(f"Analysis workstream: analyze episodes for TVmaze show {show_id} here.")

