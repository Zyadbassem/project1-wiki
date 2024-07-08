from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('search/', views.search, name="search"),
    path('random/', views.randomWiki, name="random"),
    path('edit/<str:wikiTitle>/', views.edit, name="edit"),
    path('<str:wiki>/', views.wiki, name="wiki"),
  #  path('favicon.ico/', views.favicon, name='favicon'),
]