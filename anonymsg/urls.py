from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="anonymsg"),
    path("list-message", views.MyAnonymousView.as_view(), name="anonymous-page"),
    path("edit-message", views.edit_message, name="edit-message"),
    path(
        "list-message/<str:name>",
        views.OtherAnonymousView.as_view(),
        name="anonymous-page-other",
    ),
    path("ask-page/<str:name>", views.AskView.as_view(), name="ask-page"),
    path("flutter/", views.flutter_home, name="flutter/anonymsg"),
    path("flutter/list-message/<str:name>", views.flutter_list_message, name="flutter/anonymous-page"),
    path("flutter/edit-message/", views.flutter_edit_message, name="flutter/edit-message"),
    path(
        "flutter/list-message/<str:name>/",
        views.flutter_anonymous_page_other,
        name="flutter/anonymous-page-other",
    ),
    path("flutter/ask-page/<str:name>/", views.flutter_ask_view, name="flutter/ask-page"),
]
