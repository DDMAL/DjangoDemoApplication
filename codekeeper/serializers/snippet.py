from codekeeper.models.snippet import Snippet
from codekeeper.models.tag import Tag
from codekeeper.models.person import Person
from rest_framework import serializers


class CreatorSnippetSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    class Meta:
        model = Person
        fields = ('url', 'full_name')


class TagSnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSnippetSerializer(many=True)
    creator = CreatorSnippetSerializer()

    class Meta:
        model = Snippet