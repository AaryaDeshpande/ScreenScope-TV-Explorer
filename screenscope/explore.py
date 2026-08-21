"""Explorer filter and query helpers.

Owner: Explorer, QA, and deployment workstream.
"""


def discover_year_parameter(media_type: str) -> str:
    """Return the TMDB year parameter name for a movie or TV query."""
    if media_type == "movie":
        return "primary_release_year"
    if media_type == "tv":
        return "first_air_date_year"
    raise ValueError("media_type must be 'movie' or 'tv'")
