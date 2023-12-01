from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Page(models.Model):
    handle = models.SlugField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Pages'