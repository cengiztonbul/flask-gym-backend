from werkzeug.utils import redirect

from app.models.user import User
from app.utils.forms import LoginForm


def login_manager(app):
    @app.route("/login", ['POST'])
    def login(request):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects(email=form.email.data).get()
        if user is None:
            return redirect("/login")

    @app.route("/login", ['GET'])
    def login(request):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects(email=form.email.data).get()

