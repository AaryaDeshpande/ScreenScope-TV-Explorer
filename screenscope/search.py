"""Search-result transformations and card helpers.

Owner: Search and result-selection workstream.
"""

from typing import Any


def result_card_fields(media: dict[str, Any]) -> dict[str, Any]:
    """Return the normalized fields required for one movie/TV result card."""
    # TODO (Debshree 1/2): Return only id, media_type, title, release_year,
    # poster_url, rating, and popularity with friendly missing-value fallbacks.
    raise NotImplementedError("Search owner: implement result-card mapping")
