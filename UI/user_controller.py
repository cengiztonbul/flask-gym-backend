from sanic.response import file
from sanic.response import text
from sanic import Sanic


def add_users_get(request):
    return file('./add_user.htm')


def add_users_post(request):
    return text("Not implemented yet")


def add_routes(app: Sanic):
    app.add_route(add_users_post, "/users/add", methods=['POST'])
    app.add_route(add_users_get, "/users/add", methods=['GET'])
