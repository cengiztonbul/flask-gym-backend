from app import create_app
from app.models.trainer import Trainer
from app.models.user import User
from app.services.database import init_db

init_db()


if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=8000, debug=True)
