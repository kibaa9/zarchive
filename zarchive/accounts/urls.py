from django.contrib.auth.views import LogoutView
from django.urls import path, include
from zarchive.accounts import views


urlpatterns = [
    path('create/', views.CreateUserPage.as_view(), name='create_user_page'),
    path('login/', views.LoginPage.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('profile/<slug:slug>/', include([
        path('', views.ProfileDetailsPage.as_view(), name='profile_details_page'),
        path('edit/', views.EditProfilePage.as_view(), name='profile_edit_page'),
    ]))
]
