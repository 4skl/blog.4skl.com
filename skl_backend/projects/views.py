from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Tag, Project
from .serializers import TagSerializer, ProjectSerializer, ProjectListSerializer
# Create your views here.

# ViewSets define the view behavior.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        queryset = self.queryset
        ids = request.query_params.get('ids', None)
        if ids is not None:
            try:
                ids = [int(id) for id in ids.split(',')]
            except ValueError:
                ids = []
            queryset = self.queryset.filter(id__in=ids)
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    ordering_fields = ['name', 'created']
    queryset = Project.objects.filter(published=True).order_by('-date_created')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer
    
    # Add a custom action to filter by tag
    @action(detail=False)
    def tag(self):
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