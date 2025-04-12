import ast
from pathlib import Path

def extract_docstrings_from_file(file_path):
    """Extracts all module, class, and function docstrings from a Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            node = ast.parse(f.read(), filename=str(file_path))
    except Exception as e:
        return [f"⚠️ Error parsing {file_path}: {e}"]

    docstrings = []

    # Module-level docstring
    if ast.get_docstring(node):
        docstrings.append(ast.get_docstring(node))

    # Function, Class, and AsyncFunction docstrings
    for child in ast.walk(node):
        if isinstance(child, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(child)
            if doc:
                docstrings.append(doc)
    return docstrings

def scan_directory(directory):
    """Recursively scans a directory for Python files and extracts docstrings."""
    docs = []
    for path in Path(directory).rglob("*.py"):
        if any(part in path.parts for part in ['venv', 'env', 'myenv', '__pycache__']):
            continue
        relative_path = path.relative_to(directory)
        docs.append(f"### {relative_path}\n\n#### Docstrings:\n")
        for doc in extract_docstrings_from_file(path):
            docs.append(f'"""\n{doc}\n"""\n')
    return "\n".join(docs)

def write_to_markdown(output_file, content):
    """Writes content to a markdown file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    documentation = scan_directory(".")
    write_to_markdown("documentation_output.md", documentation)
    print("✅ Documentation written to documentation_output.md")
