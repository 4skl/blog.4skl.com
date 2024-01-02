from django.contrib import admin
from .models import Tag, Project

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  # Display only the ID of each tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass