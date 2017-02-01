from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'title: {0}, id: {1}'.format(self.title, self.id)
