import pymongo
from Data import TTDbContext as Context


db = Context.get_db().test_database
users_db = db.users


def db_add_user(user):
    global users_db
    user.commit()
