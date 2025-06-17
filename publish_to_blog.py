import os
import shutil
import subprocess

# Paths relative to where this script runs (in scraper repo)
SCRAPER_OUTPUT_DIR = "output"

# The data-blog repo will be cloned inside this workflow folder
DATABLOG_DIR = "data-blog"
DATABLOG_RESULTS_DIR = os.path.join(DATABLOG_DIR, "results")

def copy_files():
    os.makedirs(DATABLOG_RESULTS_DIR, exist_ok=True)
    for filename in os.listdir(SCRAPER_OUTPUT_DIR):
        src_path = os.path.join(SCRAPER_OUTPUT_DIR, filename)
        dst_path = os.path.join(DATABLOG_RESULTS_DIR, filename)
        print(f"Copying {src_path} to {dst_path}")
        shutil.copy2(src_path, dst_path)

def git_commit_push():
    os.chdir(DATABLOG_DIR)
    subprocess.run(["git", "add", "results"], check=True)
    commit_message = "Update blog results with latest analysis"
    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
    except subprocess.CalledProcessError:
        print("Nothing to commit.")
        return
    subprocess.run(["git", "push"], check=True)
    print("Changes pushed to data-blog repo.")

if __name__ == "__main__":
    copy_files()
    git_commit_push()
