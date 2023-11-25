from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tags'

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)
    git = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag)

    featured = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'