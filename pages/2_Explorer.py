"""Explorer filters and result presentation.

OWNER: Kuba

FILL-IN CHECKLIST
1. Load the genre list through the prepared API function.
2. Load filtered movie/TV results through the prepared API function.
3. Display Aarya's metrics/table and Snehal's two figures.

The page controls and helper calls are already structured below. Complete the
three small functions, keeping API, pandas, and chart logic in their modules.
"""

from datetime import date
from typing import Any

import streamlit as st

from screenscope import api
from screenscope.analysis import chart_data, results_to_dataframe, summarize_results
from screenscope.charts import popularity_figure, rating_popularity_figure
from screenscope.config import tmdb_access_token
from screenscope.explore import media_type_from_label
from screenscope.styles import apply_global_styles


EXPLORER_RESULTS_KEY = "explorer_results"


def load_genres(media_type: str, token: str) -> list[dict[str, Any]]:
    """Load the genre options for the selected media type."""
    # TODO (Kuba 1/3): Return api.get_genres(media_type, token).
    raise NotImplementedError("Kuba: load the Explorer genres")


def load_results(
    media_type: str,
    token: str,
    genre_id: int | None,
    year: int,
) -> list[dict[str, Any]]:
    """Load one filtered result page from TMDB."""
    # TODO (Kuba 2/3): Return api.discover_media() using media_type, token,
    # genre_id, and year. The function signature is already in api.py.
    raise NotImplementedError("Kuba: load the filtered Explorer results")


def render_analysis(results: list[dict[str, Any]]) -> None:
    """Display summary values, the result table, and two charts."""
    frame = results_to_dataframe(results)
    summary = summarize_results(frame)
    top_results, rated_results = chart_data(frame)

    # TODO (Kuba 3/3):
    # 1. Use three st.metric() calls for the values in summary.
    # 2. Display frame with st.dataframe().
    # 3. Display popularity_figure(top_results) and
    #    rating_popularity_figure(rated_results) with st.pyplot().
    pass


st.set_page_config(page_title="Explorer | ScreenScope", page_icon="S", layout="wide")
apply_global_styles()

st.title("Explore & Analyze")
st.caption("Filter one TMDB result page and analyze only those returned titles.")

token = tmdb_access_token()
if not token:
    st.warning("Add TMDB_ACCESS_TOKEN to .streamlit/secrets.toml first.")

media_label = st.radio("Media type", ["Movies", "TV Shows"], horizontal=True)
media_type = media_type_from_label(media_label)

genres: list[dict[str, Any]] = []
if token:
    try:
        genres = load_genres(media_type, token)
    except (api.TMDBAPIError, NotImplementedError) as error:
        st.info(str(error))

genre_by_name = {genre["name"]: genre["id"] for genre in genres}
genre_by_name = {"All genres": None, **genre_by_name}

left, right = st.columns(2)
with left:
    selected_genre = st.selectbox("Genre", list(genre_by_name))
with right:
    selected_year = st.number_input(
        "Release year",
        min_value=1900,
        max_value=date.today().year + 1,
        value=date.today().year,
    )

if st.button("Explore", type="primary", disabled=not bool(token)):
    try:
        st.session_state[EXPLORER_RESULTS_KEY] = load_results(
            media_type,
            token,
            genre_by_name[selected_genre],
            int(selected_year),
        )
    except (api.TMDBAPIError, NotImplementedError) as error:
        st.error(str(error))

results = st.session_state.get(EXPLORER_RESULTS_KEY, [])
if results:
    st.divider()
    st.subheader("Analysis of current results")
    render_analysis(results)
else:
    st.caption("Choose filters and select Explore to load the analysis.")
