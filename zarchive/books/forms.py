from django import forms
from zarchive.authors.models import Author
from zarchive.books.models import Book
from zarchive.genres.models import Genre


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_by', ]

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    custom_genre = forms.CharField(
        max_length=40,
        required=False,
        help_text="Can't find what you need? Enter a custom genre separated by commas.",
    )

    pages = forms.CharField()

    year_of_publish = forms.CharField()

    publisher = forms.CharField()

    def clean_author(self):
        author_name = self.cleaned_data.get('author')
        author, _ = Author.objects.get_or_create(name=author_name)
        return author

    def clean_custom_genre(self):
        custom_genre = self.cleaned_data.get('custom_genre', '')
        if custom_genre:
            custom_genres_list = custom_genre.split(',')
            if not all(genre.isalpha() for genre in custom_genres_list):
                raise forms.ValidationError("Genres should only contain letters.")
            return ','.join(custom_genres_list)
        return custom_genre


class CreateBookForm(BaseBookForm):
    class Meta(BaseBookForm.Meta):
        fields = ['title', 'author', 'description', 'genres', 'custom_genre', 'pages', 'year_of_publish', 'publisher',
                  'cover_image']

    author = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        print(self.cleaned_data)
        author_name = self.cleaned_data['author']
        author, created = Author.objects.get_or_create(name=author_name)

        genres = list(self.cleaned_data.pop('genres', []))
        custom_genre = self.cleaned_data.get('custom_genre', '')

        if custom_genre:
            for genre_name in custom_genre.split(','):
                genre, created = Genre.objects.get_or_create(name=genre_name)
                genres.append(genre)

        book = super().save(commit=False)
        book.author = author
        book.created_by = self.user

        if commit:
            book.save()
            book.genre.set(genres)
            self.save_m2m()
        return super().save(commit)


class EditBookForm(BaseBookForm):
    class Meta(BaseBookForm.Meta):
        fields = ['description', 'genres', 'custom_genre', 'pages', 'year_of_publish', 'publisher', 'cover_image']
