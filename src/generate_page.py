import os

def extract_title(markdown: str) -> str:
    """
    Extracts the first H1 header (a line starting with '# ') from the markdown text.
    Returns the header text (without '#').

    Raises:
        Exception: If no H1 header is found.
    """
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):  # Only match H1 (single '#')
            return line[2:].strip()
    raise Exception("No H1 header found in markdown.")

def generate_page(from_path, template_path, dest_path):
    from markdown_blocks import markdown_to_html_node

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title from markdown
    title = extract_title(markdown_content)

    # Replace placeholders in template
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)