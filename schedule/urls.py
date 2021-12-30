from django.urls import path
from .views import schedule, delete_activity, flutter_activity_list
# from schedule import views as schedule

urlpatterns = [
    path('', schedule, name='schedule'),
    path('delete/', delete_activity, name='delete'),
    path('flutter/activity-list/<str:name>', flutter_activity_list, name='flutter/schedule')
]