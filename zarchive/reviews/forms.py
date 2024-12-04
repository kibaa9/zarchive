from django import forms
from django.core.exceptions import ValidationError

from zarchive.reviews.models import Review


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'book']


class ReviewCreateForm(ReviewBaseForm):
    def __init__(self, *args, user=None, book=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.book = book

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise ValidationError("Ensure this value is between 1 and 5.")
        return rating

    def clean(self):
        cleaned_data = super().clean()

        if not self.user or not self.book:
            raise ValidationError("User or book information is missing.")

        if Review.objects.filter(book=self.book, user=self.user).exists():
            raise ValidationError("You have already reviewed this book.")

        return cleaned_data


class ReviewEditForm(ReviewBaseForm):
    pass
