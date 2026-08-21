"""Search-result transformations and presentation helpers.

Owner: Search and result-selection workstream.
"""

from typing import Any


def result_card_fields(show: dict[str, Any]) -> dict[str, Any]:
    """Return the fields required to render one result card."""
    raise NotImplementedError("Search owner: implement result-card mapping")

