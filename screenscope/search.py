"""Search-result transformations and card helpers.

Owner: Search and result-selection workstream.
"""

from typing import Any


def result_card_fields(media: dict[str, Any]) -> dict[str, Any]:
    """Return the normalized fields required for one movie/TV result card."""
    raise NotImplementedError("Search owner: implement result-card mapping")
