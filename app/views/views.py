def init_view(app):
    @app.route('/', methods=['GET'])
    def index():
        return {"test": "test"}

