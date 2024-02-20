from flask import Flask
from .routes import routes_list
from flask import Flask
from EasyOCR.run import detect as easyocr

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def test():
        result = easyocr()
        print(result)
        return result

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port='5000')