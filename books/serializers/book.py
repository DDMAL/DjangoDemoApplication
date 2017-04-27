from rest_framework import serializers
from books.models.book import Book
from books.models.author import Author


class BookAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    author = BookAuthorSerializer()
