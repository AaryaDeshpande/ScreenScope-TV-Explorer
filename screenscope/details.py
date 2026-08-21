"""Finished helper that gives the Detail panel safe display values."""

from typing import Any


def display_title(media: dict[str, Any]) -> str:
    """Return a safe title for either a normalized movie or TV result."""
    return str(media.get("title") or media.get("original_title") or "Untitled")


def detail_fields(media: dict[str, Any]) -> dict[str, Any]:
    """Return display-ready metadata for one selected movie or TV show."""
    genres = media.get("genre_names") or []
    rating = media.get("rating")
    popularity = media.get("popularity")
    runtime = media.get("runtime")
    return {
        "title": display_title(media),
        "poster_url": media.get("poster_url"),
        "overview": media.get("overview") or "No overview available.",
        "genres": ", ".join(genres) if genres else "Not available",
        "release_date": media.get("release_date") or "Not available",
        "rating": rating if rating is not None else "Not rated",
        "popularity": popularity if popularity is not None else "Not available",
        "runtime": runtime if runtime is not None else "Not available",
        "status": media.get("status") or "Not available",
    }
