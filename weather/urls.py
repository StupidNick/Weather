from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User





urlpatterns = [
    url(r'^', include('weatherManager.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('weather/', include('weatherManager.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
