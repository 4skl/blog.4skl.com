from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tag, Project
from .serializers import TagSerializer, ProjectSerializer
# Create your views here.

# ViewSets define the view behavior.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(published=True)
    
    # Override the get_queryset method to allow for filtering by tag
    def get_queryset(self):
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            return self.queryset.filter(tags__name__in=[tag])
        return self.queryset
    
    # Add a custom action to return only featured projects
    @action(detail=False)
    def featured(self, request):
        queryset = self.queryset.filter(featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)