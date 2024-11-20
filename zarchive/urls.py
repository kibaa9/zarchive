from django.contrib import admin
from django.urls import path, include
from zarchive import common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zarchive.common.urls')),
]
