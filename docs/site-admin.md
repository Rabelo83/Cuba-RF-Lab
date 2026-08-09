# Site Admin

<span class="status-badge status-concept">GitHub Pages setup</span>

This repository includes a GitHub Actions workflow for publishing the website.

Expected public URL:

```text
https://rabelo83.github.io/ETECSA-RF-Lab/
```

## How The Site Publishes

The workflow at `.github/workflows/pages.yml`:

1. runs on pushes to `main`
2. installs documentation dependencies from `requirements-docs.txt`
3. builds the MkDocs site with `mkdocs build --strict`
4. uploads the generated `site/` folder
5. deploys the artifact to GitHub Pages

## Repository Settings Needed

If the first deployment does not appear, check GitHub repository settings:

1. Go to Settings.
2. Open Pages.
3. Under Build and deployment, set Source to GitHub Actions.
4. Make sure Actions are enabled for the repository.

For a public project site, the repository should be public or otherwise on a GitHub plan that allows Pages for the repository visibility.

## If The Workflow Fails At Configure GitHub Pages

This usually means Pages has not been enabled for the repository yet.

Fix:

1. Open repository Settings.
2. Open Pages.
3. Set Source to GitHub Actions.
4. Save.
5. Go to Actions.
6. Open Deploy GitHub Pages.
7. Run the workflow manually, or push a new normal commit to `main`.

## Local Preview

Install docs dependencies, then run:

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000/
```
