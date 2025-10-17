import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

DIR_STATIC = "./static"
DIR_DOCS = "./docs"
DIR_CONTENT = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.endswith("/"):
        basepath += "/"

    print(f"Using base path: {basepath}")
    
    print("🧹 Deleting old public directory...")
    if os.path.exists(DIR_DOCS):
        shutil.rmtree(DIR_DOCS)

    print("📂 Copying static files to docs...")
    copy_files_recursive(DIR_STATIC, DIR_DOCS)

    print("📝 Generating HTML pages from markdown content...")
    generate_pages_recursive(DIR_CONTENT, TEMPLATE_PATH, DIR_DOCS, basepath)

    print("✅ Site generation complete! Your site is ready in 'docs/'.")


if __name__ == "__main__":
    main()
