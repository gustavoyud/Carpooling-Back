from django.conf.urls import url, include
from rest_framework import routers
from .views import destinyAPIView, destinyRudView

urlpatterns = [
    url(r'^destiny/$', destinyAPIView.as_view(), name='destiny-create'),
    url(r'^destiny/(?P<destiny_pk>\d+)/$', destinyRudView.as_view(), name='destiny-rud'),
]
