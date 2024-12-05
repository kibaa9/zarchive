from django.urls import path

from zarchive.publishers import views

urlpatterns = [
    path('', views.PublisherListView, name='publisher_list_view'),
    path('<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_details_view'),
]