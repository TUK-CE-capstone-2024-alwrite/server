from .controllers.detect_controllers import detect_bp

# routes.py 또는 routes_list 함수
def routes_list(app):
    app.register_blueprint(detect_bp)
    return app