from sanic import Sanic
from UI import user_controller
from Data import TTDbContext


app = Sanic('some_name')
user_controller.add_routes(app)
TTDbContext.global_init()

app.run(host="127.0.0.1", port=8000, debug=True)
