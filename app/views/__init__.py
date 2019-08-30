

def init_views(app):
    from .views import init_view
    init_view(app)

    from .auth_views import init_auth_views
    init_auth_views(app)

    from app.views.admin_controller import admin_routes, admin_data_routes
    admin_routes(app)
    admin_data_routes(app)
