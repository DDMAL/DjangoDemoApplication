from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import pysolr
from books.serializers.search.author import AuthorSearchSerializer
from books.models.author import Author


@receiver(post_save, sender=Author)
def index_author(sender, instance, created, **kwargs):
    connection = pysolr.Solr(settings.SOLR_SERVER)
    existing = connection.search("*:*", fq=["type:author", "pk:{0}".format(instance.pk)])
    if existing.hits > 0:
        for doc in existing.docs:
            connection.delete(id="{0}".format(doc["id"]))

    data = AuthorSearchSerializer(instance).data
    connection.add([data])
    connection.commit()


@receiver(post_delete, sender=Author)
<<<<<<< HEAD
def delete_book(sender, instance, **kwargs):
    connection = pysolr.Solr(settings.SOLR_SERVER)
    existing = connection.search("*:*", fq=["type:author", "pk:{0}".format(instance.pk)])
    if existing.hits > 0:
        for doc in existing.docs:
            connection.delete(id="{0}".format(doc['id']))
=======
def delete_author(sender, instance, **kwargs):
    pass
>>>>>>> resolve
