

def init_views(app):
    from .views import init_view
    init_view(app)

    from .auth_views import init_auth_views
    init_auth_views(app)

    from .test_profile_view import test_profile_view, test_data_routes
    test_profile_view(app)
    test_data_routes(app)

    from .trainer_controller import students_data, list_student_view
    list_student_view(app)
    students_data(app)

    from app.views.admin_controller import init_admin_routes
    init_admin_routes(app)
