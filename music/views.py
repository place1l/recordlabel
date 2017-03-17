from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>MUSIC HOMEPAGE</h1>")
