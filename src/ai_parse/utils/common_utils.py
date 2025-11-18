def to_json_str(data: dict) -> str:
    """Convert a dictionary to a JSON string."""
    import json
    return json.dumps(data, ensure_ascii=False)

def str_to_dict(json_str: str) -> dict:
    """Convert a JSON string to a dictionary."""
    import json
    return json.loads(json_str)

def get_file_extension(url: str) -> str:
    """Extract file extension from a URL, ignoring query and fragment."""
    from urllib.parse import urlparse
    import os

    # Parse the URL and extract the path component
    parsed = urlparse(url)
    path = parsed.path  # e.g., '/documents/report.pdf'

    # Extract extension from the path
    _, ext = os.path.splitext(path)
    return ext[1:].lower()  # Remove leading dot and lowercase

if __name__ == "__main__":
    print(get_file_extension("https://plpython.oss-cn-beijing.aliyuncs.com/test.pdf"))