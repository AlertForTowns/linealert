# generate_docs.py

def generate_feature_docs():
    """
    Automatically generate documentation for the new features.
    """
    print("Generating documentation for new features...")

    # Data Processing Feature
    data_processing_feature = """
    ## Data Processing Feature

    **Function:** `process_data(data)`
    
    **Description:**
    This function processes the input list of numbers by squaring each item.

    **Example:**

    ```python
    data = [1, 2, 3, 4]
    print(process_data(data))  # Output: [1, 4, 9, 16]
    ```

    **Test Case:**
    - Input: `[1, 2, 3, 4]`
    - Expected Output: `[1, 4, 9, 16]`
    """

    with open("docs/data_processing_feature.md", "w") as f:
        f.write(data_processing_feature)
        print("Documentation for data processing feature generated at docs/data_processing_feature.md")
    
    # You can add more features here if needed. For now, it's just the `data_processing` feature.
    
# Call this function when needed in your workflow
generate_feature_docs()

