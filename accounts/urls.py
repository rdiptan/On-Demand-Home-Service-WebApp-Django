from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('registerCustomer/', views.registerCustomer.as_view(), name='register_customer'),
    path('registerServicemen/', views.registerServicemen.as_view(), name='register_servicemen'),
    path('customerProfile/', views.customerAccount, name="customer_profile"),
    path('servicemenProfile/', views.servicemenAccount, name="servicemen_profile"),
    path('password-change', auth_views.PasswordChangeView.as_view(template_name='accounts/passwordChange.html'), name="password_change"),
    path('password-change-done', auth_views.PasswordChangeView.as_view(template_name='accounts/passwordChangeDone.html'), name="password_change_done"),
]