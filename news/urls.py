from django.urls import path
from . import views

urlpatterns = [
    path('', views.newshome, name='newshome'),
    path('newsreq/', views.newsrequest, name='newsrequest'),
    path('flutter/add-news', views.flutter_add_news, name='flutter-add-news'),
    path('flutter/get-news', views.flutter_get_news, name='flutter-get-news'),
]