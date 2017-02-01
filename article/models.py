from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import RatingModel


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now, editable=False)
    edited = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    primary_key = models.SlugField(primary_key=True, editable=False, unique=True)
    rating_object = GenericRelation(RatingModel)

    def __str__(self):
        return 'title: {0}, id: {1}'.format(self.title, self.primary_key)

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        self.pk = slugify(self.title)
        return super().save(*args, **kwargs)
