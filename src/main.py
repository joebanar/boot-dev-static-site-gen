import os
import shutil
from generate_page import generate_page  # Make sure this file exists and has your generate_page() function

def copy_recursive(src, dst):
    """
    Recursively copies the contents of the src directory into dst.
    Deletes all existing contents of dst before copying.
    """
    # Remove destination directory if it exists
    if os.path.exists(dst):
        print(f"Deleting existing directory: {dst}")
        shutil.rmtree(dst)

    # Recreate the destination directory
    os.mkdir(dst)
    print(f"Created directory: {dst}")

    # Iterate through all items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} → {dst_path}")
        elif os.path.isdir(src_path):
            copy_recursive(src_path, dst_path)
        else:
            print(f"Skipped unknown item: {src_path}")

def main():
    src_dir = "static"
    dst_dir = "public"

    # 1. Clean and copy static files
    print("Copying static files...")
    copy_recursive(src_dir, dst_dir)

    # 2. Generate main HTML page
    content_path = "content/index.md"
    template_path = "template.html"
    dest_path = os.path.join(dst_dir, "index.html")

    print(f"\nGenerating HTML page from '{content_path}' → '{dest_path}' using '{template_path}'")
    generate_page(content_path, template_path, dest_path)

    print("\n✅ Site generation complete!")

if __name__ == "__main__":
    main()
