import mongoengine

from app.models.user import User


def init_db():
    # TODO add that to .env
    db_connection_str = """mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority"""
    return mongoengine.connect(host=db_connection_str)


def db_add_user():
    User.commit()


def db_find_user_by_email(mail):
    user_object = User.objects(email=mail).get()
    return user_object


def db_find_workout_by_user_email():
    pass
