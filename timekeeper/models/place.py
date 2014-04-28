from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Place(models.Model):
    class Meta:
        app_label = "timekeeper"

    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.name)


@receiver(post_save, sender=Place)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_place item_id:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    place = instance
    d = {
        'type': 'timekeeper_place',
        'id': str(uuid.uuid4()),
        'item_id': place.id,
        'name': place.name,
        'latitude_coordinate': place.latitude,  # This uses the dynamic fields for lat/lon in Solr.
        'longitude_coordinate': place.longitude,
        'created': place.created,
        'updated': place.updated
    }
    solrconn.add(**d)
    solrconn.commit()


@receiver(post_delete, sender=Place)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_place item_id:{0}".format(instance.id), q_op="AND")
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
