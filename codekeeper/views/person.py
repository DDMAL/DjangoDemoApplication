from rest_framework import generics
from rest_framework import renderers
from codekeeper.models.person import Person
from codekeeper.serializers.person import PersonSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class PersonList(generics.ListCreateAPIView):
    template_name = "person/person_list.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "person/person_detail.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()