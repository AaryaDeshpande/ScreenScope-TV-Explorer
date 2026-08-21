"""Movie and TV detail presentation helpers.

Owner: Selected media detail workstream.
"""

from typing import Any


def display_title(media: dict[str, Any]) -> str:
    """Return a safe title for either a normalized movie or TV result."""
    return str(media.get("title") or media.get("original_title") or "Untitled")


def detail_fields(media: dict[str, Any]) -> dict[str, Any]:
    """Return display-ready metadata for one selected movie or TV show."""
    raise NotImplementedError("Details owner: implement detail-panel mapping")
