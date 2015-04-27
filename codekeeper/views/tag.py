from rest_framework import generics
from rest_framework import renderers
from codekeeper.models.tag import Tag
from codekeeper.serializers.tag import TagSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class TagList(generics.ListCreateAPIView):
    template_name = "tag/tag_list.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Tag
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "tag/tag_detail.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Tag
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
