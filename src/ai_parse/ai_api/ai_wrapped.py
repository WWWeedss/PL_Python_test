import os

from zai import ZhipuAiClient

def get_response_from_ai(prompt: str, apikey: str) -> str:
    client = ZhipuAiClient(api_key=apikey)
    response = client.chat.completions.create(
        model="glm-4.5-flash",
        messages=[
            {"role": "user", "content": prompt}
        ],
        thinking={
            "type": "disabled",
        },
        stream=False,
        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = "请用中文简短介绍一下人工智能的发展历史。"
    apikey = os.getenv("ZHIPUAI_API_KEY")
    response = get_response_from_ai(prompt, apikey)
    print("AI Response:", response)