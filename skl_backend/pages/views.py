from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Page
from .serializers import PageSerializer

# Create your views here.
class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all() #.filter(published=True) #.order_by('date_created') if we move to a blog model for pages

    def retrieve(self, request, *args, **kwargs):
        page = self.get_object()
        serializer = PageSerializer(page)
        return Response(serializer.data)