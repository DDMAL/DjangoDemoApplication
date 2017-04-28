from rest_framework import serializers
from books.models.book import Book


class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

    title_s = serializers.CharField(source="title")
    author = serializers.CharField(source="author.last_name")
    pk = serializers.IntegerField(source="id")
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.__class__.__name__.lower()
