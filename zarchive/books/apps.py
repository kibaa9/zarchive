from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zarchive.books'

    def ready(self):
        import zarchive.books.signals
