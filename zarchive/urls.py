from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zarchive.common.urls')),
    path('account/', include('zarchive.accounts.urls')),
    path('book/', include('zarchive.books.urls')),
]
