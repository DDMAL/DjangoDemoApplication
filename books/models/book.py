from django.db import models


class Book(models.Model):
    class Meta:
        app_label = "books"

    title = models.CharField(max_length=255)
    author = models.ForeignKey("books.Author")

    def __str__(self):
        return "{0}".format(self.title)
