from rest_framework import generics
from books.models.book import Book
from books.serializers.book import BookSerializer


class BooksListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = "book_list.html"


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = "book_detail.html"
