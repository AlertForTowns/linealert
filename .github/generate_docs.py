import os
import inspect
import markdown

# Directory where the Python files are located
CODE_DIR = './'  # Adjust this path if needed
OUTPUT_FILE = 'generated_docs.md'

def extract_docstrings():
    """Extracts docstrings from all Python files in the directory."""
    docstrings = {}

    for root, dirs, files in os.walk(CODE_DIR):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                # Parse functions and classes and extract docstrings
                for name, obj in inspect.getmembers(inspect.getmodule(content)):
                    if inspect.isfunction(obj) or inspect.isclass(obj):
                        docstring = inspect.getdoc(obj)
                        if docstring:
                            docstrings[name] = docstring
    return docstrings

def generate_markdown(docstrings):
    """Generates markdown from extracted docstrings."""
    markdown_content = "# Generated Documentation\n\n"
    for name, docstring in docstrings.items():
        markdown_content += f"## {name}\n\n{docstring}\n\n"
    return markdown_content

def save_markdown(content):
    """Saves the generated markdown content to a file."""
    with open(OUTPUT_FILE, 'w') as f:
        f.write(content)

def main():
    """Main function to extract docstrings and generate documentation."""
    docstrings = extract_docstrings()
    if docstrings:
        markdown_content = generate_markdown(docstrings)
        save_markdown(markdown_content)
        print(f"Documentation generated and saved to {OUTPUT_FILE}")
    else:
        print("No docstrings found.")

if __name__ == '__main__':
    main()
