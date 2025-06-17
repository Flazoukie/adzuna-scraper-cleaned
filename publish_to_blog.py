import os
import shutil
import subprocess
import sys

DATABLOG_DIR = "data-blog"
SCRAPER_OUTPUT_DIR = os.path.join(DATABLOG_DIR, "results")  # This is where analysis results live
DATABLOG_RESULTS_DIR = SCRAPER_OUTPUT_DIR  # Keep it the same, unless you want to separate source/target

def copy_files():
    if not os.path.exists(SCRAPER_OUTPUT_DIR):
        print(f"⚠️ Source folder '{SCRAPER_OUTPUT_DIR}' does not exist. Exiting.")
        sys.exit(0)

    files = os.listdir(SCRAPER_OUTPUT_DIR)
    if not files:
        print(f"⚠️ No files found in '{SCRAPER_OUTPUT_DIR}'. Exiting.")
        sys.exit(0)

    print(f"📂 Files in {SCRAPER_OUTPUT_DIR} before staging for commit:")
    print(files)

def git_commit_push(github_token):
    os.chdir(DATABLOG_DIR)
    print(f"📍 Current directory for git commands: {os.getcwd()}")

    subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions@github.com"], check=True)

    remote_url = f"https://x-access-token:{github_token}@github.com/Flazoukie/data-blog.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

    subprocess.run("git add results/*", shell=True, check=True)

    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if result.returncode != 0:
        subprocess.run(["git", "commit", "-m", "Update blog results with latest analysis"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("🚀 Changes pushed to data-blog repo.")
    else:
        print("✅ No changes detected in r
