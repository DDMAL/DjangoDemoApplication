from django.db import models


class Author(models.Model):
    class Meta:
        app_label = "books"

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)
