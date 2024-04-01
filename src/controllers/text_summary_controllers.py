from flask import Blueprint, jsonify
from src.services.speachToText_service import speachToText as speachToText
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