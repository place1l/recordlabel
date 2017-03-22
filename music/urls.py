from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    #/music/track_id/
    url(r'^(?P<track_id>[0-9]+)/$', views.track, name='track'),
]
