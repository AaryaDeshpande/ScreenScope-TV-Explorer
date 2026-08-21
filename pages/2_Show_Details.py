"""Selected-show details and cast page.

Owner: Yan / details workstream.
"""

import streamlit as st

from screenscope.state import selected_show_id
from screenscope.styles import apply_global_styles


st.set_page_config(page_title="Show Details | ScreenScope", page_icon="TV", layout="wide")
apply_global_styles()

st.title("Show Details")
show_id = selected_show_id()
if show_id is None:
    st.info("Select a show from the Search page first.")
else:
    st.info(f"Details workstream: load TVmaze show {show_id} and its cast here.")

