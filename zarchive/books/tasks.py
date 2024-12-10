from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_book_approval_email(user_email, book_title):
    send_mail(
        subject='Your Book has been approved',
        message=f'Your Book {book_title} has been approved.',
        from_email="zarchive@OfficialEmails.scam",
        recipient_list=[user_email],
    )
