from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')

students = []


@app.route("/x/<data>", methods=['POST'])
def x(request, data):
    students.append(data)
    return text(data)

@app.route("/x")
def y(request):
    s = ""
    for a in students:
        s += a + '\n'
    return text(a)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)