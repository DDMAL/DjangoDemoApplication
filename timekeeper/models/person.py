from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


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


@receiver(post_save, sender=Person)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_person item_id:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    person = instance
    d = {
        'type': 'timekeeper_person',
        'id': str(uuid.uuid4()),
        'item_id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'created': person.created,
        'updated': person.updated
    }
    solrconn.add(**d)
    solrconn.commit()


@receiver(post_delete, sender=Person)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:timekeeper_person item_id:{0}".format(instance.id), q_op="AND")
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
