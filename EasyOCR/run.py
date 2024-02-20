from .easyocr import *
import os
# GPU 설정
#os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'


def get_files(path):
    file_list = []

    files = [f for f in os.listdir(path) if not f.startswith('.')]  # skip hidden file
    files.sort()
    abspath = os.path.abspath(path)
    for file in files:
        file_path = os.path.join(abspath, file)
        file_list.append(file_path)

    return file_list, len(file_list)


def detect(): # # Using default model
    # reader = Reader(['ko'], gpu=True)

    # Using custom model
    reader = Reader(['ko','en'], gpu=False,
                    model_storage_directory='EasyOCR/model',
                    user_network_directory='EasyOCR/user_network_dir',
                    recog_network='custom')

    files, count = get_files('EasyOCR/demo_images')
    result_set = []

    for idx, file in enumerate(files):
        filename = os.path.basename(file)

        result = reader.readtext(file)
    
        for (bbox, string, confidence) in result:
            print("filename: '%s', confidence: %.4f, string: '%s'" % (filename, confidence, string))
            result_set.append({
                'filename': filename,
                'confidence': float(confidence),  # Convert confidence to float
                'string': string,
            })

    return result_set
