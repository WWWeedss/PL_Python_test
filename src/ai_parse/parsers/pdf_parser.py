from io import BytesIO
from PyPDF2 import PdfReader


def parse_pdf(file_bytes: bytes) -> tuple[str, int]:
    reader = PdfReader(BytesIO(file_bytes))
    page_count = len(reader.pages)
    parts = []

    for idx, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            if text:
                parts.append(f"[Page {idx}]\n{text}")
            else:
                parts.append(f"[Page {idx}]\n")
        except Exception as e:
            print(f"Error extracting text from page {idx}: {e}")
    full_text = "\n\n".join(parts).strip()
    return full_text, page_count