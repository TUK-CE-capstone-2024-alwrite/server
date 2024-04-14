import os
import requests
from openai import OpenAI
import json

def load_api_key_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data.get("OPENAI_API_KEY")
    except Exception as e:
        print("api_key 인증 오류", str(e))
        return {"error": "api_key 인증 오류",'isSuccess' : 0}

def summarize_text(text):
    try:        
        json_file_path = "src/secret_info/authentication/openai_key.json"

        # 환경 변수 대신 JSON 파일에서 API 키를 읽어옵니다.
        api_key = load_api_key_from_json(json_file_path)

        # API 키가 유효한지 확인합니다.
        if not api_key:
            print("API key 유효하지 않음.")
            exit()

        # OpenAI 클라이언트를 초기화합니다.
        client = OpenAI(api_key=api_key)
                
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
            return {'summary_text' : summary_text, 'isSuccess' : 1}
        else:
            return {"error": "response안에서 choice불가능.", 'isSuccess' : 0}

    except Exception as e:
        error_message = {"error": str(e),'isSuccess' : 0}
        print(e)
        return error_message


