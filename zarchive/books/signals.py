from cloudinary.templatetags import cloudinary
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from zarchive.books.models import Book
from zarchive.books.tasks import send_book_approval_email


@receiver(post_delete, sender=Book)
def delete_cover_image(sender, instance, **kwargs):
    if instance.cover_image:
        cloudinary.uploader.destroy(instance.cover_image.public_id)


@receiver(post_save, sender=Book)
def send_book_approval_notification(sender, instance, created, **kwargs):
    if not created and instance.is_approved:
        print(instance)
        print(instance.title)
        print(instance.created_by.email)
        send_book_approval_email.delay(user_email=instance.created_by.email, book_title=instance.title)
