from django.shortcuts import Http404
from rest_framework import views
from .models import Comment
from rest_framework import status
from rest_framework.response import Response
from .serializers import CommentSerializer


class CommentView(views.APIView):
    def get_comment(self, pk):
        try:
            Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        article = self.get_comment(pk)
        serializer = CommentSerializer(article, self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
