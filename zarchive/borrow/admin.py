from django.contrib import admin
from zarchive.borrow.models import Borrow


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = (
        'borrower',
        'book',
        'borrow_date',
        'return_date',
        'returned_at',
        'is_returned',
    )

    list_filter = (
        'borrow_date',
        'return_date',
        'is_returned',
    )

    search_fields = (
        'borrower__username',
        'borrower__email',
        'book__title',
    )

    autocomplete_fields = (
        'borrower',
        'book',
    )

    readonly_fields = ('borrow_date',)

    fieldsets = (
        (None, {
            'fields': ('borrower', 'book', 'borrow_date')
        }),
        ('Return Info', {
            'fields': ('return_date', 'returned_at', 'is_returned')
        }),
    )
