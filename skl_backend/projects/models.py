from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tags'

class Project(models.Model):
    handle = models.SlugField(max_length=100, primary_key=True, blank=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    content = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)
    git = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.handle = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'