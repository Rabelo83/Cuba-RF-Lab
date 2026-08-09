# Site Admin

<span class="status-badge status-concept">GitHub Pages setup</span>

This repository includes a MkDocs site and a GitHub Actions workflow for validating the website build.

Expected public URL:

```text
https://rabelo83.github.io/ETECSA-RF-Lab/
```

## How The Site Publishes Now

The repository is currently using branch-based GitHub Pages from `main`.

To make that deployment match the local MkDocs preview, the generated MkDocs static output is committed at the repository root:

```text
index.html
assets/
search/
architecture/
sops/
...
```

The `.nojekyll` file tells GitHub Pages to serve these files as plain static output.

The workflow at `.github/workflows/pages.yml` validates the MkDocs build on pushes to `main`, but it does not deploy.

## Repository Settings Needed

For the current branch-based setup:

1. Go to Settings.
2. Open Pages.
3. Under Build and deployment, use Deploy from a branch.
4. Select branch `main`.
5. Select folder `/root`.
6. Save.

For a public project site, the repository should be public or otherwise on a GitHub plan that allows Pages for the repository visibility.

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

## Updating The Public Static Output

After editing `docs/`, rebuild and copy the MkDocs output to the repository root:

```bash
mkdocs build --strict
cp -R site/. .
```

Then commit both the source documentation changes and the generated static output.
