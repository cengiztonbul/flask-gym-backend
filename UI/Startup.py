from sanic import Sanic
import UI.user_controller as uc


app = Sanic('some_name')
uc.add_routes(app)
app.run(host="127.0.0.1", port=8000, debug=True)
