from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models

from zarchive.accounts.models import AppUser, Profile


class AppUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email',)


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_author', 'slug']

    widgets = {
        'date_of_birth': forms.DateInput(attrs={
            'type': 'date',
        }),
    }
