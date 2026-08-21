"""Finished helper that gives the Search page safe display values."""

from typing import Any


def result_card_fields(media: dict[str, Any]) -> dict[str, Any]:
    """Return the normalized fields required for one movie/TV result card."""
    rating = media.get("rating")
    popularity = media.get("popularity")
    return {
        "id": media.get("id"),
        "media_type": media.get("media_type") or "Unknown",
        "title": media.get("title") or "Untitled",
        "release_year": media.get("release_year") or "Year unavailable",
        "poster_url": media.get("poster_url"),
        "rating": rating if rating is not None else "Not rated",
        "popularity": popularity if popularity is not None else "Not available",
    }
