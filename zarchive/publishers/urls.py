from django.urls import path

from zarchive.publishers import views

urlpatterns = [
    path('', views.PublisherListView.as_view(), name='publisher_list_page'),
    path('<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail_page'),
]