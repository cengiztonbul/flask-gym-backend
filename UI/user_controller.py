from sanic.response import file
from Business import user_manager as um
from Data.User import Users
from sanic.response import text


def add_users_get(request):
    return file('./add_user.htm')


def add_user_post(request):
    user = Users()
    user.fname = request.form.get('fname')
    user.lname = request.form.get('lname')
    um.add_user(user)
    return text("Success")


def add_routes(app):
    app.add_route(add_user_post, "/users/add", methods=['POST'])
    app.add_route(add_users_get, "/users/add", methods=['GET'])
