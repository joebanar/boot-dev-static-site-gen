import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

DIR_STATIC = "./static"
DIR_PUBLIC = "./public"
DIR_CONTENT = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    print("🧹 Deleting old public directory...")
    if os.path.exists(DIR_PUBLIC):
        shutil.rmtree(DIR_PUBLIC)

    print("📂 Copying static files to public...")
    copy_files_recursive(DIR_STATIC, DIR_PUBLIC)

    print("📝 Generating HTML pages from markdown content...")
    generate_pages_recursive(DIR_CONTENT, TEMPLATE_PATH, DIR_PUBLIC)

    print("✅ Site generation complete! Your site is ready in 'public/'.")


if __name__ == "__main__":
    main()
