from django import forms

from zarchive.genres.models import Genre


class GenreBaseForm(forms.ModelForm):
    class Meta:
        model = Genre
        exclude = ['id', ]


class GenreCreateForm(GenreBaseForm):
    pass


class GenreEditForm(GenreBaseForm):
    pass
