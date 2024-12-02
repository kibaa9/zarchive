from django.urls import path, include
from zarchive.genres import views

urlpatterns = [
    path('', views.GenreListView.as_view(), name='genre_catalogue_page'),
    path('create/', views.GenreCreateView.as_view(), name='genre_create_page'),
    path('genre/<int:pk>/', include([
        path('books/', views.BookByGenreListView.as_view(), name='books_by_genre_page'),
        path('edit/', views.GenreEditView.as_view(), name='genre_edit_page'),
        path('delete/', views.GenreDeleteView.as_view(), name='genre_delete_page'),
    ]))
]
