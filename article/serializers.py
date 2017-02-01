from rest_framework import serializers
from . import models
from comment.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = models.Article
        fields = ('title', 'text', 'comments', 'primary_key')
