from flask import render_template

def init_view(app):
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/users/<int:user_id>')
    def user_profile(user_id):
        return render_template('index.html')
