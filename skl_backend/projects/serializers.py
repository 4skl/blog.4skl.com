from rest_framework import serializers
from .models import Tag, Project

# Serializers define the API representation.
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'description', 'color']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'content', 'image', 'url', 'git', 'tags', 'featured', 'date_created', 'date_updated']