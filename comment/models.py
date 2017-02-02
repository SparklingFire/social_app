from django.db import models
from article.models import Article
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import RatingModel


class Comment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now, editable=False)
    edited = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    hidden = models.BooleanField(default=False)
    rating_object = GenericRelation(RatingModel)

    def __str__(self):
        return 'ID:{0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        try:
            if self.parent.parent:
                self.parent = self.parent.parent
        except AttributeError:
            pass
        if not self.author:
            self.hidden = True
        return super().save(*args, **kwargs)
