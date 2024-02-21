from flask import Flask
from .routes import routes_list

def create_app():
    app = Flask(__name__)

    routes_list(app)

    @app.route('/')
    def test():
        return 'test'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port='5000')