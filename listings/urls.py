from django.urls import path,include
from listings.views import *



urlpatterns = [
    path('',index,name='listings'),
    path('search/',search,name='search'),
    path('<int:list_id>',listing,name='listing')
]