from django.urls import path
from .views import *

app_name = "note"

urlpatterns = [
    path("", index, name="index"),
    path('add_message/', add_message, name="add_message"),
    path('<str:id>/delete', delete_message, name="delete_message"),
    path("flutter/list-note/<str:name>", flutter_list_note, name="flutter/list-note"),
    path("flutter/detail-note/<str:name>/<str:id>", flutter_detail_note, name="flutter/edit-note"),
    path("flutter/delete-note/", flutter_delete_note, name="flutter/delete-note"),
    path("flutter/add-note/", flutter_add_note, name="flutter/add-note"),
    path("flutter/edit-note/", flutter_edit_note, name="flutter/edit-note"),
]
