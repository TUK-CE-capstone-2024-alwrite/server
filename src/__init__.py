from flask import Flask
from .routes import routes_list
from .database import database as db

def create_app():
  app = Flask(__name__)
  
  routes_list(app)
  
  @app.route('/')
  def test():
    return 'hello world!'
  
  return app
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')