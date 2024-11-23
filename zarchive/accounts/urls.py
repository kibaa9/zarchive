from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from zarchive.accounts import views


urlpatterns = [
    path('create/', views.CreateUserPage.as_view(), name='create_user_page'),
    path('login/', views.LoginPage.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
]
