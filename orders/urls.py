
from django.urls import path
from .views import *

urlpatterns = [
    path('cart',show_cart,name="cart"),
    path('add_to_cart',add_cart_item,name="add_to_cart"),
    path('remove_from_cart/<pk>',remove_from_cart,name="remove_from_cart"),
    path('confirm_order',confirm_order,name="confirm_order"),
    path('orders',show_orders,name="orders")
]
