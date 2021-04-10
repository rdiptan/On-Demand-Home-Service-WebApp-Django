from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name="service"),
    path('viewservice/<slug:service_slug>/', views.view_service, name="serviceview"),
    
]