import requests
import pandas as pd
import time
from datetime import date
import os

def fetch_adzuna_jobs(keyword="data science", country="de", pages=3, results_per_page=100,
                       app_id=None, app_key=None):
    all_jobs = []

    for page in range(1, pages + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
        params = {
            "app_id": app_id,
            "app_key": app_key,
            "what": keyword,
            "results_per_page": results_per_page,
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Failed on page {page}: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])
        print(f"Fetched {len(results)} jobs from page {page}")
        all_jobs.extend(results)

        time.sleep(1)

    return pd.DataFrame(all_jobs)


if __name__ == "__main__":
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")
    df = fetch_adzuna_jobs(app_id=app_id, app_key=app_key, pages=5)

    today = date.today().isoformat()
    out_dir = "data"
    os.makedirs(out_dir, exist_ok=True)
    df.to_csv(f"{out_dir}/jobs_{today}.csv", index=False)
