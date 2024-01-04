from rest_framework import serializers
from .models import Tag, Project

# Serializers define the API representation.
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'color']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['handle', 'title', 'description', 'content', 'image', 'url', 'git', 'tags', 'featured', 'date_created', 'date_updated']

class ProjectListSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = Project
        fields = ['link', 'handle', 'title', 'description', 'image', 'url', 'git', 'tags', 'featured', 'date_created', 'date_updated']