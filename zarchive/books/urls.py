from django.urls import path, include
from zarchive.books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_catalogue_page'),
    path('top/', views.BookTopListView.as_view(), name='book_top_catalogue_page'),
    path('available/', views.BookAvailableListView.as_view(), name='book_available_catalogue_page'),
    path('create/', views.BookCreateView.as_view(), name='book_create_page'),
    path('book/<int:pk>/', include([
        path('', views.BookDetailView.as_view(), name='book_detail_page'),
        path('edit/', views.BookEditView.as_view(), name='book_edit_page'),
        path('delete/', views.BookDeleteView.as_view(), name='book_delete_page'),
    ]))
]
