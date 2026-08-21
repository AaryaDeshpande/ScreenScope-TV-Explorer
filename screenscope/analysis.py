"""pandas transformations for the Explorer page.

OWNER: Aarya

FILL-IN CHECKLIST
1. Calculate three summary values for the current result DataFrame.
2. Prepare a top-popularity DataFrame for a bar chart.
3. Prepare rows with both rating and popularity for a scatter chart.
"""

from typing import Any

import pandas as pd

from screenscope.contracts import MEDIA_FIELDS


def results_to_dataframe(results: list[dict[str, Any]]) -> pd.DataFrame:
    """Return an Explorer DataFrame with the shared media columns."""
    return pd.DataFrame(results, columns=MEDIA_FIELDS)


def summarize_results(results: pd.DataFrame) -> dict[str, float | int]:
    """Return count, mean rating, and mean popularity for current results."""
    # TODO (Aarya 1/2):
    # 1. result_count is len(results).
    # 2. Drop missing values before averaging the "rating" column.
    # 3. Average the "popularity" column.
    # 4. Return exactly these keys: result_count, average_rating,
    #    average_popularity. Use 0.0 when an average has no values.
    raise NotImplementedError("Aarya: calculate the three summary values")


def chart_data(results: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return top-popularity and rating-versus-popularity chart datasets."""
    # TODO (Aarya 2/2):
    # 1. Sort by "popularity" descending and keep the first 10 rows.
    # 2. Create another DataFrame after dropna(subset=["rating", "popularity"]).
    # 3. Return both DataFrames as: return top_popularity, rated_results
    raise NotImplementedError("Aarya: prepare the two chart datasets")
