from django import forms
from zarchive.authors.models import Author
from zarchive.books.models import Book
from zarchive.genres.models import Genre
from zarchive.publishers.models import Publisher
from zarchive.validators import AlphaValidator, LetterAndCommaValidator


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_by', ]

    title = forms.CharField(
        help_text="Notice: Title can not be changed after creation",
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '8', 'style': 'width: 100%;'}),  # Breaks if genre name is too long
        required=False,
    )

    custom_genre = forms.CharField(
        validators=[LetterAndCommaValidator(), ],
        max_length=40,
        required=False,
        help_text="Can't find what you need? Enter a custom genre separated by commas.",
    )

    pages = forms.CharField()

    year_of_publish = forms.CharField(
        help_text='Please enter and year between 1800 and 2100',
    )

    publisher = forms.CharField(
        required=False,
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 50,
                'placeholder': "Please don't share spoilers about the book"
            }
        )
    )

    def clean_author(self):
        author_name = self.cleaned_data.get('author')
        author, _ = Author.objects.get_or_create(name=author_name)
        return author

    def clean_custom_genre(self):
        custom_genre = self.cleaned_data.get('custom_genre', '')
        if custom_genre:
            custom_genres_list = custom_genre.split(',')
            return ','.join(custom_genres_list)
        return custom_genre


class BookCreateForm(BookBaseForm):
    class Meta(BookBaseForm.Meta):
        fields = ['title', 'author', 'description', 'genres', 'custom_genre', 'pages', 'year_of_publish', 'publisher',
                  'cover_image']

    author = forms.CharField(
        validators=[AlphaValidator(), ],
        help_text="Notice: Author can not be changed after creation",
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        author_name = self.cleaned_data['author']
        author, _ = Author.objects.get_or_create(name=author_name)

        if self.cleaned_data['publisher']:
            publisher = self.cleaned_data['publisher']
            publisher, _ = Publisher.objects.get_or_create(name=publisher)

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


class BookEditForm(BookBaseForm):
    class Meta(BookBaseForm.Meta):
        fields = ['description', 'genres', 'custom_genre', 'pages', 'year_of_publish', 'publisher', 'cover_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['genres'].initial = self.instance.genre.all()

    def save(self, commit=True):
        genres = list(self.cleaned_data.pop('genres', []))
        custom_genre = self.cleaned_data.get('custom_genre', '')

        if custom_genre:
            for genre_name in custom_genre.split(','):
                genre, created = Genre.objects.get_or_create(name=genre_name)
                genres.append(genre)

        book = super().save(commit=False)

        if commit:
            book.save()
            book.genre.set(genres)
            self.save_m2m()
        return super().save(commit)
