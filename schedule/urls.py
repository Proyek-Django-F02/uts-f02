from django.urls import path
from .views import schedule, delete_activity, flutter_activity_list, flutter_add_activity, flutter_delete_activity
# from schedule import views as schedule

urlpatterns = [
    path('', schedule, name='schedule'),
    path('delete/', delete_activity, name='delete'),

    path('flutter/activity-list/<str:name>', flutter_activity_list, name='flutter-schedule'),
    path('flutter/add/', flutter_add_activity, name='flutter-add'),
    path('flutter/delete', flutter_delete_activity, name='flutter-delete')
]