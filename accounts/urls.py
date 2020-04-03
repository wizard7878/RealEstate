from django.urls import path,include
from accounts.views import *



urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register,name='register')
]