"""pandas transformations for episode and season analysis.

Owner: Episode data analysis workstream.
"""

from typing import Any

import pandas as pd

from screenscope.contracts import EPISODE_FIELDS


def episodes_to_dataframe(episodes: list[dict[str, Any]]) -> pd.DataFrame:
    """Return an episode DataFrame with the shared columns.

    TODO: normalize numeric values, parse dates, and decide how missing ratings
    should be represented before charts are calculated.
    """
    return pd.DataFrame(episodes, columns=EPISODE_FIELDS)


def summarize_seasons(episodes: pd.DataFrame) -> pd.DataFrame:
    """Return season-level episode count and rating statistics."""
    raise NotImplementedError("Analysis owner: implement season summary")

