from rest_framework import serializers
from books.models.author import Author


class AuthorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name_s', 'last_name_s', 'pk', 'type')

    first_name_s = serializers.CharField(source="first_name")
    last_name_s = serializers.CharField(source="last_name")
    pk = serializers.IntegerField(source="id")
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.__class__.__name__.lower()
