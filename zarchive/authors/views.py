from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from zarchive.authors.forms import AuthorCreateForm, AuthorEditForm
from zarchive.authors.models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list_page.html'
    context_object_name = 'author_list'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.all().order_by('-created_at')


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    pk_url_kwarg = 'pk'
    template_name = 'authors/author_detail_page.html'
    context_object_name = 'author'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'books/create_book_page.html'
    success_url = reverse_lazy('home-page')


class AuthorEditView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit_author_page.html'

    def get_success_url(self):
        return reverse_lazy('author_detail_page', kwargs={'pk': self.object.pk})


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    pk_url_kwarg = 'pk'
    template_name = 'authors/delete_author_page.html'
    success_url = reverse_lazy('author_list_page')
