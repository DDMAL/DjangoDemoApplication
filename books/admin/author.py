from django.contrib import admin
from books.models.author import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
