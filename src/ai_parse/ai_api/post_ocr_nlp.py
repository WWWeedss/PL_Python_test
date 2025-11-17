from src.ai_parse.ai_api.ai_wrapped import get_response_from_ai

def nlp_cleanup(text: str) -> str:
    return get_response_from_ai("请对以下文本进行语法和拼写纠正，并提升其可读性：\n"
                                "注意仅输出纠正后的源格式文本内容\n"
                                "不要使用 Markdown 格式输出\n"
                                "文本如下:"
                                "\n\n" + text)


if __name__ == "__main__":
    sample_text = "Ths is a smple txt with sme erors. It neds to be corected."
    cleaned_text = nlp_cleanup(sample_text)
    print("Original Text:", sample_text)
    print("Cleaned Text:", cleaned_text)