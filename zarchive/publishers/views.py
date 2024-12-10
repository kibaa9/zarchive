from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zarchive.books.models import Book
from zarchive.publishers.forms import PublisherCreateForm, PublisherUpdateForm
from zarchive.publishers.models import Publisher


class PublisherListView(LoginRequiredMixin, ListView):
    model = Publisher
    template_name = 'publishers/publisher_list_page.html'
    context_object_name = 'publishers'


class PublisherDetailView(LoginRequiredMixin, DetailView):
    model = Publisher
    template_name = 'publishers/publisher_detail_page.html'
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = self.object
        context['books'] = Book.objects.filter(publisher=publisher.name)
        context['book_count'] = Book.objects.filter(publisher=publisher.name).count()
        return context


class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'publishers/publisher_create_page.html'
    success_url = reverse_lazy('home-page')


class PublisherEditView(LoginRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherUpdateForm
    template_name = 'publishers/publisher_edit_page.html'

    def get_success_url(self):
        return reverse_lazy('author_detail_page', kwargs={'pk': self.object.pk})


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('publisher_list_page')
