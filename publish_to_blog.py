import os
import shutil
import subprocess
import sys

SCRAPER_OUTPUT_DIR = "output"
DATABLOG_DIR = "data-blog"
DATABLOG_RESULTS_DIR = os.path.join(DATABLOG_DIR, "results")

def copy_files():
    os.makedirs(DATABLOG_RESULTS_DIR, exist_ok=True)
    print(f"Files in {SCRAPER_OUTPUT_DIR} before copying:")
    files = os.listdir(SCRAPER_OUTPUT_DIR)
    print(files)
    for filename in files:
        src_path = os.path.join(SCRAPER_OUTPUT_DIR, filename)
        dst_path = os.path.join(DATABLOG_RESULTS_DIR, filename)
        print(f"Copying {src_path} to {dst_path}")
        shutil.copy2(src_path, dst_path)
    print(f"Files in {DATABLOG_RESULTS_DIR} after copying:")
    print(os.listdir(DATABLOG_RESULTS_DIR))

def git_commit_push(github_token):
    os.chdir(DATABLOG_DIR)
    print(f"Current directory for git commands: {os.getcwd()}")

    subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions@github.com"], check=True)

    remote_url = f"https://x-access-token:{github_token}@github.com/Flazoukie/data-blog.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

    subprocess.run(["git", "add", "results/*"], shell=True, check=True)
    
    # Commit only if there are changes
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if result.returncode != 0:
        subprocess.run(["git", "commit", "-m", "Update blog results with latest analysis"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to data-blog repo.")
    else:
        print("No changes detected in results folder. Nothing to commit.")

if __name__ == "__main__":
    token = os.getenv("BLOG_REPO_TOKEN")
    if not token:
        raise RuntimeError("GitHub token not provided in environment variable BLOG_REPO_TOKEN.")
    copy_files()
    git_commit_push(token)
