import os
import requests
from openai import OpenAI

# 환경 변수에서 API 키를 읽어옵니다.
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트를 초기화합니다.
client = OpenAI(api_key=api_key)

def summarize_text(text):
    try:
        # API 호출 시에 API 키를 사용하여 인증합니다.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "주요 내용을 요약해줘. \n" + text}
            ]
        )
        
        # response 객체의 choices 속성을 사용하여 선택지를 가져옵니다.
        summary_text = response.choices[0].message.content
        
        # 선택지가 있는지 확인합니다.
        if summary_text:
            return summary_text
        else:
            return {"error": "No choices found in response"}

    except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message


