from timekeeper.models.person import Person
from timekeeper.serializers.person import PersonSerializer
from timekeeper.renderers.custom_html_renderer import CustomHTMLRenderer
from rest_framework.renderers import JSONRenderer, JSONPRenderer
from rest_framework import generics


class PersonListHTMLRenderer(CustomHTMLRenderer):
    template_name = "person/person_list.html"


class PersonDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "person/person_detail.html"


class PersonList(generics.ListCreateAPIView):
    model = Person
    serializer_class = PersonSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PersonListHTMLRenderer)

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Person
    serializer_class = PersonSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PersonDetailHTMLRenderer)