from ..models.user import User
from app import login

DEFAULT_PASSWORD = "123456"


def create_user(first_name, last_name, email, role_id):
    user = User()

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.role_id = role_id
    user.password_hash = DEFAULT_PASSWORD  # password_hash.hash_pwd(DEFAULT_PASSWORD)

    user.save()
    return user


def find_user_by_email(email):
    return User.objects(email=email).get()


def delete_user_by_id(user_id):
    User.objects(user_id=user_id).get().delete()


@login.user_loader
def load_user(email):
    return User.objects(email=email).get()
