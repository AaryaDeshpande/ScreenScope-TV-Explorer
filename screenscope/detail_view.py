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
        if fields["poster_url"]:
            st.image(
                fields["poster_url"],
                caption="Poster",
                use_column_width=True,
            )
        else:
            st.caption("No poster available")

        

    with information_column:
        st.title(fields["title"])
        st.write(fields["overview"])
        

        st.write(f"Genres: {fields['genres']}")
        st.write(f"Release date: {fields['release_date']}")
        st.write(f"Rating: {fields['rating']}")
        st.write(f"Popularity: {fields['popularity']}")
        st.write(f"Runtime: {fields['runtime']}")
        st.write(f"Status: {fields['status']}")
        
        
