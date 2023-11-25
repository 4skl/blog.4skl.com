from django.shortcuts import render
from rest_framework import viewsets
from .models import Page
from .serializers import PageSerializer

# Create your views here.
class PageHandleViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        handle = self.request.query_params.get('handle', None)
        if handle is not None:
            return Page.objects.filter(handle=handle)
        return Page.objects.none()  # return an empty queryset if no handle is provided

    serializer_class = PageSerializer