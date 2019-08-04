import pymongo


def init_db():
    client = pymongo.MongoClient(
        "mongodb+srv://furkana:E8aHuJOUvtrrIBeb@cluster0-e1ggm.mongodb.net/test?retryWrites=true&w=majority")
    print("Connected to DB")
    return client


def db_add_user(db, name, surname, mail, weight, height, age):
    user = {"name": name,
            "surname": surname,
            "mail": mail,
            "weight": weight,
            "height": height,
            "age": age,
            "workouts": {},
            "dietplans": {}
            }
    db.insert_one(user)


def update_user_mail(db, user_mail, update_key, update_value):
    db.update_one({"mail": user_mail},
                  {"$set": {update_key: update_value}})


# def insert_user_workout(db, user_mail, insert_key, insert_value):
#     db.update_one({"mail": user_mail},
#                   {"$set": {insert_key: insert_value}})


db = init_db().test_database
users_db = db.users
db_add_user(users_db, "Fu", "ar", "f@gmail.com", 70, 170, 20)
