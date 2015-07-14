from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from app.models import *


class PostView(TemplateView):
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)

        context['post'] = get_object_or_404(Post, slug=kwargs.get('slug'))

        return context
