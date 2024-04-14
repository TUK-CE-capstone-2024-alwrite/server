from flask import Blueprint, jsonify
from src.services.speachToText_service import speachToText as speachToText
from src.services.openai_summary_service import summarize_text
from openai import OpenAI
import json

text_summary_bp = Blueprint(name='stt', import_name=__name__, url_prefix='/api/stt')

@text_summary_bp.route('/', methods=['POST'])
def text_summary() -> str:
    # 음성 파일을 텍스트로 변환 요청
    # result는 json 형태임 - result = {'result': text, 'isSuccess': 1}
    # isSuccess가 0이면 변환 실패인 경우라 에러 메시지를 반환해줘야 함
    # isSuccess가 1일 경우에만 담겨있는 텍스트 값을 가지고 다음 단계로 넘어가야 함
    result = speachToText()
    
    # result가 실패인 경우에는 에러 메시지를 반환해줘야 함
    if result['isSuccess'] == 0:
        return jsonify(result)
    
    # 최종적으로 반환되는 결과는 summary 작업을 거친 텍스트만 반환해주도록 코드를 작성해야 함
    return jsonify(result)


@text_summary_bp.route('/summary', methods=['POST'])
def openai_summary():
    # text_summary 함수 호출하여 음성 파일을 텍스트로 변환한 결과 받아오기
    response = speachToText()
    
    # 텍스트 추출
    text = response['result']
    
    # OpenAI를 사용하여 텍스트 요약
    summary_text = summarize_text(text)
    
    # 변환 성공 여부 확인
    if response['isSuccess'] == 0:
        # 변환 실패 시 에러 메시지 반환
        return jsonify(response)
    
    # 요약 결과 반환
    return jsonify(summary_text)


