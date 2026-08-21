# Deployment and Release Checklist

Owner: Explorer, QA, and deployment workstream.

## Streamlit Community Cloud

1. Confirm `main` starts locally with `streamlit run app.py`.
2. Confirm `requirements.txt` contains every imported third-party package.
3. Sign in to Streamlit Community Cloud with the repository owner.
4. Create an app from this repository, branch `main`, file `app.py`.
5. In the app's advanced settings, add this secret:

   ```toml
   TMDB_ACCESS_TOKEN = "the-team-read-access-token"
   ```

6. Never place the token in code, screenshots, logs, issues, or the README.
7. Save the public Streamlit URL in the README.

## Required GitHub Access

- Add `Yanliu-dev`, `kubar95`, `XYWang-sunset`, and `snehal-jindal` as
  collaborators.
- Ask Debshree for her GitHub username and add it.
- Invite instructor `babbages`.
- Confirm each student has a merged, meaningful pull request.

## QA Matrix

- Missing local/deployed token
- Empty search
- Typo or no matching title
- Movie and TV results with the same name
- Person results excluded from multi search
- Missing poster, overview, date, or rating
- Movie details and TV details
- Genre/year combination with no discover results
- API timeout, 401, 404, and server error
- Charts with missing ratings or very low vote counts
- Mobile-width layout
- Fresh private/incognito browser session

## Final Demo

Keep the recording under the course limit. A suggested two-minute flow is in
`docs/DEMO_SCRIPT.md`.
