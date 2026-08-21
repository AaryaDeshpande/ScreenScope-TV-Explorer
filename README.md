# ScreenScope

ScreenScope is a collaborative Python and Streamlit app for searching movies
and TV shows, viewing their details, and exploring popularity and rating
patterns with live data from the
[TMDB API](https://developer.themoviedb.org/docs/getting-started).

The graded MVP has only two user-facing pages:

1. **Search** - search movies and TV shows, choose a result, and view details.
2. **Explorer** - filter movies or TV shows by genre and release year, then
   analyze the returned ratings and popularity with pandas and charts.

## Course Requirements

| Requirement | ScreenScope implementation |
| --- | --- |
| Python web app | Python modules and two Streamlit pages |
| Data analysis | pandas analysis and Plotly charts over filtered TMDB results |
| API | TMDB search, details, genre, and discover endpoints |
| Hosted on Streamlit | Deploy `app.py` with Streamlit Community Cloud |
| Hosted on GitHub | Shared repository with commits and pull requests |
| Team access | All six members and the instructor added as collaborators |

## Deliberately Small MVP

### Tab 1: Search

- One search box using TMDB `/search/multi`
- Keep movie and TV results; ignore people
- Result cards with poster, title, media type, year, rating, and popularity
- A selected result displays its overview, genres, release date, rating, vote
  count, popularity, runtime, and status on the same page

### Tab 2: Explorer

- Choose `Movie` or `TV Show`
- Filter by one genre and one release/first-air year
- Use TMDB `/discover/movie` or `/discover/tv`, sorted by popularity
- Build one pandas DataFrame from the current result page
- Show summary metrics, a results table, and two charts:
  - top titles by popularity
  - rating versus popularity, with vote count available for context

The Explorer reports only on the current filtered TMDB result page. Labels
must say **"most popular in these results"**, not claim universal trending.

The MVP does **not** need TMDB account login, favorites, watchlists,
recommendations, machine learning, a database, episode analysis, or a second
API. The provided account-details documentation belongs to the same TMDB API,
but that endpoint is not required for this read-only app.

## Team Ownership

Each member should create a feature branch, make at least one meaningful
commit, and open one pull request. Confirm Debshree's GitHub username before
inviting collaborators.

| Owner | GitHub | Workstream | Primary files | Definition of done |
| --- | --- | --- | --- | --- |
| Aarya Deshpande | `AaryaDeshpande` | App shell, visual system, integration | `app.py`, `screenscope/styles.py`, shared docs | Two-page navigation and styling are consistent; merged app runs end to end |
| Xianyu Wang | `XYWang-sunset` | TMDB API, authentication, normalized data | `screenscope/api.py`, `screenscope/contracts.py`, `tests/test_api.py` | Search, details, genres, and discover helpers return the shared contract and handle failures |
| Debshree Chowdhury | **username needed** | Search form and result cards | `pages/1_Search.py`, `screenscope/search.py` | Query returns movie/TV cards and stores the selected media ID and type |
| Yan Liu | `Yanliu-dev` | Selected movie/TV detail panel | `screenscope/details.py`, `screenscope/detail_view.py` | Selected result displays safe, useful detail fields and missing-data fallbacks |
| Kuba | `kubar95` | pandas analysis and charts | `screenscope/analysis.py`, `tests/test_analysis.py` | Explorer results produce metrics, a table, and two clearly labeled charts |
| Snehal Jindal | `snehal-jindal` | Explorer filters, QA, deployment | `pages/2_Explorer.py`, `screenscope/explore.py`, `docs/DEPLOYMENT.md` | Genre/year filters work, the public app is deployed, and the QA checklist passes |

Assignments reduce merge conflicts; they are not walls. Teammates should
review one another's pull requests and coordinate before changing a shared
function signature.

## Shared Media Contract

Feature modules exchange normalized dictionaries or DataFrames using the
fields in `screenscope/contracts.py`:

```text
id, media_type, title, original_title, release_date, release_year,
genre_ids, genre_names, overview, poster_url, backdrop_url, rating,
vote_count, popularity, original_language
```

The detail response may also include:

```text
runtime, status, tagline, homepage
```

## Repository Structure

```text
.
|-- app.py                         # Shared Streamlit entry point
|-- pages/
|   |-- 1_Search.py                # Search, results, and selected details
|   `-- 2_Explorer.py              # Filters and data-analysis view
|-- screenscope/
|   |-- api.py                     # TMDB HTTP client and endpoints
|   |-- config.py                  # Local/Streamlit token loading
|   |-- contracts.py               # Shared normalized field names
|   |-- search.py                  # Search-card transformations
|   |-- details.py                 # Detail transformations
|   |-- detail_view.py             # Reusable Streamlit detail renderer
|   |-- analysis.py                # pandas analysis and chart data
|   |-- explore.py                 # Explorer query helpers
|   |-- state.py                   # Selected media state
|   `-- styles.py                  # Shared visual tokens and CSS
|-- tests/
|-- docs/
|-- requirements.txt
`-- CONTRIBUTING.md
```

## Local Setup

The course standard is Python 3.10.

```bash
git clone https://github.com/AaryaDeshpande/ScreenScope-TV-Explorer.git
cd ScreenScope-TV-Explorer
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

Add the TMDB **API Read Access Token** to your local
`.streamlit/secrets.toml`:

```toml
TMDB_ACCESS_TOKEN = "paste-your-read-access-token-here"
```

The real secrets file is ignored by Git. Add the same secret in Streamlit
Community Cloud when deploying. Never commit a token, API key, or session ID.

## Collaboration Workflow

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing. In short:

1. Pull the latest `main`.
2. Create your assigned feature branch from `main`.
3. Work mainly in your assigned files.
4. Run the app and tests.
5. Commit with a descriptive message and push your branch.
6. Open a pull request to `main` and request a teammate review.
7. Merge only after the app starts and there are no unresolved conflicts.

## Design Direction

The source of truth is [docs/DESIGN.md](docs/DESIGN.md). Use the dark
ScreenScope concept: compact navigation, prominent search, responsive poster
cards, restrained blue actions, warm rating accents, and readable charts. All
runtime titles, posters, and metrics must come from TMDB rather than hard-coded
prototype examples.

## Submission Checklist

- [ ] All six students are GitHub collaborators.
- [ ] Instructor `babbages` is invited to the repository.
- [ ] Every member has at least one meaningful commit and pull request.
- [ ] Live TMDB search and discover data appear in the app.
- [ ] pandas-based analysis and two charts are visible.
- [ ] App is deployed publicly with Streamlit.
- [ ] TMDB is visibly credited with the required notice.
- [ ] Empty results, missing posters, missing ratings, and API failures are handled.
- [ ] No secrets are committed.
- [ ] `pytest` passes and the final demo is recorded.

## TMDB Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

ScreenScope must include an About/Credits area with an approved TMDB logo and a
link to [The Movie Database](https://www.themoviedb.org/). TMDB branding must
remain less prominent than the ScreenScope identity.
