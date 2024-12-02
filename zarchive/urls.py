from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zarchive.common.urls')),
    path('account/', include('zarchive.accounts.urls')),
    path('books/', include('zarchive.books.urls')),
    path('authors/', include('zarchive.authors.urls')),
    path('genres/', include('zarchive.genres.urls')),
]
