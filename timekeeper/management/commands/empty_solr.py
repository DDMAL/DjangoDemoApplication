from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import solr


class Command(BaseCommand):
    args = ""
    help = "Completely clear the Solr index"

    def handle(self, *args, **options):
        self.stdout.write("Deleting Solr Index: ", ending='')
        try:
            solrconn = solr.SolrConnection(settings.SOLR_SERVER)
            solrconn.delete_query("*:*")
            solrconn.commit()
        except Exception, e:
            raise CommandError('An error was returned from the Solr server: {0}'.format(e))

        self.stdout.write("Done.")
