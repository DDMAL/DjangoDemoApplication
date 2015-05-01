from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    class Meta:
        fields = ('type', 'title')


    def to_representation(self, instance):
        print(self.fields)