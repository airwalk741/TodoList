from django.db import models
from django.contrib.auth import settings

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    checked = models.BooleanField(default=False)
    is_update_form = models.BooleanField(default=False)
