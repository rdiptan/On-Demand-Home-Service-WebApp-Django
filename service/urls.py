from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name="service"),
    path('addservice', views.add_service, name="addservice"),
    path('postservice', views.post_service, name="postservice"),
    path('getservice', views.get_service, name="getservice"),
    path('updateservice/<int:service_id>/', views.update_service, name="updateservice"),
    path('deleteservice/<int:service_id>/', views.delete_service, name="deleteservice"),

]