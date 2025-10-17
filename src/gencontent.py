import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f" * Generating page: {from_path} -> {dest_path}")

    with open(from_path, "r", encoding="utf-8") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r", encoding="utf-8") as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title.strip())
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as to_file:
        to_file.write(template)


def extract_title(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 title found in markdown.")


def generate_pages_recursive(source_dir_path, template_path, dest_dir_path):
    """
    Recursively converts all .md files in source_dir_path into .html files
    inside dest_dir_path, preserving relative folder structure.
    """
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(from_path):
            # Recurse into subdirectories
            generate_pages_recursive(from_path, template_path, dest_path)

        elif os.path.isfile(from_path) and from_path.endswith(".md"):
            # Convert .md to .html while keeping folder structure
            dest_html_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(from_path, template_path, dest_html_path)
