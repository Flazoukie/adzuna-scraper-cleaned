import os
import shutil
from datetime import date

# Paths
output_dir = "output"
blog_repo = "blog"
post_dir = f"{blog_repo}/posts/adzuna-weekly/{date.today().isoformat()}"

# Create destination folder in blog
os.makedirs(post_dir, exist_ok=True)

# Files to copy
files_to_copy = [
    "top_cities.png",
    "company_map.html",
    "interactive_job_table.html"
]

# Copy files from output/ to blog post folder
for filename in files_to_copy:
    src = os.path.join(output_dir, filename)
    dst = os.path.join(post_dir, filename)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {filename} to blog")
    else:
        print(f"File not found: {filename}")
