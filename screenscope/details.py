"""Show detail and cast presentation helpers.

Owner: Show details and cast workstream.
"""

import re
from typing import Any


def plain_text_summary(summary: str | None) -> str:
    """Return a basic plain-text fallback for TVmaze's HTML summaries."""
    if not summary:
        return "No summary is available."
    return re.sub(r"<[^>]+>", "", summary).strip()


def detail_fields(show: dict[str, Any]) -> dict[str, Any]:
    """Return display-ready metadata for one selected show."""
    raise NotImplementedError("Details owner: implement detail-page mapping")

