from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, forms
from .forms import *

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('registerCustomer/', views.registerCustomer.as_view(), name='register_customer'),
    path('registerServicemen/', views.registerServicemen.as_view(), name='register_servicemen'),
    path('customerProfile/', views.customerAccount, name="customer_profile"),
    path('servicemenProfile/', views.servicemenAccount, name="servicemen_profile"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/passwordChange.html'), name="password_change"),
    path('password-change-done/', auth_views.PasswordChangeView.as_view(template_name='accounts/passwordChangeDone.html'), name="password_change_done"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', form_class=UserPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]