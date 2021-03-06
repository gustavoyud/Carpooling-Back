"""carpooling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^', include('car.urls')),
    url(r'^api/', include('cars.urls'), name='cars'),
    url(r'^api/places/', include('destiny.urls'), name='destiny'),
    url(r'^api/user/', include('schedule.urls'), name='schedule'),
    url(r'^schedule/', include('user_schedule.urls'), name='user-schedule'),    
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/$', obtain_jwt_token, name="api-login"),
]
