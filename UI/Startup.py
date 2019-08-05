from sanic import Sanic
import UI.user_controller as uc


app = Sanic('some_name')
uc.add_routes(app)
app.run(host="0.0.0.0", port=8000, debug=True)
