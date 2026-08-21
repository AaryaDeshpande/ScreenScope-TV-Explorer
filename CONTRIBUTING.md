# Contributing to ScreenScope

This project is designed for six contributors to work in parallel without
overwriting one another.

## Before You Start

```bash
git switch main
git pull origin main
git switch -c feature/short-description
```

Suggested branches:

```text
feature/app-shell
feature/tmdb-api
feature/search-results
feature/media-details
feature/explorer-analysis
feature/explorer-deploy
```

Do not run `git init` after cloning. Do not commit directly to `main`.

## While You Work

- Stay primarily within the files assigned to your workstream.
- Import shared API and contract helpers instead of copying request code.
- Treat missing posters, dates, overviews, and ratings as normal API data.
- Keep API calls cached and use only the returned page of results.
- Do not describe filtered results as globally "trending."
- Do not commit `.DS_Store`, virtual environments, credentials, or generated data.
- Never print or log the TMDB token.
- Ask in the group chat before changing another workstream's public function.

## Before Opening a Pull Request

```bash
python -m pytest
streamlit run app.py
git status
git add -- path/to/your_file.py
git commit -m "Add concise description of feature"
git push -u origin feature/short-description
```

Open a pull request into `main`. Use the repository template to explain what
changed, how it was tested, and which screenshots demonstrate the feature.

Each pull request should provide one coherent improvement. Avoid combining
unrelated formatting or refactors with feature work.

## Review and Integration

- At least one teammate should open and run the branch before merge.
- The app must start without exceptions.
- Existing pages and tests must continue to work.
- Resolve merge conflicts on the feature branch, not directly on `main`.
- Delete the remote feature branch after a successful merge.
