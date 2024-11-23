from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from zarchive.accounts.forms import AppUserForm
from zarchive.accounts.models import AppUser


class CreateUserPage(CreateView):
    template_name = 'user/create-user.html'
    model = AppUser
    form_class = AppUserForm
    success_url = reverse_lazy('home-page')


class LoginPage(LoginView):
    template_name = 'user/login_page.html'


