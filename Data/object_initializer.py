from umongo import Instance

from Data import TTDbContext as Context

# ---------- Documents ----------
from Data.User import Users
from Data.workout import Workout
# -------------------------------

instance = Instance(Context.get_db().test_database)

instance.register(Workout)
instance.register(Users)
