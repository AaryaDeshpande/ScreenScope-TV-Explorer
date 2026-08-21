# ScreenScope Project Plan

## Product Statement

ScreenScope helps a user find a television show, inspect reliable show details,
and understand episode-rating patterns without moving between multiple sites.

## Required MVP

### Search

- Title query using TVmaze `/search/shows?q=:query`
- Up to ten result cards
- Image fallback, name, premiere year, genres, language, rating, and status
- Select action that stores the TVmaze show ID in Streamlit session state

### Show Details

- Show image and plain-text summary
- Genres, language, status, premiere and end dates
- Rating, network or web channel, official site, and TVmaze link
- Main cast from `/shows/:id/cast`

### Episode Analysis

- Episodes from `/shows/:id/episodes`
- pandas DataFrame with missing values handled explicitly
- KPI row: seasons, episodes, rated episodes, average episode rating
- Episode-rating chart by season and episode
- Season summary chart or table
- Best- and lowest-rated episodes with a minimum-vote caveat if needed

### Explore

- A bounded catalog sample from one or a few `/shows?page=:num` pages
- Filters for genre, language, status, premiere year, and minimum rating
- Clearly label this as a catalog sample rather than global trending data

## Important Language

TVmaze does not provide a universal "trending" metric in its public show
records. Do not label high-rated or recently premiered shows as trending unless
the team defines and displays a transparent proxy. Prefer labels such as:

- "Highest-rated shows in this catalog sample"
- "Recently premiered shows in this sample"
- "Most common genres in the analyzed results"

## Stretch Goals

- Compare two selected shows
- Broadcast and streaming schedule
- Person search and credits
- Recommendation heuristic based on shared genres and language
- Additional movie API added only after the TV MVP is deployed

## Definition of Done

The app is done when a new visitor can search, select, inspect, and analyze a
show on the public Streamlit URL; API failures and missing data do not crash the
app; all six contributors have merged meaningful PRs; and the README, TVmaze
credit, tests, and demo are complete.

