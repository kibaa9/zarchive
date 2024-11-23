from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from zarchive.accounts.models import AppUser


class AppUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if AppUser.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = '__all__'
