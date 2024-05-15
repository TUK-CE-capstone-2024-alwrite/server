from .easyocr import *
import os
from flask import jsonify
# GPU 설정
#os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

#변환할 이미지 가져오기
def get_files(path):
    file_list = []

    files = [f for f in os.listdir(path) if not f.startswith('.')]  # skip hidden file
    files.sort()
    abspath = os.path.abspath(path)
    for file in files:
        file_path = os.path.join(abspath, file)
        file_list.append(file_path)

    return file_list, len(file_list)

#이미지 텍스트 변환
def detect_easyocr(language): # # Using default model
    # reader = Reader(['ko'], gpu=True)

    # Using custom model
    # 이미지에서 텍스트를 추출하기 위해 reader 객체 생성
    if language == 'multi':
        reader = Reader(['ko', 'en'], gpu=False,
                    model_storage_directory='src/EasyOCR/model',
                    user_network_directory='src/EasyOCR/user_network_dir',
                    recog_network='custom')
    elif language == 'ko':
        reader = Reader(['ko','en'], gpu=False,
                    model_storage_directory='src/EasyOCR/model_kor',
                    user_network_directory='src/EasyOCR/user_network_dir',
                    recog_network='custom')
    elif language == 'en':
        reader = Reader(['ko','en'], gpu=False,
                    model_storage_directory='src/EasyOCR/model_en',
                    user_network_directory='src/EasyOCR/user_network_dir',
                    recog_network='custom')

    files, count = get_files('src/EasyOCR/demo_images')
    result_set = []

    #reader에서 텍스트 / bbox / confidence 추출
    for idx, file in enumerate(files):
        filename = os.path.basename(file)

        result = reader.readtext(file)
        # print(jsonify({"result": result}))
         # 이미지에서 감지된 각 단어에 대해 문자열로 변환
        words = []  # 단어들을 저장할 리스트
        for (bbox, string, confidence) in result:
            words.append(string)

        # 감지된 단어들을 하나의 문장으로 합치고 결과에 추가
        sentence = ' '.join(words)
        result_set.append({
            'filename': filename,
            'string': sentence
        })


    return result_set