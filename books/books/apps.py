from django.apps import AppConfig


class BooksAppConfig(AppConfig):
    name = "books"
    verbose_name = "Books"

    def ready(self):
        import books.signals