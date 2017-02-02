from rest_framework import serializers
from . import models
from comment.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    comments_data = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = ('title', 'text', 'comments_data', 'primary_key')

    def get_comments_data(self, obj):
        return CommentSerializer(obj.comments, many=True, read_only=True).data
