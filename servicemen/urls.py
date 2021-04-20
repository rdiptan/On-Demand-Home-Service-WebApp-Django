from django.urls import path
from . import views

urlpatterns = [
    path('', views.availability, name="availability"),
    path('servicemen-order/', views.ServicemenOrderListView, name="servicemen_order"),
    path('servicemen-order-detail/<int:pk>/', views.ServicemenOrderDetailView.as_view(), name="servicemen_order_detail"),
    path('servicemen-order-status/<int:pk>/', views.ServicemenOrderStatuChangeView.as_view(), name="servicemen_orderstatus_change"),
    path('servicemen-new-order/', views.ServicemenNewOrderListView.as_view(), name="servicemen_new_order"),

]