from __future__ import unicode_literals

from django.db import models

class UpcomingEvent(models.Model):
    artist = models.CharField(max_length=50)
    event_title = models.CharField(max_length=50)
    event_info = models.CharField(max_length=500)
    location = models.CharField(max_length=75)
    
