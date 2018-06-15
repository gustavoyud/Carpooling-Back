from django.conf.urls import url, include
from rest_framework import routers
from .views import scheduleAPIView,scheduleRudView, scheduleCreateAPIView

urlpatterns = [
    url(r'^schedule/get/$', scheduleAPIView.as_view(), name='schedule-get'),
    url(r'^schedule/post/$', scheduleCreateAPIView.as_view(), name='schedule-post'),
    url(r'^schedule/(?P<schedule_pk>\d+)/$', scheduleRudView.as_view(), name='schedule-rud'),
]
