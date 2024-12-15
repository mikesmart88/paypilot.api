
from django.urls import path, include
from . import views

# create yr app urls here

urlpatterns = [
   
    path('', views.home, name="home page"),
]