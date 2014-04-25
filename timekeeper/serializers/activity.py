from timekeeper.models.activity import Activity
from rest_framework import serializers

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity