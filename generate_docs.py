import os
import ast

def extract_docstrings_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    docstrings = []

    # Module-level docstring
    module_docstring = ast.get_docstring(tree)
    if module_docstring:
        docstrings.append(f"# Module: `{file_path}`\n\n{module_docstring}\n")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            name = node.name
            doc = ast.get_docstring(node)
            if doc:
                kind = "Function" if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) else "Class"
                docstrings.append(f"## {kind}: `{name}`\n\n{doc}\n")

    return "\n".join(docstrings)

def scan_project(directory):
    output = []
    for root, dirs, files in os.walk(directory):
        # Skip virtualenvs and hidden directories
        if any(part.startswith('.') or part in ('myenv', '__pycache__') for part in root.split(os.sep)):
            continue

        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, directory)
                doc = extract_docstrings_from_file(full_path)
                if doc:
                    output.append(doc)

    return "\n\n---\n\n".join(output)

if __name__ == "__main__":
    print("Generating documentation...")

    output = scan_project(".")
    with open("documentation_output.md", "w", encoding='utf-8') as f:
        f.write("# Project Documentation\n\n")
        f.write(output)

    print("Documentation written to documentation_output.md")
