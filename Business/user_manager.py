from passlib.hash import pbkdf2_sha256

from Data import UserDAL as uDAL
from Data.user import User


def add_user(user):
    # check user data
    uDAL.db_add_user(user)
    return 0


def add_user(first_name, last_name, email, password, confirm_password):
    if first_name is None or first_name == "":
        raise Exception("First name cannot be null.")

    if last_name is None or last_name == "":
        raise Exception("Last name cannot be null.")

    if email is None or email == "":
        raise Exception("not a valid email")

    if password != confirm_password:
        raise Exception("Passwords don't match")

    pwd_hash = pbkdf2_sha256.hash(password)
    u = User(first_name=first_name, last_name=last_name, email=email, password_hash=pwd_hash)
    try:
        u.save()

    except Exception as e:
        raise e  # Exception("Unknown error has occurred.")


def login(email, pwd):
    res = uDAL.db_find_user_by_email(email)
    # user_hash = res.get("password_hash")
    user_hash = res.password_hash
    is_valid_pass = pbkdf2_sha256.verify(pwd, user_hash)
    return str(is_valid_pass)
