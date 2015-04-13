from rest_framework import generics
from rest_framework import renderers
from codekeeper.models.snippet import Snippet
from codekeeper.serializers.snippet import SnippetSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class SnippetList(generics.ListCreateAPIView):
    template_name = "snippet/snippet_list.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Snippet
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "snippet/snippet_detail.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Snippet
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
