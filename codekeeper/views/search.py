import scorched
from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from codekeeper.serializers.search import SearchSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer

class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        querydict = request.GET
        if not querydict:
            return Response({"results": []})

        solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
        resp = solrconn.query(title=querydict.get('q')).execute()
        records = [r for r in resp]
        print(records)
        s = self.get_serializer(records, many=True)

        print(s.data)
        return Response({'content': s.data})