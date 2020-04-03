from pages import views
from django.urls import path,include
urlpatterns = [
    path('about/',views.about,name='about')
]
