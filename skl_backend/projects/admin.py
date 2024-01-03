from django.contrib import admin
from .models import Tag, Project

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('handle',)