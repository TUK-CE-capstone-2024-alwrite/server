from werkzeug.utils import secure_filename
from flask import jsonify, request
import requests
import json
import os
import time
import shutil

# vito.ai 서버에 인증 토큰 요청
def getTokens(config) -> str:
    try:
        resp = requests.post(
            'https://openapi.vito.ai/v1/authenticate',
            data={'client_id': config.get('CLIENT_ID'),
            'client_secret': config.get('CLIENT_SECRET')}
        )
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return {'error': 'api 인증 정보 오류', 'isSuccess' : 0}
    
    # 토큰 반환
    return resp.json().get('access_token')

# vito.ai 서버에 STT 요청
def requestSTT(token,file) -> str:
    try:
        config = {}
        folder = 'src/speach_file/'
        empty_folder(folder)
        
        # 파일 저장
        file.save(folder + secure_filename(file.filename))
        
        file_from_dir = get_files(folder)
        resp = requests.post(
            'https://openapi.vito.ai/v1/transcribe',
            headers={'Authorization': 'bearer '+token},
            data={'config': json.dumps(config)},
            files={'file': open(file_from_dir, 'rb')}
        )
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return {'error': '토큰 인증 오류', 'isSuccess' : 0}
    
    # id 값 반환
    return resp.json().get('id')

# 변환된 텍스트 결과 요청
def getResult(token, resId) -> str:
    try:
        resp = requests.get(
            'https://openapi.vito.ai/v1/transcribe/'+resId,
            headers={'Authorization': 'bearer '+token},
        )
        
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return {'error': '텍스트 변환 오류', 'isSuccess' : 0}

    # 텍스트 변환 결과 반환
    return resp

# 폴더 비우기 함수
def empty_folder(folder: str) -> None:
    # 저장 폴더 비우기
    # 실패시 애러 메시지 반환.
    for filename in os.listdir(folder):
        if filename != '.gitkeep':
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
                return {'error': '이미지 인식 오류', 'isSuccess' : 0}

#변환할 파일 가져오기
def get_files(path) -> str:
    #  숨김 파일을 제외한 녹음 파일 하나만 가져오기 
    files = [f for f in os.listdir(path) if not f.startswith('.')]
    files.sort()
    abspath = os.path.abspath(path)
    for file in files:
        file_path = os.path.join(abspath, file)
    print(file_path)
    
    return file_path

# vito.ai 서버에 STT 요청 함수
def check_status_and_get_result(token, resId):
    result = getResult(token, resId)
    status = result.json().get('status')
    
    if status == 'failed':
        return {'error': '텍스트 변환 오류', 'isSuccess': 0}
    elif status == 'transcribing':
        # 재귀적으로 호출하여 status가 success가 될 때까지 기다림
        time.sleep(5)  # 5초간 대기 후 재요청 5초 정도 걸린다고 함
        return check_status_and_get_result(token, resId)
    elif status == 'completed':
        return {'result': result.json().get('results'), 'isSuccess': 1}
    
# 결과값에서 텍스트만 추출하는 함수
def extract_text_from_result(result):
    utterances = result['result']['utterances']
    text = ' '.join(utterance['msg'] for utterance in utterances)
    return text

# 텍스트 변환 서비스 실행 함수
def speachToText() -> str:
    # 파일 수신
    # 실패시 애러 메시지 반환
    try:
        file = request.files['file']
    except Exception as e:
        print(e)
        return {'error': '파일 수신 실패','isSuccess' : 0}
    
    # 인증 파일 읽기
    try:
        with open('src/secret_info/authentication/vito_auth.json') as f:
            config = json.load(f)
    except FileNotFoundError as e:
        print(e)
        return {'error': '인증 정보 누락 오류', 'isSuccess' : 0}

    # vito.ai 서버에 인증 토큰 요청
    token = getTokens(config)
    
    # 저장된 음성 파일을 vito.ai 서버에 STT 요청
    # id 값 반환 - 결과를 받기 위한 id 값
    resId = requestSTT(token,file)
    
    # 변환된 텍스트 결과 요청
    result = check_status_and_get_result(token, resId)

    # result에서 텍스트만 추출하여 하나의 텍스트로 반환
    text = extract_text_from_result(result)
    
    return  {'result': text, 'isSuccess': 1}