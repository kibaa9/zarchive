from django.urls import path
from zarchive.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
]
