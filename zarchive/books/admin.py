from django.contrib import admin
from zarchive.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'year_of_publish',
        'is_available',
        'is_approved',
        'created_by',
        'created_at',
    )

    list_filter = (
        'is_available',
        'is_approved',
        'year_of_publish',
        'created_by',
    )

    search_fields = (
        'title',
        'author__name',
        'description',
    )

    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    filter_horizontal = ('genre',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'description', 'genre', 'cover_image')
        }),
        ('Publishing Info', {
            'fields': ('pages', 'year_of_publish', 'publisher')
        }),
        ('Management', {
            'fields': ('is_available', 'is_approved', 'created_by', 'created_at')
        }),
    )
