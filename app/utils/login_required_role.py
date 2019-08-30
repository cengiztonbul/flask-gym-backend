from functools import wraps

from flask_login import current_user
from app import login


def login_required(role: list = "ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login.unauthorized()
            if (current_user.role not in role) and (role != "ANY"):
                return login.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper
