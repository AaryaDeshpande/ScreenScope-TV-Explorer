"""Small TMDB API wrapper used by both Streamlit pages.

OWNER: Xianyu

FILL-IN CHECKLIST
1. Normalize movie/TV search results.
2. Add the four detail-only fields.
3. Return the genre list.
4. Build and normalize the discover request.

The request and normalization helpers are already complete.
"""

from typing import Any

import requests

from screenscope.contracts import SUPPORTED_MEDIA_TYPES
from screenscope.explore import discover_year_parameter


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


def _validate_media_type(media_type: str) -> None:
    """Reject values that cannot be used in a TMDB movie/TV URL."""
    if media_type not in SUPPORTED_MEDIA_TYPES:
        raise ValueError("media_type must be 'movie' or 'tv'")


def _request_json(
    path: str,
    access_token: str,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """GET one TMDB endpoint and return its JSON dictionary."""
    try:
        response = requests.get(
            f"{BASE_URL}{path}",
            headers=build_headers(access_token),
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as error:
        raise TMDBAPIError("TMDB request failed. Please try again.") from error

    if not isinstance(data, dict):
        raise TMDBAPIError("TMDB returned an unexpected response.")
    return data


def _image_url(path: str | None) -> str | None:
    """Return a displayable TMDB image URL when an image path exists."""
    return f"{IMAGE_BASE_URL}{path}" if path else None


def _normalize_media(
    item: dict[str, Any], media_type: str | None = None
) -> dict[str, Any]:
    """Give movie and TV responses the same field names for the UI."""
    kind = media_type or item.get("media_type")
    if kind not in SUPPORTED_MEDIA_TYPES:
        return {}

    is_movie = kind == "movie"
    title = item.get("title" if is_movie else "name")
    original_title = item.get("original_title" if is_movie else "original_name")
    release_date = item.get("release_date" if is_movie else "first_air_date") or ""

    genres = item.get("genres") or []
    return {
        "id": item.get("id"),
        "media_type": kind,
        "title": title or original_title or "Untitled",
        "original_title": original_title or title or "Untitled",
        "release_date": release_date,
        "release_year": release_date[:4] or None,
        "genre_ids": item.get("genre_ids") or [genre.get("id") for genre in genres],
        "genre_names": [genre.get("name") for genre in genres if genre.get("name")],
        "overview": item.get("overview") or "",
        "poster_url": _image_url(item.get("poster_path")),
        "backdrop_url": _image_url(item.get("backdrop_path")),
        "rating": item.get("vote_average"),
        "vote_count": item.get("vote_count"),
        "popularity": item.get("popularity"),
        "original_language": item.get("original_language"),
    }


def search_media(query: str, access_token: str) -> list[dict[str, Any]]:
    """Return normalized movie and TV results from ``/search/multi``."""
    data = _request_json("/search/multi", access_token, {"query": query})
    normalized_results: list[dict[str, Any]] = []

    for item in data.get("results", []):
        # TODO (Xianyu 1/4): If item["media_type"] is movie or TV, normalize
        # it with _normalize_media() and append it to normalized_results.
        pass

    return normalized_results[:10]


def get_media_details(
    media_type: str, media_id: int, access_token: str
) -> dict[str, Any]:
    """Return normalized details from ``/movie/{id}`` or ``/tv/{id}``."""
    _validate_media_type(media_type)
    data = _request_json(f"/{media_type}/{media_id}", access_token)
    details = _normalize_media(data, media_type)

    # TODO (Xianyu 2/4): Use details.update({...}) to add runtime, status,
    # tagline, and homepage from data. For TV runtime, use the first value in
    # data.get("episode_run_time", []) when available.

    return details


def get_genres(media_type: str, access_token: str) -> list[dict[str, Any]]:
    """Return official genres from ``/genre/{media_type}/list``."""
    _validate_media_type(media_type)
    data = _request_json(f"/genre/{media_type}/list", access_token)

    # TODO (Xianyu 3/4): Replace [] with data.get("genres", []).
    return []


def discover_media(
    media_type: str,
    access_token: str,
    *,
    genre_id: int | None = None,
    year: int | None = None,
) -> list[dict[str, Any]]:
    """Return one normalized discover page sorted by popularity."""
    _validate_media_type(media_type)
    params: dict[str, Any] = {"sort_by": "popularity.desc"}

    # TODO (Xianyu 4/4):
    # 1. If genre_id exists, set params["with_genres"] = genre_id.
    # 2. If year exists, use discover_year_parameter(media_type) as its key.
    # 3. Request f"/discover/{media_type}" with params.
    # 4. Normalize each item in data["results"] and return the list.
    raise NotImplementedError("Xianyu: finish the discover request")
