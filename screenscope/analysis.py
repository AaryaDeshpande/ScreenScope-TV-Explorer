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
    result_count = len(results)

    clean_ratings = results["rating"].dropna()
    avg_rating = clean_ratings.mean() if not clean_ratings.empty else 0.0

    clean_pop = results["popularity"].dropna()
    avg_pop = clean_pop.mean() if not clean_pop.empty else 0.0

    return {
        "result_count": result_count,
        "average_rating": avg_rating,
        "average_popularity": avg_pop,
    }


def chart_data(results: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return top-popularity and rating-versus-popularity chart datasets."""

    top_popularity = results.sort_values("popularity", ascending=False)[:10]
    rated_results = results.dropna(subset=["rating", "popularity"])

    return top_popularity, rated_results
