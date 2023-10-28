from django.contrib.gis.db import models

# Create your models here.

# class Alerts(models.Model):
#     id = models.AutoField(primary_key=True)
#     alert_type = models.CharField(max_length=255)
#     source = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     location = models.PointField()

class Pin(models.Model):
    