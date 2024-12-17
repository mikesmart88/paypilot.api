
from django.urls import path, include
from . import views

# create yr app urls here

app_name = 'paypilotapp'
urlpatterns = [
   
    path('', views.home, name="home page"),
    path('Products/', views.products, name='product pages'),
    path('Exchnage/', views.exchange, name='exchnage payments'),
    path('Spots/', views.spot, name="spots"),

    path('slot/binace/', views.binaceslot, name='binace collect slot'),
]
