from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class ImageDetail(models.Model):
    upload_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    tags = TaggableManager()
