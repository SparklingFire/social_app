from django.views import generic
from rest_framework import views
from rest_framework.response import Response
from . import models
from . import serializers


class Index(generic.TemplateView):
    template_name = 'index.html'


class EventList(views.APIView):
    def get(self, request):
        queryset = models.Article.objects.all()
        serializer = serializers.ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
