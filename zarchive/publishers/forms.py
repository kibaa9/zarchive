from django import forms
from zarchive.publishers.models import Publisher


class BasePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

    website = forms.URLField(
        widget=forms.TextInput(),
        required=False,
    )


class PublisherCreateForm(BasePublisherForm):
    pass


class PublisherUpdateForm(BasePublisherForm):
    pass
