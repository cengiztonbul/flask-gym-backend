import pymongo


def init_db():
    client = pymongo.MongoClient(
        "mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority")
    print("Connected to DB")
    return client


db_connection_string = pymongo.MongoClient(
        "mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority")


def get_db():
    global db_connection_string
    return db_connection_string
