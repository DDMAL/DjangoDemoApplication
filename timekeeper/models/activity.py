from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


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


@receiver(post_save, sender=Activity)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_activity item_id:{0}".format(instance.id))
    if record:
        solrconn.delete(record.results[0]['id'])

    activity = instance
    d = {
        'type': 'timekeeper_activity',
        'id': str(uuid.uuid4()),
        'item_id': activity.id,
        'title': activity.title,
        'start_time': activity.start_time,
        'end_time': activity.end_time,
        'created': activity.created,
        'updated': activity.updated
    }
    solrconn.add(**d)
    solrconn.commit()


@receiver(post_delete, sender=Activity)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_activity item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
