from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)    
    subtitle = models.CharField(max_length=200)
    description = RichTextUploadingField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True, default="")
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

def __str__(self):
    return self.title

