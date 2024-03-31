from flask import Flask
from flask_cors import CORS
from src.routes import routes_list

def create_app():
    app = Flask(__name__)
    CORS(app)

    routes_list(app)

    @app.route('/')
    def test():
        return 'dev test'

    return app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)