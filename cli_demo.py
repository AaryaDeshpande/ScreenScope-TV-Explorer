"""Command-line demo for searching TMDB through the shared API wrapper."""

import argparse
import os

from screenscope.api import TMDBAPIError, search_media


def main() -> int:
    """Search TMDB and print a compact list of normalized results."""
    parser = argparse.ArgumentParser(description="Search movies and TV shows")
    parser.add_argument("query", help="Title to search for, such as Dune")
    args = parser.parse_args()

    token = os.getenv("TMDB_ACCESS_TOKEN")
    if not token:
        parser.error("set TMDB_ACCESS_TOKEN before running the demo")

    try:
        results = search_media(args.query, token)
    except TMDBAPIError as error:
        parser.error(str(error))

    if not results:
        print(f'No movie or TV results found for "{args.query}".')
        return 0

    print(f'Results for "{args.query}":')
    for result in results:
        year = result.get("release_year") or "year unknown"
        rating = result.get("rating")
        rating_text = f"{rating:.1f}" if isinstance(rating, (int, float)) else "unrated"
        print(
            f'- {result["title"]} '
            f'({result["media_type"]}, {year}, rating {rating_text})'
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
