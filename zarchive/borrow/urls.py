from django.urls import path

from zarchive.borrow import views

urlpatterns = [
    path('', views.BorrowBookView.as_view(), name='borrow_book_page'),
    path('return/', views.ReturnBookView.as_view(), name='return_book_page'),
]
