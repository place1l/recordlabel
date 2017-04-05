from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>HOMEPAGE</h1><ul><li><a href = /artist/>Artists</a></li><li><a href = /music/>Music</a></li><li><a href = /events/>Events</a></li></ul>")
