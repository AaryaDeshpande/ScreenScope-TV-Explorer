# ScreenScope

ScreenScope is a small Streamlit app for finding movies and TV shows with live
data from [TMDB](https://developer.themoviedb.org/docs/getting-started).

The app has two simple pages:

1. **Search:** Search by title, select a result, and see its details.
2. **Explorer:** Choose Movie or TV, a genre, and a year; then see a table,
   summary numbers, and two charts.

That is the entire required product. We are not building accounts, watchlists,
recommendations, machine learning, a database, or a second API.

## What It Should Look Like

These are the current starting screens. Keep the same simple flow while filling
in the live results and charts.

| Home | Search | Explorer |
| --- | --- | --- |
| <img src="docs/reference/screenscope-home.png" alt="ScreenScope home" width="320"> | <img src="docs/reference/screenscope-search.png" alt="ScreenScope Search" width="320"> | <img src="docs/reference/screenscope-explorer.png" alt="ScreenScope Explorer" width="320"> |

## Your Assignment

Each person owns one small part. Search the listed files for your name and
`TODO`. Keep the existing function names so everyone else's code connects.

| Person | Branch | Work only in | Fill in |
| --- | --- | --- | --- |
| **Xianyu** | `feature/tmdb-api` | `screenscope/api.py` | `search_media()`, `get_media_details()`, `get_genres()`, and `discover_media()` |
| **Debshree** | `feature/search-results` | `pages/1_Search.py`, `screenscope/search.py` | Call `search_media()`, show result cards, and call `select_media()` when one is selected |
| **Yan** | `feature/media-details` | `screenscope/details.py`, `screenscope/detail_view.py` | Prepare safe detail values and display the selected title below Search |
| **Kuba** | `feature/explorer-analysis` | `screenscope/analysis.py` | Calculate three summary values and prepare data for two Matplotlib charts |
| **Snehal** | `feature/explorer-deploy` | `pages/2_Explorer.py`, `screenscope/explore.py`, `docs/DEPLOYMENT.md` | Connect Movie/TV, genre, and year filters; display Kuba's results; deploy the app |
| **Aarya** | `feature/app-integration` | `app.py`, `screenscope/styles.py`, shared docs | Merge the pieces, keep the three screens consistent, test the full app, and record the demo |

Each assignment should be one focused pull request. The matching details are
also in [GitHub Issues](https://github.com/AaryaDeshpande/ScreenScope-TV-Explorer/issues).

### When Your Part Is Done

- **Xianyu:** The four API functions return dictionaries using the fields in
  `screenscope/contracts.py`.
- **Debshree:** Searching `Friends` displays selectable movie/TV results.
- **Yan:** Selecting a movie or show displays its poster and basic information.
- **Kuba:** Given result data, the summary and two chart datasets are produced.
- **Snehal:** Explorer filters produce a table, summary, and two charts; the
  Streamlit link opens publicly.
- **Aarya:** Both pages work together, tests pass, attribution is visible, and
  every teammate has a merged pull request.

## Build Order

1. **Xianyu** connects the API.
2. **Debshree and Yan** complete Search and Details.
3. **Kuba and Snehal** complete Explorer and Analysis.
4. **Aarya** integrates, tests, and prepares the final demo.

Steps 2 and 3 can happen in parallel. While waiting for the API, use a small
sample dictionary with the field names in `screenscope/contracts.py`.

## Set Up Once

The course standard is Python 3.10.

```bash
git clone https://github.com/AaryaDeshpande/ScreenScope-TV-Explorer.git
cd ScreenScope-TV-Explorer
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Put your own TMDB **API Read Access Token** in
`.streamlit/secrets.toml`:

```toml
TMDB_ACCESS_TOKEN = "paste-your-token-here"
```

Never commit or paste a real token into GitHub.

Run the app:

```bash
streamlit run app.py
```

## Complete Your Part

```bash
git switch main
git pull origin main
git switch -c your-branch-name

# Fill in the TODO comments in your assigned files.

pytest
git add path/to/your_file.py
git commit -m "Add your feature"
git push -u origin your-branch-name
```

Then open a pull request into `main` and ask one teammate to review it.

## Keep It Simple

- Work mainly in your assigned files.
- Do not rename shared functions or fields without telling the group.
- Do not add extra pages or features before the required flow works.
- Handle missing titles, posters, dates, and ratings without crashing.
- Explorer describes only the current returned results. Say **"most popular in
  these results"**, not "globally trending."

## Final Checklist

- [ ] Search calls the TMDB API and displays movie/TV results.
- [ ] Selecting a result displays its details.
- [ ] Explorer filters by media type, genre, and year.
- [ ] pandas creates the analysis table and summary.
- [ ] Matplotlib displays two charts.
- [ ] The app is deployed with Streamlit.
- [ ] All six teammates and instructor `babbages` have repository access.
- [ ] Every teammate has a meaningful commit and pull request.
- [ ] No API token is committed.
- [ ] `pytest` passes.

## TMDB Credit

This product uses the TMDB API but is not endorsed or certified by TMDB.

The deployed app must also link to [The Movie Database](https://www.themoviedb.org/)
and display an approved TMDB logo.
