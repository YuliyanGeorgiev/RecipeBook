from django.conf.urls import url
from . import views

app_name='food'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<post_id>[0-9]+)/vote$', views.vote, name="vote"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.comment, name='comment'),

]