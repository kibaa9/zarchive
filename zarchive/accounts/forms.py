from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from zarchive.accounts.models import Profile


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

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 55,
            }
        )
    )


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['name', 'description', 'date_of_birth', 'profile_picture']

    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    widgets = {
        'date_of_birth': forms.DateInput(attrs={
            'type': 'date',
        }),
    }