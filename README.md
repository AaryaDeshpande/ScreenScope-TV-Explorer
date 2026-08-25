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

Each person owns one Python file. Open your file and complete only the numbered
`TODO` blocks bearing your name. The surrounding imports, function signatures,
and page flow are already provided.

| Person | Branch | Your Python file | Complete these functions |
| --- | --- | --- | --- |
| **Xianyu** | `feature/tmdb-api` | `screenscope/api.py` | `search_media()`, `get_media_details()`, `get_genres()`, `discover_media()` |
| **Debshree** | `feature/search-page` | `pages/1_Search.py` | `render_result_card()` |
| **Yan** | `feature/detail-panel` | `screenscope/detail_view.py` | `render_detail_panel()` |
| **Kuba** | `feature/explorer-page` | `pages/2_Explorer.py` | `load_genres()`, `load_results()`, `render_analysis()` |
| **Snehal** | `feature/charts-deploy` | `screenscope/charts.py` | `popularity_figure()`, `rating_popularity_figure()` |
| **Aarya** | `feature/data-analysis` | `screenscope/analysis.py` | `summarize_results()`, `chart_data()` |

Each person makes one focused pull request containing their assigned Python
file. Do not rename the prepared functions because other files already call
them.

### When Your Part Is Done

- **Xianyu:** The four API functions return normalized movie/TV dictionaries.
- **Debshree:** Search results show a poster, title, metadata, and Select button.
- **Yan:** A selected movie or show displays a readable detail panel.
- **Kuba:** Explorer filters load results and display metrics, a table, and charts.
- **Snehal:** Both Matplotlib functions return labeled figures. After all pull
  requests merge, deploy the app and record the short final demo.
- **Aarya:** pandas returns the three summary values and two clean chart datasets.

## Build Order

1. **Xianyu** completes the API functions.
2. **Debshree and Yan** complete Search and Details in parallel.
3. **Aarya and Snehal** complete analysis and charts in parallel.
4. **Kuba** connects the API, analysis, and charts on Explorer.
5. **Snehal** deploys and records the demo after all pull requests merge.

Everyone can start immediately because each function already has its inputs,
outputs, and numbered steps. Sample data can be used before the API is ready.

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

Run the optional command-line demo:

```bash
export TMDB_ACCESS_TOKEN="paste-your-read-access-token-here"
python cli_demo.py Dune
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
