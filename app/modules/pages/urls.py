from django.conf.urls import include, url

from app.modules.pages.views import *


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
