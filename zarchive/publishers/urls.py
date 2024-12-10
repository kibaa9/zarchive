from django.urls import path, include
from zarchive.publishers import views

urlpatterns = [
    path('', views.PublisherListView.as_view(), name='publisher_list_page'),
    path('create/', views.PublisherCreateView.as_view(), name='publisher_create_page'),
    path('book/<int:pk>/', include([
        path('', views.PublisherDetailView.as_view(), name='publisher_detail_page'),
        path('edit/', views.PublisherEditView.as_view(), name='publisher_edit_page'),
        path('delete/', views.PublisherDeleteView.as_view(), name='publisher_delete_page'),
    ]))
]
