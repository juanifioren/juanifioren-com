from django.conf.urls import include, url

from app.modules.posts.views import *


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PostView.as_view(), name='post'),
    url(r'^tag/(?P<tag>[-\w]+)/$', PostsTagView.as_view(), name='posts-tag'),
]
