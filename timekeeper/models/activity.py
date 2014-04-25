from django.db import models

class Activity(models.Model):
    class Meta:
        app_label = "timekeeper"
        verbose_name_plural = "activities"

    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.ForeignKey('timekeeper.Place')
    partner = models.ForeignKey('timekeeper.Person', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.title)