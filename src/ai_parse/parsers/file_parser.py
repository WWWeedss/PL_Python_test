from src.ai_parse.parsers.pdf_parser import parse_pdf


def parse_file(file_bytes: bytes, filetype: str) -> dict:
    result = {
        "content" : "",
        "metadata" : {}
    }
    if filetype == "pdf":
        full_text, page_count = parse_pdf(file_bytes)
        result["content"] = full_text
        result["metadata"]["page_count"] = page_count
    else:
        raise Exception("Unsupported file type")

    return result
