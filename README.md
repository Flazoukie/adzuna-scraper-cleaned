# Adzuna Scraper & Analysis Automation

This repository automates weekly scraping, analysis, and publishing of data science job market insights in Germany.

## Workflows Overview

### 1. Scrape Job Data (`scrape.yml`)
- Runs every Monday at 07:00 UTC (08:00 CET) automatically.
- Scrapes job offers data from the Adzuna API.
- Commits the raw job data CSV files to this repo.

### 2. Analyze Scraped Data (`analyze.yml`)
- Triggered automatically after scraping completes.
- Runs a Jupyter notebook that analyzes job data and generates:
  - Top cities bar plot (`top_cities.png`)
  - Interactive company map (`company_map.html`)
  - Interactive job table (`interactive_job_table.html`)
- Saves results in a dated folder inside this repo.
- Pushes these results to the `data-blog` repository under `results/YYYY-MM-DD/`.

### 3. Publish Weekly Blog Post (`publish.yml`)
- Triggered automatically after analysis completes (or run manually).
- Clones the `data-blog` repository.
- Auto-generates a `.qmd` Quarto blog post in `data-blog/posts/` embedding the latest results.
- Commits and pushes the new post to the `data-blog` repo, ready for rendering.

---

## Manual Runs

All workflows can be runned automatically from the GitHub Actions UI:
- Go to the **Actions** tab
- Select the workflow (Scrape, Analyze, or Publish)
- Click **Run workflow**

---

## Secrets Required

We use the following secrets which are set in this repository's Settings > Secrets:

- `ADZUNA_APP_ID` — Adzuna API app ID
- `ADZUNA_APP_KEY` — Adzuna API key
- `BLOG_REPO_TOKEN` — a personal access token with push permissions to the `data-blog` repository

---

## Notes

- The `data-blog` repository hosts my Quarto blog and serves the published posts.
- All results and blog posts are organized by date for easy tracking.

---

Feel free to contact me if you have any questions!
