# ScreenScope

ScreenScope is a collaborative Streamlit application for searching TV shows,
viewing show and cast details, and analyzing episode ratings with live data from
the [TVmaze REST API](https://www.tvmaze.com/api).

> **Scope note:** TVmaze is a television API. The graded MVP is therefore a
> **TV Show Explorer & Episode Analytics** app. Movie support is a future
> extension and is not part of the required submission.

## Course Requirements

| Requirement | ScreenScope implementation |
| --- | --- |
| Python web app | Python modules and Streamlit pages |
| Data analysis | pandas analysis of episodes, seasons, genres, and ratings |
| API | Live TVmaze search, show, episode, cast, and catalog endpoints |
| Hosted on Streamlit | Deploy `app.py` with Streamlit Community Cloud |
| Hosted on GitHub | This shared repository and pull-request history |
| Team access | All six members and the instructor added as collaborators |

## MVP User Flow

1. Search for a television show by title.
2. Select the correct result from the returned show cards.
3. Open the selected show's details, including image, summary, genres, language,
   status, premiere date, rating, network or streaming service, and cast.
4. Analyze episode ratings by season with a table and charts.
5. Optionally explore a small catalog sample by genre, language, status, year,
   and minimum rating.

The MVP does **not** require accounts, saved watchlists, a database, movie data,
machine learning, or a second API.

## Suggested Team Ownership

Confirm or swap these assignments in the group chat before feature work begins.
Each owner works primarily in the listed files, opens a feature branch, makes at
least one meaningful commit, and submits one pull request.

| Owner | Workstream | Primary files | Definition of done |
| --- | --- | --- | --- |
| Aarya Deshpande | App shell, visual system, integration | `app.py`, `screenscope/styles.py`, shared docs | Navigation and visual system are consistent; PRs integrate cleanly |
| Xianyu Wang | TVmaze API and normalized data | `screenscope/api.py`, `screenscope/contracts.py`, `tests/test_api.py` | API functions return the shared field contract and handle failures |
| Debshree Chowdhury | Search and result selection | `pages/1_Search.py`, `screenscope/search.py` | Search returns useful cards and stores the selected TVmaze show ID |
| Yan Liu | Show details and cast | `pages/2_Show_Details.py`, `screenscope/details.py` | Selected show displays required metadata and cast safely |
| Kuba | Episode data analysis | `pages/3_Episode_Analysis.py`, `screenscope/analysis.py`, `tests/test_analysis.py` | pandas summary and at least two meaningful charts work |
| Snehal Jindal | Catalog exploration, QA, and deployment | `pages/4_Explore.py`, `screenscope/explore.py`, `docs/DEPLOYMENT.md` | Filters work on a bounded catalog sample; deployed app and demo are verified |

Assignments are organizational boundaries, not walls. Teammates should review
one another's pull requests and may pair when an interface changes.

## Shared Data Contract

Feature modules should exchange normalized dictionaries or DataFrames using the
fields in `screenscope/contracts.py` rather than depending on every nested API
field. The core show fields are:

```text
id, name, genres, language, status, premiered, ended, rating,
summary, image_url, network_name, web_channel_name, official_site, tvmaze_url
```

The core episode fields are:

```text
id, name, season, number, airdate, runtime, rating, summary, image_url
```

## Repository Structure

```text
.
|-- app.py                         # Shared Streamlit entry point
|-- pages/
|   |-- 1_Search.py                # Search and select a show
|   |-- 2_Show_Details.py          # Metadata and cast
|   |-- 3_Episode_Analysis.py      # pandas analysis and charts
|   `-- 4_Explore.py               # Optional catalog filters
|-- screenscope/
|   |-- api.py                     # TVmaze HTTP client and endpoints
|   |-- contracts.py               # Shared normalized field names
|   |-- search.py                  # Search-page transformations
|   |-- details.py                 # Detail-page transformations
|   |-- analysis.py                # Episode DataFrames and summaries
|   |-- explore.py                 # Catalog filtering
|   |-- state.py                   # Shared Streamlit selection state
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
streamlit run app.py
```

TVmaze's public API does not require an API key. Do not add unrelated keys or
secrets to the repository.

## Collaboration Workflow

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing. In short:

1. Pull the latest `main`.
2. Create one feature branch from `main`.
3. Work mainly in your assigned files.
4. Run the app and tests.
5. Commit with a descriptive message and push your branch.
6. Open a pull request to `main` and request a teammate review.
7. Merge only after the app still starts and the PR has no unresolved conflict.

## Design Direction

The source of truth is [docs/DESIGN.md](docs/DESIGN.md). The UI follows the
dark ScreenScope concept: compact header, prominent search, responsive show-card
grid, focused detail view, restrained blue actions, warm rating accents, and
clear analysis charts. The reference images are visual inspiration only; all
content must come from TVmaze rather than hard-coded TMDB examples.

## Submission Checklist

- [ ] Every team member is a GitHub collaborator.
- [ ] Instructor is invited to the repository.
- [ ] Every member has at least one meaningful commit and pull request.
- [ ] Live TVmaze API data appears in the app.
- [ ] pandas-based analysis and charts are visible.
- [ ] App is deployed publicly with Streamlit.
- [ ] TVmaze is visibly credited and linked.
- [ ] Empty results, missing images, missing ratings, and API failures are handled.
- [ ] `pytest` passes and the final two-minute demo is recorded.

## Data Attribution

ScreenScope uses data and images from [TVmaze](https://www.tvmaze.com/), whose
public API data is provided under CC BY-SA. TVmaze must remain visibly credited
in the deployed application.

