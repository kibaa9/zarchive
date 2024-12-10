from django import forms

from zarchive.publishers.models import Publisher


class BasePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherCreateForm(BasePublisherForm):
    pass


class PublisherUpdateForm(BasePublisherForm):
    pass
