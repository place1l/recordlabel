from django.http import Http404
from django.http import HttpResponse
from .models import Track
from django.shortcuts import render

def index(request):
    all_tracks = Track.objects.all()
    return render(request, 'music/index.html', {'all_tracks' : all_tracks})

#@TODO: need a template for track -- Track title displayed
def track(request, track_id):
    try:
        track = Track.objects.get(pk = track_id)
    except Track.DoesNotExist:
        raise Http404("Track Not Found")
    return render(request, 'music/track.html', {'track' : track})
