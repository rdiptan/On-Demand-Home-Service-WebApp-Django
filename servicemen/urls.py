from django.urls import path
from . import views

urlpatterns = [
    path('servicemen-order/', views.ServicemenOrderListView.as_view(), name="servicemen_order"),
    path('servicemen-order-detail/<int:pk>/', views.ServicemenOrderDetailView.as_view(), name="servicemen_order_detail"),
    path('servicemen-order-status/<int:pk>/', views.ServicemenOrderStatuChangeView.as_view(), name="servicemen_orderstatus_change"),
]