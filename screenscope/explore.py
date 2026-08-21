"""Catalog filtering helpers.

Owner: Catalog exploration workstream.
Only operate on a bounded set of catalog pages during the MVP.
"""

from typing import Any


def filter_catalog(
    shows: list[dict[str, Any]],
    *,
    genre: str | None = None,
    language: str | None = None,
    status: str | None = None,
    premiered_after: int | None = None,
    minimum_rating: float | None = None,
) -> list[dict[str, Any]]:
    """Return shows matching the active exploration filters."""
    raise NotImplementedError("Explore owner: implement bounded filtering")

