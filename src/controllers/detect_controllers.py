from flask import Blueprint
from src.services.detect_service import detect as detect
from src.services.detect_service import predict

detect_bp = Blueprint(name='detect',import_name=__name__, url_prefix='/api/detect')

@detect_bp.route('/', methods=['POST'])
def detect_multi() -> str:
    result = detect(language='multi')
    return result

@detect_bp.route('/ko', methods=['POST'])
def detect_kor() -> str:
    result = detect(language='ko')
    return result

@detect_bp.route('/en', methods=['POST'])
def detect_en() -> str:
    result = detect(language='en')
    return result

@detect_bp.route('/eng', methods=['POST'])
def detect_eng():
    result = predict()
    return result