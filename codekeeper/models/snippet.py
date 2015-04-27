from django.db import models


class Snippet(models.Model):
    class Meta:
        app_label = "codekeeper"

    title = models.CharField(max_length=256, blank=True, null=True)
    snippet = models.TextField()
    tags = models.ManyToManyField("codekeeper.Tag", blank=True)
    creator = models.ForeignKey("codekeeper.Person")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(self.title)