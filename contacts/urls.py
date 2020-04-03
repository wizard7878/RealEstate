from django.urls import path,include
from contacts.views import *



urlpatterns = [
   path('contact/',contact,name='contact')
]