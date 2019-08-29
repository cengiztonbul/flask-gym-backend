from .views import init_view
from .test_profile_view import test_profile_view, test_data_routes
from .trainer_controller import students_data, list_student_view


def init_views(app):
    init_view(app)

    test_profile_view(app)
    test_data_routes(app)

    list_student_view(app)
    students_data(app)
