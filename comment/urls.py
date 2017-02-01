from django.conf.urls import url
from comment.views import CommentView


urlpatterns = [
    url('^comment/(?P<pk>[0-9]+)/$', CommentView.as_view(), name='comment-view')
]
