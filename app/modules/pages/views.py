from django.views.generic import TemplateView

from app.models import *


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['posts'] = Post.objects.order_by('-date_posted')

        return context
