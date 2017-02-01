from article.models import Article
from comment.models import Comment
from django.db.models.signals import (post_save)
from django.dispatch import receiver
from .models import (RatingModel, Vote)


@receiver(post_save, sender=Article)
@receiver(post_save, sender=Comment)
def rating_model_save(sender, instance, **kwargs):
    if len(instance.rating_object.all()) < 1:
        RatingModel.objects.create(content_object=instance,
                                   user_rating=instance.author.get_user_rating_object())
