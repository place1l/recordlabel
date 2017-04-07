from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    #eventually a file will be uploaded for artist_picture
    picture = models.CharField(max_length=1500)
    #eventually a file will be uploaded for example_tracks
    tracks = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
