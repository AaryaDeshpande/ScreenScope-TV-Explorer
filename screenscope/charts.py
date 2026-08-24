"""Matplotlib figures for the Explorer page.

OWNER: Snehal

FILL-IN CHECKLIST
1. Draw a horizontal bar chart of title versus popularity.
2. Draw a scatter chart of rating versus popularity.
3. Label each chart clearly and return its Figure.
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


def popularity_figure(top_results: pd.DataFrame) -> Figure:
    """Return a labeled horizontal bar chart for popular titles."""
    figure, axis = plt.subplots()

    # TODO (Snehal 1/2): Call axis.barh() using the "title" and "popularity"
    # columns. Add a title and x-axis label, then invert the y-axis so the most
    # popular title appears first.
    axis.barh(top_results["title"], top_results["popularity"], color="#2dd4bf")
    axis.set_title("Most Popular Titles")
    axis.set_xlabel("Popularity")
    axis.invert_yaxis()
    figure.tight_layout()
    return figure


def rating_popularity_figure(rated_results: pd.DataFrame) -> Figure:
    """Return a labeled scatter chart of rating versus popularity."""
    figure, axis = plt.subplots()

    # TODO (Snehal 2/2): Call axis.scatter() with "rating" on the x-axis and
    # "popularity" on the y-axis. Add a title and labels for both axes.
    axis.scatter(rated_results["rating"], rated_results["popularity"], color="#fb7185")
    axis.set_title("Rating vs. Popularity")
    axis.set_xlabel("Rating")
    axis.set_ylabel("Popularity")
    figure.tight_layout()
    return figure
