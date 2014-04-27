from timekeeper.models.activity import Activity
from timekeeper.models.place import Place
from rest_framework import serializers

class PlaceActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceActivitySerializer()

    class Meta:
        model = Activity