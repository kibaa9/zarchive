from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Avg
from django.http import request
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zarchive.books.forms import BookCreateForm, BookEditForm
from zarchive.books.models import Book
from zarchive.borrow.models import Borrow
from zarchive.reviews.forms import ReviewCreateForm


class BookListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.all().annotate(
            total_rating=Sum('reviews__rating'),
            average_rating=Avg('reviews__rating')
        ).order_by('-created_at')


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'books/book_detail_page.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()

        self.object = Book.objects.annotate(
            average_rating=Avg('reviews__rating')
        ).get(pk=self.object.pk)

        context['average_rating'] = self.object.average_rating or 0

        if self.request.user.is_authenticated:
            user_review = self.object.reviews.filter(user=self.request.user).first()
            if user_review:
                context['user_review'] = user_review

        context['form'] = kwargs.get('form') or ReviewCreateForm()

        user_borrow = Borrow.objects.filter(book=self.object, borrower=self.request.user, is_returned=False).first()
        context['user_borrow'] = user_borrow

        user_borrow_info = Borrow.objects.filter(book=self.object, is_returned=False).first()
        context['user_borrow_info'] = user_borrow_info

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to submit a review.")
            return redirect('login')

        if self.object.reviews.filter(user=request.user).exists():
            messages.error(request, "You have already reviewed this book.")
            return redirect('book_detail_page', pk=self.object.pk)

        form = ReviewCreateForm(request.POST, user=request.user, book=self.object)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been added successfully.")
            return redirect('book_detail_page', pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'books/create_book_page.html'
    success_url = reverse_lazy('home-page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BookEditView(UpdateView):
    model = Book
    form_class = BookEditForm
    template_name = 'books/book_edit_page.html'

    def get_success_url(self):
        return reverse_lazy('book_detail_page', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['genre'] = self.object.genre.all()
        print(f"Initial genres: {initial['genre']}")
        return initial


class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'books/book_delete_page.html'
    success_url = reverse_lazy('book_catalogue_page')


class BookTopListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.all().annotate(
            total_rating=Sum('reviews__rating'),
            average_rating=Avg('reviews__rating')
        ).order_by('-average_rating')


class BookAvailableListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.all().filter(is_available=True).annotate(
            total_rating=Sum('reviews__rating'),
            average_rating=Avg('reviews__rating')
        ).order_by('-average_rating')


class BookBorrowListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(borrows__borrower=self.request.user, borrows__is_returned=False).order_by('-borrows__return_date')


class UserListBooksView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(created_by=user)
