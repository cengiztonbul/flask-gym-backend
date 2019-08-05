from Data import UserDAL as uDAL


def add_user(user):
    # check user data
    uDAL.db_add_user(user)
    return 0
