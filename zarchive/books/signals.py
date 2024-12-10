from cloudinary.templatetags import cloudinary
from django.db.models.signals import post_delete
from django.dispatch import receiver
from zarchive.books.models import Book


@receiver(post_delete, sender=Book)
def delete_cover_image(sender, instance, **kwargs):
    if instance.cover_image:
        cloudinary.uploader.destroy(instance.cover_image.public_id)
