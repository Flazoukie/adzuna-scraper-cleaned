import os
import shutil
import subprocess

# Paths inside GitHub Actions runner
SCRAPER_OUTPUT_DIR = "output"
DATABLOG_DIR = "data-blog"  # relative to root of the GitHub Actions workspace
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

def git_commit_push():
    os.chdir(DATABLOG_DIR)
    print(f"Current directory for git commands: {os.getcwd()}")

    # Set Git identity
    subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions@github.com"], check=True)

    # ⚠️ Overwrite the remote URL with authentication token
    github_token = os.environ["DATA_BLOG_TOKEN"]
    remote_url = f"https://x-access-token:{github_token}@github.com/Flazoukie/data-blog.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

    # Stage, commit, and push
    subprocess.run(["git", "add", "results/*"], check=True)
    subprocess.run(["git", "commit", "-m", "Update blog results with latest analysis"], check=True)
    subprocess.run(["git", "push"], check=True)

    print("Changes pushed to data-blog repo.")


if __name__ == "__main__":
    copy_files()
    git_commit_push()

