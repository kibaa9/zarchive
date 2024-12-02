from django import forms

from zarchive.authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['slug', ]


class AuthorCreateForm(BaseAuthorForm):
    pass


class AuthorEditForm(BaseAuthorForm):
    pass
