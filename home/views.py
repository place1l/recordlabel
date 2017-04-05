from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>HOMEPAGE</h1>\n<a href = /music/>Music</a>")
