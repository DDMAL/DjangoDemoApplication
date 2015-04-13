from django.db import models


class Tag(models.Model):
    class Meta:
        app_label = "codekeeper"

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(self.name)