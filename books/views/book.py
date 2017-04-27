from rest_framework import generics


class BooksListView(generics.ListCreateAPIView):
    pass


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass