from django.db import models

class TrackerLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tracker_id = models.ForeignKey('Tracker', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tracker_locations'

class Tracker(models.Model):
    name = models.CharField(max_length=100)
    tracker_id = models.CharField(max_length=100, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'trackers'
