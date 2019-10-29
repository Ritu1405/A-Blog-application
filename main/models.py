from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length= 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    slug = models.SlugField(max_length= 200, default=1)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length = 60)
    body = models.TextField()
    created_on = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey('Website', on_delete = models.CASCADE)

    def __str__(self):
        return self.author


