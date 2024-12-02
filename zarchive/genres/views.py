from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from zarchive.books.models import Book
from zarchive.genres.forms import GenreEditForm, GenreCreateForm
from zarchive.genres.models import Genre


class GenreListView(ListView):
    model = Genre
    template_name = 'genre/genre_catalogue_page.html'
    context_object_name = 'genre_list'
    paginate_by = 20

    def get_queryset(self):
        return Genre.objects.all().order_by('name')


class BookByGenreListView(ListView):
    model = Book
    template_name = 'books/book_catalogue_page.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        genre_id = self.kwargs.get('pk')
        self.genre = get_object_or_404(Genre, pk=genre_id)
        return Book.objects.filter(genre=self.genre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = self.genre
        return context


class GenreCreateView(CreateView):
    models = Genre
    form_class = GenreCreateForm
    template_name = 'genre/genre_create_page.html'
    success_url = reverse_lazy('genre_catalogue_page')


class GenreEditView(UpdateView):
    model = Genre
    form_class = GenreEditForm
    template_name = 'genre/genre_edit_page.html'
    success_url = reverse_lazy('genre_catalogue_page')


class GenreDeleteView(DeleteView):
    model = Genre
    pk_url_kwarg = 'pk'
    template_name = 'genre/genre_delete_page.html'
    success_url = reverse_lazy('genre_catalogue_page')

