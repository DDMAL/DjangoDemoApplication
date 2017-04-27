from rest_framework import serializers
from books.models.author import Author
from books.models.book import Book


class AuthorBooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    books = AuthorBooksSerializer(many=True)
