from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zarchive.books.forms import CreateBookForm, EditBookForm
from zarchive.books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.all().order_by('-created_at')


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'books/book_detail_page.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'books/create_book_page.html'
    success_url = reverse_lazy('home-page')

    def get_form_kwargs(self):
        """Pass the current user to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BookUpdateView(UpdateView):
    model = Book
    form_class = EditBookForm
    template_name = 'books/book_edit_page.html'

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})


class BookDeleteView(DeleteView):
    pass
