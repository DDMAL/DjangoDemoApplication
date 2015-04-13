from django.db import models


class Person(models.Model):
    class Meta:
        app_label = "codekeeper"

    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)