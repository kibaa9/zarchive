from django.contrib import admin
from zarchive.genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

    search_fields = ('name',)
