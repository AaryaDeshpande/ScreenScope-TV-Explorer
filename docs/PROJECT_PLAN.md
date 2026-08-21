# ScreenScope Project Plan

## Product Statement

ScreenScope helps a user search for a movie or TV show, inspect useful details,
and explore how rating and popularity vary within a filtered TMDB result set.

## Required MVP

### Tab 1: Search

- Title query using TMDB `/search/multi`
- Filter the response to `movie` and `tv` records
- Up to ten result cards with poster fallback, title, type, year, rating, and
  popularity
- Select action stores both the TMDB ID and media type
- Selected detail panel calls `/movie/{id}` or `/tv/{id}` and displays overview,
  genres, date, rating, vote count, popularity, runtime, and status

### Tab 2: Explorer

- Media selector: Movie or TV Show
- Genre list from `/genre/movie/list` or `/genre/tv/list`
- Filters: one genre and one release/first-air year
- One page from `/discover/movie` or `/discover/tv`
- Sort by `popularity.desc`
- pandas DataFrame containing the normalized shared media fields
- Summary metrics: result count, average rating, and average popularity
- Table with title, year, rating, vote count, and popularity
- Chart 1: top titles by popularity
- Chart 2: rating versus popularity, with vote count available for context

## Interpretation Rules

- The charts describe only the current filtered API result page.
- Popularity and rating are different measures and must not be conflated.
- A high rating with very few votes should not be presented as definitive.
- Missing ratings are excluded and counted, not silently converted to zero.
- Use "most popular in these results," not "globally trending."

## Authentication

Use one application-level TMDB API Read Access Token as a Bearer token. Store
it locally in `.streamlit/secrets.toml` and in Streamlit Community Cloud
secrets. Account details, user sessions, favorites, and watchlists are outside
the MVP.

## Stretch Goals Only After Deployment

- Daily/weekly trending endpoint as a separate view
- Cast and crew
- Trailer links
- Compare two titles
- Watch-provider availability

## Definition of Done

The app is done when a visitor can search and inspect a movie or TV show, run a
genre/year discovery query, understand two charts based on the returned data,
and use the public Streamlit URL without crashes. All six contributors must
have merged meaningful pull requests, tests must pass, no secret may appear in
Git history, and TMDB attribution must be visible.
