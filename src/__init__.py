from flask import Flask
from .routes import routes_list
from .database.database import Database

def create_app():
    app = Flask(__name__)
    database = Database()  # Database 클래스의 인스턴스 생성

    routes_list(app, database)  # routes_list 함수에 데이터베이스 인스턴스를 전달

    @app.route('/')
    def test():
        return database.db.child('test').get().val()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port='5000')