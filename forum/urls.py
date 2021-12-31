from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', TopicListView.as_view(), name='forum-index'),
    path('topic/add/', TopicCreateView.as_view(), name='topic-add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('validate_topicname', validate_topicname, name='validate_topicname'),
    path('json/', topic_list_json, name='topic_list_json'),
    path('topic/<int:pk>/json/', topic_detail_json, name='topic_detail_json'),
    path('post/<int:pk>/json/', post_detail_json, name='post_detail_json'),
    path('flutter/add-topic/', add_topic, name='flutter_add_topic'),
    path('flutter/add-post/', add_post, name='flutter_add_post'),
    path('flutter/add-comment/', add_comment, name='flutter_add_comment'),
    path('flutter/update-post/', update_post, name='flutter_update_post'),
    path('flutter/delete-post/', delete_post, name='flutter_delete_post'),
]
