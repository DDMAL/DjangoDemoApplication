from rest_framework import generics


class AuthorsListView(generics.ListCreateAPIView):
    pass


class AuthorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass
