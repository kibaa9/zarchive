from django.views.generic import ListView
from zarchive.books.models import Book


class HomePage(ListView):
        model = Book
        template_name = 'common/home.html'
        context_object_name = 'book_list'
        paginate_by = 10
