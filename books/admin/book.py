from django.contrib import admin
from books.models.book import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
