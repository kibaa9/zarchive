from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.utils.timezone import now
from django.views.generic import CreateView, UpdateView
from zarchive.books.models import Book
from zarchive.borrow.models import Borrow


class BorrowBookView(LoginRequiredMixin, CreateView):
    model = Borrow
    fields = []
    template_name = 'borrow/borrow_book_page.html'

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        if not book.is_available:
            messages.error(request, "This book is not available for borrowing.")
            return redirect('book_detail_page', pk=book.pk)

        return_date = now() + timedelta(days=14)

        Borrow.objects.create(
            borrower=request.user,
            book=book,
            borrow_date=now(),
            return_date=return_date,
        )

        book.is_available = False
        book.save()

        messages.success(request, "You have successfully borrowed the book.")
        return redirect('book_detail_page', pk=book.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(pk=self.kwargs['pk'])
        context['book'] = book
        return context


class ReturnBookView(LoginRequiredMixin, UpdateView):
    model = Borrow
    fields = []
    template_name = 'borrow/return_book_page.html'

    def get_object(self):
        return get_object_or_404(Borrow, pk=self.kwargs['pk'], borrower=self.request.user)

    def form_valid(self, form):
        borrow = self.get_object()

        if borrow.returned_at:
            messages.info(self.request, "This book has already been returned.")
            return redirect('book_detail_page', pk=borrow.book.pk)

        borrow.returned_at = timezone.now()
        borrow.is_returned = True
        borrow.save()

        borrow.book.is_available = True
        borrow.book.save()

        messages.success(self.request, f"You've returned '{borrow.book.title}' successfully.")
        return redirect('book_detail_page', pk=borrow.book.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        borrow = self.get_object()
        context['borrow'] = borrow
        return context
