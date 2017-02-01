from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.Index.as_view(), name='index'),
    url('^news/$', views.NewsList.as_view(), name='news-list'),
    url('^news/(?P<pk>[0-9]+)/$', views.NewsDetails.as_view(), name='news-details'),
]
