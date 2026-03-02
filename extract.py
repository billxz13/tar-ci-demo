import sys
import tarfile
import os

repo_dir = os.environ["GITHUB_WORKSPACE"]
target_dir = os.path.join(repo_dir, "docs")

os.makedirs(target_dir, exist_ok=True)

tar_path = sys.argv[1]

with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path=target_dir)

print("Extracted to docs/")