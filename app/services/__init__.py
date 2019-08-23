def init_services():

    from .database import init_db
    db_connection = init_db()
