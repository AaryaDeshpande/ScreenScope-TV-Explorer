"""Search page.

OWNER: Debshree

FILL-IN CHECKLIST
1. Show each result's poster or a missing-poster caption.
2. Show its title, media type, year, rating, and popularity.
3. Make the Select button save the result with state.select_media().

The API call, saved result list, and selected-detail connection are already
wired below. Only complete render_result_card().
"""

from typing import Any

import streamlit as st

from screenscope import api, state
from screenscope.config import tmdb_access_token
from screenscope.detail_view import render_detail_panel
from screenscope.search import result_card_fields
from screenscope.styles import apply_global_styles


SEARCH_RESULTS_KEY = "search_results"


def render_result_card(media: dict[str, Any]) -> None:
    """Display one normalized result and let the user select it."""
    fields = result_card_fields(media)
    card = st.container(border=True)
    poster_column, information_column = card.columns([1, 4])

    with poster_column:
        # TODO (Debshree 1/3): Display fields["poster_url"] with st.image()
        # when present. Otherwise show a "No poster available" caption.
        pass

    with information_column:
        # TODO (Debshree 2/3): Display title, media type, release year, rating,
        # and popularity from fields. Plain Streamlit text is enough.
        pass

        # TODO (Debshree 3/3): Add a Select button with a unique key. When
        # clicked, call state.select_media(fields["id"], fields["media_type"]).
        pass


st.set_page_config(page_title="Search | ScreenScope", page_icon="S", layout="wide")
apply_global_styles()

st.title("Search Movies & TV Shows")
st.caption("Search TMDB, select one movie or show, and inspect its details.")

token = tmdb_access_token()
if not token:
    st.warning("Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml first.")

query = st.text_input("Title", placeholder="Try Dune, Friends, or Stranger Things")
if st.button("Search", type="primary", disabled=not bool(token)):
    if not query.strip():
        st.warning("Enter a title before searching.")
    else:
        try:
            st.session_state[SEARCH_RESULTS_KEY] = api.search_media(query, token)
        except api.TMDBAPIError as error:
            st.error(str(error))

results = st.session_state.get(SEARCH_RESULTS_KEY, [])
if results:
    st.subheader(f"Results ({len(results)})")
    for result in results:
        render_result_card(result)

st.divider()
st.subheader("Selected details")
selection = state.selected_media()
if selection and token:
    selected_id, selected_type = selection
    try:
        selected_details = api.get_media_details(selected_type, selected_id, token)
        render_detail_panel(selected_details)
    except api.TMDBAPIError as error:
        st.error(str(error))
else:
    st.caption("Select a result above to see its details.")
