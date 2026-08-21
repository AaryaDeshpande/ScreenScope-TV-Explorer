"""Selected movie/TV detail panel.

OWNER: Yan

FILL-IN CHECKLIST
1. Show the poster in the left column when one exists.
2. Show title and overview in the right column.
3. Show genres, date, rating, popularity, runtime, and status.
"""

from typing import Any

import streamlit as st

from screenscope.details import detail_fields


def render_detail_panel(media: dict[str, Any]) -> None:
    """Render a stable detail section below the search results."""
    fields = detail_fields(media)
    poster_column, information_column = st.columns([1, 3])

    with poster_column:
        # TODO (Yan 1/3): If fields["poster_url"] exists, display it with
        # st.image(). Otherwise display a short "No poster available" caption.
        pass

    with information_column:
        # TODO (Yan 2/3): Display fields["title"] and fields["overview"].
        pass

        # TODO (Yan 3/3): Display the remaining prepared values. A small
        # st.write() or st.markdown() block is enough; no custom HTML is needed.
        pass
