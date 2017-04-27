from rest_framework import generics
from books.models.author import Author
from books.serializers.author import AuthorSerializer


class AuthorsListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    template_name = "author_list.html"


class AuthorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    template_name = "author_detail.html"
