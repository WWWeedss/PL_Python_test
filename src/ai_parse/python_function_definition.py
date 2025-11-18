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
        model = options.get("model", "glm-4.5-flash")

        # 下载文件
        file_bytes, file_type = get_file(path)

        # 解析文件内容
        file_dict = parse_file(file_bytes, file_type)

        # 如果开启 AI 清洗
        if use_ai_correction:
            file_dict["content"] = nlp_cleanup(file_dict["content"], apikey, model)

        result_dict["metadata"] = file_dict["metadata"]
        result_dict["content"] = file_dict["content"]
    except Exception as e:
        result_dict["errorInformation"] = str(e)

    return to_json_str(result_dict)


if __name__ == "__main__":
    test_path = "https://test-ai-parser.obs.cn-north-4.myhuaweicloud.com:443/shakespeare.pdf?AccessKeyId=HSTAMDX4VSDQ8L5P924N&Expires=1763514516&x-obs-security-token=hQpjbi1zb3V0aC0xAQAABDRIU1RBTURYNFZTRFE4TDVQOTI0TsO3bV8Wsihnf4SPqua7iJTecy1CxOj4-y1I6-FivGJ9kcQ8KjrwhprIEiz-5RZ_-IiyExmGtpJKQA2-Pah9n3ltkh0G8ymbyOaU4eciU9Fhqbrl-OPwwhaGXBGIN9Lo-XJRLKABq-AiJEV8xIvAHHX0myjgXBRaVQhvTFhqFd0RIVTZU6oVT_CAaPpysDULpPrggbYXTIu1wiSTDRCNo1HtqS_rP5C2f25GcWnLNsqQCmet1xrOTvoVIWrYe2oJKeFvJx5VsbHJ17pdS0bkuog7uSNzts1_hlaNUafre__rmq4ADPXRJmUnkC4xH-HA7iqnlpEj1E9wW-t854zmHwehgKeeN4iTGGlxP3NB33LMP232X4jmVqNGjoxaZw_xYQPEavXa3OT9SxWgt_JKlqm0CgbJUdOk8cEc4GdU3C4fW0lNBe_TsXMlDQFP4x1ckTKyrcZp4kzb2tYGDiGtm3nYv8SYZnFwKSeuGDIc4jh1uq0UeZw604-mNbEmFvMU4zUuKZbt2PClt8muMkl6F8C1XyUrlnm3YLMTSBUU5cHQUTLtUoaAlxA28xQVP68fmWJpzkwmWe6ydJsWINQV3p6yx-Y%3D&Signature=5d0qGsOwXEWf%2B2nGBVqsSL9u27Q%3D"
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