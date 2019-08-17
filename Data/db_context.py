import mongoengine
from Data.User import User


def global_init():
    db_connection_string = \
        "mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority"
    return mongoengine.connect(host=db_connection_string, alias='default')

