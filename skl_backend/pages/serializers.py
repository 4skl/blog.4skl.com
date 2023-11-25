from rest_framework import serializers
from .models import Page

# Serializers define the API representation.
class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['handle', 'title', 'content', 'date_created', 'date_updated']
