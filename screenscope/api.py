"""TVmaze API boundary.

Owner: TVmaze API workstream.

Implement all HTTP access here so pages do not issue ad hoc requests. Normalize
responses to the contracts in ``screenscope.contracts`` and handle timeouts,
HTTP errors, missing fields, and TVmaze's 429 response.
"""

from typing import Any


BASE_URL = "https://api.tvmaze.com"
REQUEST_TIMEOUT_SECONDS = 10


class TVMazeAPIError(RuntimeError):
    """Raised when ScreenScope cannot retrieve usable TVmaze data."""


def search_shows(query: str) -> list[dict[str, Any]]:
    """Return normalized shows from ``/search/shows?q=:query``."""
    raise NotImplementedError("API owner: implement TVmaze show search")


def get_show(show_id: int) -> dict[str, Any]:
    """Return one normalized show from ``/shows/:id``."""
    raise NotImplementedError("API owner: implement show details")


def get_episodes(show_id: int) -> list[dict[str, Any]]:
    """Return normalized episodes from ``/shows/:id/episodes``."""
    raise NotImplementedError("API owner: implement episode retrieval")


def get_cast(show_id: int) -> list[dict[str, Any]]:
    """Return normalized cast from ``/shows/:id/cast``."""
    raise NotImplementedError("API owner: implement cast retrieval")


def get_catalog_page(page: int = 0) -> list[dict[str, Any]]:
    """Return one bounded page from ``/shows?page=:num``."""
    raise NotImplementedError("API owner: implement one catalog page")

