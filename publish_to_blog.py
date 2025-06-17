import os
import shutil
import subprocess

# Paths — adjust if needed
SCRAPER_OUTPUT_DIR = "output"  # relative to where this script runs (adzuna scraper repo)
DATABLOG_DIR = r"C:\Users\flavi\PycharmProjects\DataBlog"
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
    subprocess.run(["git", "add", "results/*"], check=True)
    commit_message = "Update blog results with latest analysis"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Changes pushed to data-blog repo.")

if __name__ == "__main__":
    copy_files()
    git_commit_push()
