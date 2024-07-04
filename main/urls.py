from django.urls import path
from . import views


urlpatterns = [
    path('', views.helloWorld, name="main"),
    path('rooms/', views.rooms, name="rooms")
]