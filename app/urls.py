from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('app.modules.pages.urls', namespace='pages')),
    url(r'^posts/', include('app.modules.posts.urls', namespace='posts')),

    url(r'^admin/', include(admin.site.urls)),
]
