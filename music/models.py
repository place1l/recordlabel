from __future__ import unicode_literals

from django.db import models

class Track(models.Model):
    file_type = models.CharField(max_length=10)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    track_title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    #eventually a file will be uploaded for track
    track = models.CharField(max_length=1000)
    #eventually a file will be uploaded for track_pic
    track_pic = models.CharField(max_length=1000)

class Compilation(models.Model):
    comp_title = models.CharField(max_length=250)
