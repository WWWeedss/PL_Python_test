import os

from src.ai_parse.ai_api.post_ocr_nlp import nlp_cleanup
from src.ai_parse.get_file import get_file
from src.ai_parse.parsers.file_parser import parse_file
from src.ai_parse.utils.common_utils import to_json_str


def parse_document(path: str, options: dict, apikey: str) -> str:
    result_dict = {
        "content":"",
        "metadata":{},
        "errorInformation":None
    }

    try:
        use_ai_correction = options.get("use_ai_correction", False)

        # 下载文件
        file_bytes, file_type = get_file(path)

        # 解析文件内容
        file_dict = parse_file(file_bytes, file_type)

        # 如果开启 AI 清洗
        if use_ai_correction:
            file_dict["content"] = nlp_cleanup(file_dict["content"], apikey)

        result_dict["metadata"] = file_dict["metadata"]
        result_dict["content"] = file_dict["content"]
    except Exception as e:
        result_dict["errorInformation"] = str(e)

    return to_json_str(result_dict)


if __name__ == "__main__":
    test_path = "https://plpython.oss-cn-beijing.aliyuncs.com/test.pdf"
    options = {
        "use_ai_correction": True
    }
    apikey = os.getenv("ZHIPUAI_API_KEY")
    result = parse_document(test_path, options, apikey)
    print(result)

    options = {
        "use_ai_correction": False
    }
    result = parse_document(test_path, options, apikey)
    print(result)