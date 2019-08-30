from flask import render_template
from flask_login import login_required


def init_admin_routes(app):
    @app.route('/admin_panel')
    def admin_panel():
        return render_template("/admin_panel.html")

    @app.route('/workout', methods=['GET'])
    def add_workout_get():
        return render_template("/create_workout.html")

    @app.route('/workout', methods=['POST'])
    def add_workout_post(request):
        pass  # request.form["id"]
