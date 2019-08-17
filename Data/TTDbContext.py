import mongoengine


def global_init():
    mongoengine.register_connection(db="mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority")
