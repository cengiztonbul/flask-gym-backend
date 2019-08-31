from ..models.user import User
from passlib.hash import bcrypt_sha256
DEFAULT_PASSWORD = "123456"


def create_user(first_name, last_name, email, role="user"):
    user = User()

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.role = role
    user.password_hash = bcrypt_sha256.hash(DEFAULT_PASSWORD)

    user.save()
    return user


def find_user_by_email(email):
    return User.objects(email=email).first()


def delete_user_by_id(user_id):
    User.objects(user_id=user_id).first.delete()

