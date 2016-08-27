from django.conf.urls import patterns, url

urlpatterns = patterns('xin.blog.views',
    url(r'^$', 'blog', name='blog' ),
    )