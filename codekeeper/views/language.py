from rest_framework import generics
from rest_framework import renderers
from codekeeper.models.language import Language
from codekeeper.serializers.language import LanguageSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class LanguageList(generics.ListCreateAPIView):
    template_name = "language/language_list.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Language
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "language/language_detail.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Language
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
