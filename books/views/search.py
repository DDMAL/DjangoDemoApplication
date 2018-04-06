from django.conf import settings
from rest_framework import generics
from rest_framework import response
import pysolr


class SearchView(generics.GenericAPIView):
    template_name = "search.html"

    def get(self, request, *args, **kwargs):
        connection = pysolr.Solr(settings.SOLR_SERVER)
        query = request.GET.get('q', None)

        if not query:
            return response.Response({})

        field_list = ["title_s", "author_s", "first_name_s", "last_name_s", "type", "pk"]
        results = connection.search(query, fl=field_list )
        return response.Response(results.docs)
