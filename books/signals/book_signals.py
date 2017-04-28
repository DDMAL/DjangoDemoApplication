from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import pysolr
from books.serializers.search.book import BookSearchSerializer
from books.models.book import Book


@receiver(post_save, sender=Book)
def index_book(sender, instance, created, **kwargs):
    connection = pysolr.Solr(settings.SOLR_SERVER)
    existing = connection.search("*:*", fq=["type:book", "pk:{0}".format(instance.pk)])
    if existing.hits > 0:
        for doc in existing.docs:
            connection.delete(id="{0}".format(doc["id"]))

    data = BookSearchSerializer(instance).data
    connection.add([data])
    connection.commit()


@receiver(post_delete, sender=Book)
def delete_book(sender, instance, **kwargs):
    connection = pysolr.Solr(settings.SOLR_SERVER)
    existing = connection.search("*:*", fq=["type:book", "pk:{0}".format(instance.pk)])
    if existing.hits > 0:
        for doc in existing.docs:
            connection.delete(id="{0}".format(doc['id']))
