from django.apps import AppConfig


class BooksAppConfig(AppConfig):
    name = "books.books"
    verbose_name = "Books"

    def ready(self):
        pass