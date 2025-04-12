import os

def generate_documentation(directory):
    # Start with an empty docstring content
    docstring_content = ""

    # Walk through the directory to get Python files
    for filename in os.listdir(directory):
        if filename.endswith(".py"):  # Only process Python files
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            docstring = None
            in_docstring = False
            for line in lines:
                # Check for docstring start and end
                if '"""' in line:
                    if not in_docstring:
                        in_docstring = True
                        docstring = ""
                    else:
                        in_docstring = False
                        docstring_content += f"#### Docstrings:\n\n{docstring}\n\n"
                elif in_docstring:
                    docstring += line.strip()

    # Write the docstring content to a documentation file
    with open("documentation_output.md", "w") as doc_file:
        doc_file.write(docstring_content)

    # Add the testing comment to README
    readme_file = "README.md"
    if os.path.exists(readme_file):
        with open(readme_file, "a") as file:
            file.write("\n<!-- testing testing 123 auto doc is working -->\n")
            print(f"Temporary comment added to {readme_file}")
    else:
        print("README.md not found!")


# Call the function to generate documentation
generate_documentation(".")
