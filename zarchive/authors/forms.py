from django import forms
from zarchive.authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['slug', ]

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 50,
            }
        )
    )


class AuthorCreateForm(BaseAuthorForm):
    pass


class AuthorEditForm(BaseAuthorForm):
    pass
