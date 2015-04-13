from rest_framework import serializers
from codekeeper.models.person import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person