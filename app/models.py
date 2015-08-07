from django.core.urlresolvers import reverse_lazy as reverse 
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={ 'slug': self.slug })

    @property
    def tag_list(self):
        return self.tags.split(',')
