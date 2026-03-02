import sys
import tarfile
import os
import shutil

repo_dir = os.environ["GITHUB_WORKSPACE"]
docs_dir = os.path.join(repo_dir, "docs")

# 清空舊 docs
if os.path.exists(docs_dir):
    shutil.rmtree(docs_dir)

os.makedirs(docs_dir, exist_ok=True)

tar_path = sys.argv[1]

with tarfile.open(tar_path, "r") as tar:
    for member in tar.getmembers():
        if member.isdir():
            continue

        # 只取檔名，不保留上層資料夾
        member.name = os.path.basename(member.name)
        tar.extract(member, docs_dir)

print("Extracted clean site into docs/")