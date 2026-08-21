"""TMDB API boundary.

Owner: TMDB API workstream.

Implement all HTTP access here so pages do not issue ad hoc requests. Normalize
responses to ``screenscope.contracts`` and handle timeouts, HTTP errors, invalid
tokens, empty results, and missing fields.
"""

from typing import Any


BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
REQUEST_TIMEOUT_SECONDS = 10


class TMDBAPIError(RuntimeError):
    """Raised when ScreenScope cannot retrieve usable TMDB data."""


def build_headers(access_token: str) -> dict[str, str]:
    """Return the application-level Bearer authentication headers."""
    token = access_token.strip()
    if not token:
        raise ValueError("A TMDB API Read Access Token is required.")
    return {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
    }


def search_media(query: str, access_token: str) -> list[dict[str, Any]]:
    """Return normalized movie and TV results from ``/search/multi``."""
    raise NotImplementedError("API owner: implement TMDB multi search")


def get_media_details(
    media_type: str, media_id: int, access_token: str
) -> dict[str, Any]:
    """Return normalized details from ``/movie/{id}`` or ``/tv/{id}``."""
    raise NotImplementedError("API owner: implement movie and TV details")


def get_genres(media_type: str, access_token: str) -> list[dict[str, Any]]:
    """Return official genres from ``/genre/{media_type}/list``."""
    raise NotImplementedError("API owner: implement movie and TV genre lists")


def discover_media(
    media_type: str,
    access_token: str,
    *,
    genre_id: int | None = None,
    year: int | None = None,
) -> list[dict[str, Any]]:
    """Return one normalized discover page sorted by popularity."""
    raise NotImplementedError("API owner: implement movie and TV discovery")
