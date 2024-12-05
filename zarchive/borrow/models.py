from django.db import models
from zarchive.accounts.models import AppUser
from zarchive.books.models import Book


class Borrow(models.Model):
    borrower = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='borrowers',
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='borrows',
    )

    borrow_date = models.DateField(
        auto_now_add=True,
    )

    return_date = models.DateField(
        blank=True,
        null=True,
    )

    returned_at = models.DateField(
        blank=True,
        null=True,
    )

    is_returned = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.borrower} borrowing {self.book}'
