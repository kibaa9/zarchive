from django.contrib import admin

from zarchive.authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_birth',
        'date_of_death',
        'slug',
    )

    list_filter = (
        'date_of_birth',
        'date_of_death',
    )

    search_fields = (
        'name',
        'bio',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    readonly_fields = ('slug',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'bio', 'profile_picture')
        }),
        ('Life Dates', {
            'fields': ('date_of_birth', 'date_of_death')
        }),
    )
