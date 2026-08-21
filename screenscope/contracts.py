"""Shared data contracts for API, UI, and analysis workstreams.

Owner: TVmaze API workstream.
Coordinate in the team before renaming or removing fields from these contracts.
"""

SHOW_FIELDS = (
    "id",
    "name",
    "genres",
    "language",
    "status",
    "premiered",
    "ended",
    "rating",
    "summary",
    "image_url",
    "network_name",
    "web_channel_name",
    "official_site",
    "tvmaze_url",
)

EPISODE_FIELDS = (
    "id",
    "name",
    "season",
    "number",
    "airdate",
    "runtime",
    "rating",
    "summary",
    "image_url",
)

CAST_FIELDS = (
    "person_id",
    "person_name",
    "character_name",
    "person_image_url",
)

