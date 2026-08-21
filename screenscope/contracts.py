"""Finished shared field names. Coordinate before changing this file."""

MEDIA_FIELDS = (
    "id",
    "media_type",
    "title",
    "original_title",
    "release_date",
    "release_year",
    "genre_ids",
    "genre_names",
    "overview",
    "poster_url",
    "backdrop_url",
    "rating",
    "vote_count",
    "popularity",
    "original_language",
)

DETAIL_FIELDS = MEDIA_FIELDS + (
    "runtime",
    "status",
    "tagline",
    "homepage",
)

SUPPORTED_MEDIA_TYPES = ("movie", "tv")
