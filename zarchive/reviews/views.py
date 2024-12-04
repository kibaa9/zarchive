from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from zarchive.reviews.forms import ReviewEditForm
from zarchive.reviews.models import Review


class ReviewEditView(UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = 'reviews/review_edit_page.html'

    def get_success_url(self):
        return reverse_lazy('book_detail_page', kwargs={'pk': self.object.book.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    pk_url_kwarg = 'pk'
    template_name = 'reviews/review_delete_page.html'

    def get_success_url(self):
        return reverse_lazy('book_detail_page', kwargs={'pk': self.object.book.pk})
