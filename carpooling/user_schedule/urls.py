from django.conf.urls import url, include
from rest_framework import routers
from .views import userScheduleAPIView, userScheduleCreateAPIView, userScheduleRudView, isScheduledCheck

urlpatterns = [
    url(r'^user-schedule/get/$', userScheduleAPIView.as_view(), name='user-schedule-get'),
    url(r'^user-schedule/post/$', userScheduleCreateAPIView.as_view(), name='user-schedule-post'),
    url(r'^user-schedule/(?P<user_schedule_pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', userScheduleRudView.as_view(), name='user-schedule-rud'),
    url(r'^user-schedule/get/check/$', isScheduledCheck.as_view(), name='check'),
]
