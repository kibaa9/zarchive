from django.urls import path, include
from rest_framework.routers import DefaultRouter
from zarchive.books import views
from zarchive.books.views import BookViewSet, ApproveBookView, all_books_view

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_catalogue_page'),
    path('search/', views.SearchBooksView.as_view(), name='book_search_page'),
    path('top/', views.BookTopListView.as_view(), name='book_top_catalogue_page'),
    path('available/', views.BookAvailableListView.as_view(), name='book_available_catalogue_page'),
    path('borrowed/', views.BookBorrowListView.as_view(), name='book_borrowed_catalogue_page'),
    path('userlist/', views.UserListBooksView.as_view(), name='book_userlist_page'),
    path('overdue/', views.BookOverdueListView.as_view(), name='book_overdue_page'),
    path('create/', views.BookCreateView.as_view(), name='book_create_page'),
    path('approve_book/<int:pk>/', ApproveBookView.as_view(), name='approve_book_page'),
    path('api/', include(router.urls)),
    path('all-books/', all_books_view, name = 'all_books_page'),
    path('book/<int:pk>/', include([
        path('', views.BookDetailView.as_view(), name='book_detail_page'),
        path('edit/', views.BookEditView.as_view(), name='book_edit_page'),
        path('delete/', views.BookDeleteView.as_view(), name='book_delete_page'),
    ])),
]
