from timekeeper.models.place import Place
from timekeeper.serializers.place import PlaceSerializer
from timekeeper.renderers.custom_html_renderer import CustomHTMLRenderer
from rest_framework.renderers import JSONRenderer, JSONPRenderer
from rest_framework import generics


class PlaceListHTMLRenderer(CustomHTMLRenderer):
    template_name = "place/place_list.html"


class PlaceDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "place/place_detail.html"


class PlaceList(generics.ListCreateAPIView):
    model = Place
    serializer_class = PlaceSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PlaceListHTMLRenderer)


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Place
    serializer_class = PlaceSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PlaceDetailHTMLRenderer)