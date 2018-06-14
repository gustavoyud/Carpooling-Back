from django.conf.urls import url, include
from rest_framework import routers
from cars import views
from .views import carAPIView, carRudView, UserDetail

urlpatterns = [
    url(r'^cars/$', carAPIView.as_view(), name='car-create'),
    url(r'^cars/(?P<car_pk>\d+)/$', carRudView.as_view(), name='car-rud'),
    url(r'^users/detail/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
