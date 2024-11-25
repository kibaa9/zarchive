from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from zarchive.accounts.forms import AppUserForm, ProfileForm
from zarchive.accounts.models import AppUser, Profile


class CreateUserPage(CreateView):
    template_name = 'user/create_user.html'
    model = AppUser
    form_class = AppUserForm
    success_url = reverse_lazy('home-page')


class LoginPage(LoginView):
    template_name = 'user/login_page.html'


class ProfileDetailsPage(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user/user_profile_page.html'
    context_object_name = 'profile'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     profile = self.object
    #     context['review_count'] = profile.user.reviews.annotate(books_count=Count('book'))
    #     return context


class EditProfilePage(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user/profile_edit_page.html'
    success_url = reverse_lazy('profile_details_page')


class UserDeletePage(LoginRequiredMixin, DeleteView):
    model = AppUser
    template_name = 'user/user_delete_page.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return self.request.user
