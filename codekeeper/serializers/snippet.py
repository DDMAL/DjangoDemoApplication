from rest_framework import serializers
from codekeeper.models.snippet import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet