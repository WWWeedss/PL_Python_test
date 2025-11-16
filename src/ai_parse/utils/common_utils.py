def to_json_str(data: dict) -> str:
    """Convert a dictionary to a JSON string."""
    import json
    return json.dumps(data, ensure_ascii=False)
