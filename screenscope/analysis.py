"""pandas transformations for the Explorer result page.

Owner: Data analysis and charts workstream.
"""

from typing import Any

import pandas as pd

from screenscope.contracts import MEDIA_FIELDS


def results_to_dataframe(results: list[dict[str, Any]]) -> pd.DataFrame:
    """Return an Explorer DataFrame with the shared media columns."""
    return pd.DataFrame(results, columns=MEDIA_FIELDS)


def summarize_results(results: pd.DataFrame) -> dict[str, float | int]:
    """Return count, mean rating, and mean popularity for current results."""
    # TODO (Kuba 1/2): Return result_count, average_rating, and
    # average_popularity. Drop missing ratings instead of filling them with 0.
    raise NotImplementedError("Analysis owner: implement result summary metrics")


def chart_data(results: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return top-popularity and rating-versus-popularity chart datasets."""
    # TODO (Kuba 2/2): Return (1) up to 10 rows sorted by popularity and (2)
    # rows with both rating and popularity for the scatter chart.
    raise NotImplementedError("Analysis owner: prepare two chart datasets")
