from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.Index.as_view(), name='index'),
    url('^events/$', views.EventList.as_view(), name='event-list'),
]
