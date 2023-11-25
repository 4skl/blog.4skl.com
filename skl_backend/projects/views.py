from django.shortcuts import render
from rest_framework import viewsets
from .models import Tag, Project
from .serializers import TagSerializer, ProjectSerializer
# Create your views here.

# ViewSets define the view behavior.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer