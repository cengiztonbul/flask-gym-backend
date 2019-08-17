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

    u = User(first_name=first_name, last_name=last_name, email=email, password=password)

    try:
        u.save()

    except:
        raise Exception("Unknown error has occurred.")
