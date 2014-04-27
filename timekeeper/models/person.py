from django.db import models

class Person(models.Model):
    class Meta:
        app_label = "timekeeper"
        verbose_name_plural = "people"

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

    def __unicode__(self):
        return u"{0}, {1}".format(self.last_name, self.first_name)
