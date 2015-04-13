from rest_framework import serializers
from codekeeper.models.tag import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag