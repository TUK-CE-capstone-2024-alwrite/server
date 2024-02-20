# routes.py 또는 routes_list 함수
def routes_list(app, database):
    @app.route('/some_route')
    def some_route():
        return database.db.child('some_path').get().val()