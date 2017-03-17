from __future__ import unicode_literals

from django.db import models

class Bio(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_location = models.CharField(max_length=100)
    artist_bio = models.CharField(max_length=1000)
    artist_picture = models.CharField(max_length=1500)
