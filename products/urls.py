from django.urls import path
from .views import *

urlpatterns=[

    path('',index,name="index"),
    path('products_list',list_products,name="product_list"),
    path('detail_product/<pk>',detail_product,name="detail_product")
]


