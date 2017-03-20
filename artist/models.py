from __future__ import unicode_literals

from django.db import models

class Bio(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_location = models.CharField(max_length=100)
    artist_bio = models.CharField(max_length=1000)
    #eventually a file will be uploaded for artist_picture
    artist_picture = models.CharField(max_length=1500)
    #eventually a file will be uploaded for example_tracks
    example_tracks = models.CharField(max_length=1000)
