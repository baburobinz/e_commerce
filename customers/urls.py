
from django.urls import path
from .views import *

urlpatterns = [
    path('account',show_account,name="account"),
    path('login',user_login,name='user_login'),
    path('registration',user_register,name='user_register'),
    path('logout',sign_out,name='sign_out'),
   
   
]
