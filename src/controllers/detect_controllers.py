import os
from flask import Blueprint, request
from flask import jsonify
from werkzeug.utils import secure_filename
from EasyOCR.run import detect_easyocr as easyocr
import json
import src.services.detect_service as detect_service

detect_bp = Blueprint(name='detect',import_name=__name__, url_prefix='/api/detect/')

@detect_bp.route('/', methods=['POST'])
def detect() -> str:
    
    # 파일 수신
    # 실패시 애러 메시지 반환
    try:
        file = request.files['file']
    except:
        return jsonify({'error': '파일 수신 실패'})
    
    # 저장 폴더 비우기
    # 실패시 애러 메시지 반환
    folder = 'EasyOCR/demo_images/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return jsonify({'error': 'Failed to delete %s. Reason: %s' % (file_path, e)})
    
    # 파일 저장
    file.save(folder + secure_filename(file.filename))
    
    # 수신 받은 파일 텍스트 변환
    result = easyocr()
    result = detect_service.detect_route(result)
    
    return jsonify(result)