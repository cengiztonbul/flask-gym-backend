from sanic import Sanic
from sanic.response import text
from sanic.response import file

from sanic.views import HTTPMethodView

app = Sanic('some_name')

students = []


@app.route("/users/add", methods=['POST'])
def x(request):
    students = request.body


@app.route("/users/add", methods=['GET'])
def add_users(request):
    return file('./index.htm')


@app.route("/users")
def y(request):
    return text(students[0])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)