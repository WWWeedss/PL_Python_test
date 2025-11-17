from src.ai_parse.utils.common_utils import get_file_extension
import requests

def get_file(path: str) -> tuple[bytes, str]:
    # 目前仅支持 http 格式的 url
    file_type = get_file_extension(path)
    try:
        response = requests.get(path)
        response.raise_for_status()
        file_bytes = response.content
    except Exception as e:
        raise Exception(f"Failed to download file from {path}: {e}")

    return file_bytes, file_type

if __name__ == "__main__":
    url = "https://plpython.oss-cn-beijing.aliyuncs.com/test.pdf"
    file_bytes, file_type = get_file(url)
    print(f"Downloaded file type: {file_type}, size: {len(file_bytes)} bytes")