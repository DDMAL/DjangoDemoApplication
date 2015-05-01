from rest_framework import serializers
from codekeeper.models.language import Language


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
