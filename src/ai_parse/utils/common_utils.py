def to_json_str(data: dict) -> str:
    """Convert a dictionary to a JSON string."""
    import json
    return json.dumps(data, ensure_ascii=False)

def str_to_dict(json_str: str) -> dict:
    """Convert a JSON string to a dictionary."""
    import json
    return json.loads(json_str)

def get_file_extension(filename: str) -> str:
    """Get the file extension from a filename."""
    import os
    _, ext = os.path.splitext(filename)
    # Remove the leading dot and convert to lower case
    ext = ext[1:].lower()
    return ext

if __name__ == "__main__":
    print(get_file_extension("https://plpython.oss-cn-beijing.aliyuncs.com/test.pdf"))