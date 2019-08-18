from Data.user import User


def db_add_user(user):
    user.commit()


def db_find_user_by_email(mail):
    user_object = User.objects(email=mail).get()
    return user_object
