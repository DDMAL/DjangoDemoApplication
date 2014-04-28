from timekeeper.models.activity import Activity
from timekeeper.serializers.activity import ActivitySerializer
from timekeeper.renderers.custom_html_renderer import CustomHTMLRenderer
from rest_framework.renderers import JSONRenderer, JSONPRenderer
from rest_framework import generics


class ActivityListHTMLRenderer(CustomHTMLRenderer):
    template_name = "activity/activity_list.html"


class ActivityDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "activity/activity_detail.html"


class ActivityList(generics.ListCreateAPIView):
    model = Activity
    serializer_class = ActivitySerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, ActivityListHTMLRenderer)


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Activity
    serializer_class = ActivitySerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, ActivityDetailHTMLRenderer)
