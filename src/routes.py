from src.controllers.detect_controllers import detect_bp
from src.controllers.text_summary_controllers import text_summary_bp
# routes.py 또는 routes_list 함수
def routes_list(app):
    app.register_blueprint(text_summary_bp)
    app.register_blueprint(detect_bp)
    return app