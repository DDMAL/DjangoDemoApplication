from rest_framework import generics
from rest_framework import response


class SearchView(generics.GenericAPIView):
    template_name = "search.html"

    def get(self, request, *args, **kwargs):
        return response.Response({})