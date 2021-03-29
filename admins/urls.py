from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name="admin_dashboard"),
    path('register-user', views.register_user_admin, name="register_user"),
    path('show-user', views.get_user, name="show_user"),
    path('update-user-to-admin/<int:user_id', views.update_user_to_admin, name="user_to_admin")
]