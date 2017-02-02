from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.create(text=validated_data.pop('text'),
                                         author=validated_data.pop('author'),
                                         article=validated_data.pop('article'))
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.text = validated_data.pop('text')
        return instance
