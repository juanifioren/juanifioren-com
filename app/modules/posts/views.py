from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from app.models import *


class PostView(TemplateView):
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)

        context['post'] = get_object_or_404(Post, slug=kwargs.get('slug'))

        context['disqus_shortname'] = settings.DISQUS_SHORTNAME

        return context

class PostsTagView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)

        context['tag'] = kwargs.get('tag','').lower()

        context['posts'] = Post.objects.filter(
        	tags__contains=context['tag']).order_by('-date_posted')

        return context
