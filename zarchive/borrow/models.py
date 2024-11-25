from django.db import models
from zarchive.accounts.models import AppUser
from zarchive.books.models import Book


class Borrow(models.Model):
    borrower = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
    )

    borrow_date = models.DateField(
        auto_now_add=True,
    )

    return_date = models.DateField(
        blank=True,
        null=True,
    )

    is_returned = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.borrower} borrowing {self.book}'
