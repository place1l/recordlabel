from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^artist/', include('artist.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^', include('home.urls')),

]
