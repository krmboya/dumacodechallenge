from django.db import models

class County(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                           blank=True)

    def __unicode__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                           blank=True)
    county = models.ForeignKey(County)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                           blank=True)
    lat = models.CharField(max_length=255, default='0.000000',
                           blank=True)
    lon = models.CharField(max_length=255, default='0.000000',
                           blank=True)
    ward = models.ForeignKey(Ward)

    def __unicode__(self):
        return self.name

                            
