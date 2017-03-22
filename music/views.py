from django.http import HttpResponse
from .models import Track
from django.template import loader

def index(request):
    all_tracks = Track.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_tracks' : all_tracks,
    }
    return HttpResponse(template.render(context, request))

#@TODO: need a template for track -- Track title displayed
def track(request, track_id):
    return HttpResponse("<h2>track " + str(track_id) + "</h2>")
