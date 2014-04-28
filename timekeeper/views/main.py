from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({'activities': reverse('activity-list', request=request, format=format),
                     'places': reverse('place-list', request=request, format=format),
                     'people': reverse('person-list', request=request, format=format)})


@ensure_csrf_cookie
def home(request):
    data = {}
    return render(request, "index.html", data)
