from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=512)
    authors = models.CharField(max_length=512)
    jornal_info = models.CharField(max_length=512)
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']