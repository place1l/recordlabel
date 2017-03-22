from django.http import HttpResponse
from .models import Track

def index(request):
    all_tracks = Track.objects.all()
    html = ''
    for track in all_tracks:
        url = '/music/' + str(track.id) + '/'
        html += '<a href="'+ url +'">'+track.track_title+'</a></br>'
    return HttpResponse(html)

def track(request, track_id):
    return HttpResponse("<h2>track " + str(track_id) + "</h2>")
