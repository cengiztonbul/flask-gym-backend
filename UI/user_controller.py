from sanic.response import file
from sanic.response import text
from sanic import Sanic
from Business import user_manager


def add_users_get(request):
    return file('./fitnesszone-html/register.html')


def add_users_post(request):
    first_name = request.form.get('f_user')
    last_name = request.form.get('l_user')
    email = request.form.get('email')
    password = request.form.get('pwd')
    confirm_password = request.form.get('c_pwd')
    try:
        user_manager.add_user(first_name, last_name, email, password, confirm_password)
    except Exception as e:
        return text(str(e))

    return text("success")


def add_routes(app: Sanic):
    app.add_route(add_users_post, "/users/add", methods=['POST'])
    app.add_route(add_users_get, "/users/add", methods=['GET'])
