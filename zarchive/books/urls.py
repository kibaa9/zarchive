from django.urls import path, include
from zarchive.books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_catalogue_page'),
    path('create/', views.BookCreateView.as_view(), name='book_create_page'),
    path('book/<int:pk>/', include([
        path('', views.BookDetailView.as_view(), name='book_detail_page'),
        path('edit/', views.BookUpdateView.as_view(), name='book_update_page'),
        path('delete/', views.BookDeleteView.as_view(), name='book_delete_page'),
    ]))
]
