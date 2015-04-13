from rest_framework import views
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class HomePageView(views.APIView):
    template_name = "index.html"
    renderer_classes = (renderers.JSONRenderer, CustomHTMLRenderer, renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        response = Response({
            'snippets': reverse('snippet-list', request=request),
            # 'tags': reverse('tag-list', request=request),
            # 'people': reverse('person-list', request=request)
        })
        return response