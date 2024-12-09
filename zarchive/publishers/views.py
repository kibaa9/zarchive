from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from zarchive.books.models import Book
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
