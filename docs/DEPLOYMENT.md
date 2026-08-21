# Deployment and Release Checklist

Owner: QA and deployment workstream.

## Streamlit Community Cloud

1. Confirm `main` starts locally with `streamlit run app.py`.
2. Confirm `requirements.txt` contains every imported third-party package.
3. Sign in to Streamlit Community Cloud with the GitHub repository owner.
4. Create an app from this repository, branch `main`, file `app.py`.
5. TVmaze requires no API secret, so the deployment should not need credentials.
6. Save the public Streamlit URL in the README.

## Required GitHub Access

- Add all six students under repository collaborator access.
- Invite the instructor using the GitHub username specified by the course.
- Confirm each student has a merged, meaningful pull request.

## QA Matrix

- Empty search
- Typo or no matching show
- Duplicate show names
- Missing poster
- Missing summary
- Missing show rating
- Show with no episodes or no episode ratings
- API timeout, HTTP error, and rate-limit response
- Mobile-width layout
- Fresh private/incognito browser session

## Final Demo

Keep the recording under the course limit. A suggested two-minute flow is in
`docs/DEMO_SCRIPT.md`.

