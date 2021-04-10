from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name="admin_dashboard"),
    path('register-user', views.register_user_admin, name="register_user"),
    path('show-user', views.get_user, name="show_user"),
    path('update-user-to-admin/<int:user_id', views.update_user_to_admin, name="user_to_admin"),
    path('create-service', views.AdminServiceCreateView.as_view(), name="create_service"),
    path('view-service', views.AdminServiceListView.as_view(), name="view_service"),
    
    path('updateservice/<int:service_id>/', views.update_service, name="updateservice"),
    path('deleteservice/<int:service_id>/', views.delete_service, name="deleteservice"),

]