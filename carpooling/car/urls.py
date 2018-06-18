from django.conf.urls import url, include
from rest_framework import routers
from django.urls import  path
from car import views
from .views import UserRudView, UserAPIView, UserLoginApiView, UserLoginCheckAPIView, UserView

urlpatterns = [
    url(r'^users/$', UserAPIView.as_view(), name='user-create'),
    url(r'^users/(?P<user_pk>\d+)/$', UserRudView.as_view(), name='user-rud'),
    url(r'^login/$', UserLoginApiView.as_view(), name='login'),
    url(r'^login/check/$', UserLoginCheckAPIView.as_view(), name='login-check'),    
    url(r'^register/$', UserView.as_view(), name='register'),
    url(r'^users/detail/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
