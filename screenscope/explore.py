"""Finished helpers for translating Explorer choices into TMDB values."""


def media_type_from_label(label: str) -> str:
    """Translate the page's friendly label to TMDB's media type."""
    if label == "Movies":
        return "movie"
    if label == "TV Shows":
        return "tv"
    raise ValueError("label must be 'Movies' or 'TV Shows'")


def discover_year_parameter(media_type: str) -> str:
    """Return the TMDB year parameter name for a movie or TV query."""
    if media_type == "movie":
        return "primary_release_year"
    if media_type == "tv":
        return "first_air_date_year"
    raise ValueError("media_type must be 'movie' or 'tv'")
