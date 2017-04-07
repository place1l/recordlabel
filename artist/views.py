from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Artist


def index(request):
    all_artists = Artist.objects.all()
    return render(request, 'artist/index.html', {'all_artists' : all_artists})

def artist(request, artist_id):
    try:
        artist = Artist.objects.get(pk = artist_id)
    except Artist.DoesNotExist:
        raise Http404("Artist Not Found")
    return render(request, 'artist/artist.html', {'artist' : artist})
