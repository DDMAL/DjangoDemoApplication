from timekeeper.models.person import Person
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.Field(source="full_name")

    class Meta:
        model = Person