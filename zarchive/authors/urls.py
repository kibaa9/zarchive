from django.urls import path, include
from zarchive.authors import views

urlpatterns = [
    path('', views.AuthorListView.as_view(), name='author_list_page'),
    path('create/', views.AuthorCreateView.as_view(), name='author_create_page'),
    path('book/<int:pk>/', include([
        path('', views.AuthorDetailView.as_view(), name='author_detail_page'),
        path('edit/', views.AuthorEditView.as_view(), name='author_edit_page'),
        path('delete/', views.AuthorDeleteView.as_view(), name='author_delete_page'),
    ]))
]
