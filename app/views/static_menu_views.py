from flask import render_template


def static_views(app):
    @app.route('/packages')
    def packages():
        return render_template('/packages.html')

    @app.route('/contact')
    def contact():
        return render_template('/contact.html')
